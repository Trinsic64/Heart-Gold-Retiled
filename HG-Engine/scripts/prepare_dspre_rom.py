"""Build an HG-Engine input with vanilla code and the latest DSPRE files.

Copy every named filesystem file by path from the latest DSPRE-edited ROM.
The clean ROM supplies ARM9, overlays, and the original file layout so the
engine can patch them once. Neither input is modified.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import tempfile
from pathlib import Path

import ndspy.narc
import ndspy.rom


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def file_digest(path: Path) -> str:
    result = hashlib.sha256()
    with path.open("rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            result.update(chunk)
    return result.hexdigest()


def named_files(rom: ndspy.rom.NintendoDSRom) -> dict[str, int]:
    return {
        name: file_id
        for file_id in range(len(rom.files))
        if (name := rom.filenames.filenameOf(file_id)) is not None
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--code-base", required=True, type=Path)
    parser.add_argument("--latest", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    code_path = args.code_base.resolve()
    latest_path = args.latest.resolve()
    output_path = args.output.resolve()
    if len({code_path, latest_path, output_path}) != 3:
        raise SystemExit("The prepared output must differ from both inputs.")

    code = ndspy.rom.NintendoDSRom.fromFile(str(code_path))
    latest = ndspy.rom.NintendoDSRom.fromFile(str(latest_path))
    if code.idCode != b"IPKE" or latest.idCode != b"IPKE":
        raise SystemExit("Both inputs must be US HeartGold ROMs (IPKE).")

    expected_code_arm9 = "5eeaa2dcabfb66b4ff5d151687cff2c9214de9e272ba7afdae7a01d57cf319af"
    expected_code_overlay = "a35a3a7072daaacbc2d8e5642ab076d4bc4606eb16c4687709a1bc24a80535be"
    if digest(code.arm9) != expected_code_arm9 or digest(code.files[1]) != expected_code_overlay:
        raise SystemExit("Clean HeartGold code ROM changed; inspect before preparing input.")

    code_names = named_files(code)
    latest_names = named_files(latest)
    if code_names.keys() != latest_names.keys() or len(code_names) != 384:
        raise SystemExit("Named filesystem paths changed; inspect before preparing input.")

    header_count = len(ndspy.narc.NARC(latest.files[latest_names["a/0/5/0"]]).files)
    script_count = len(ndspy.narc.NARC(latest.files[latest_names["a/0/1/2"]]).files)
    if header_count != 627 or script_count != 1139:
        raise SystemExit(f"Unexpected DSPRE archive counts: {header_count} headers, {script_count} scripts.")

    for name, file_id in code_names.items():
        code.files[file_id] = latest.files[latest_names[name]]

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(dir=output_path.parent, prefix=output_path.name + ".", suffix=".nds", delete=False) as temp:
        temp_path = Path(temp.name)
    try:
        code.saveToFile(str(temp_path))
        check = ndspy.rom.NintendoDSRom.fromFile(str(temp_path))
        if digest(check.arm9) != expected_code_arm9 or digest(check.files[1]) != expected_code_overlay:
            raise RuntimeError("Clean code did not round-trip.")
        check_names = named_files(check)
        for name, file_id in check_names.items():
            if check.files[file_id] != latest.files[latest_names[name]]:
                raise RuntimeError(f"Prepared filesystem did not preserve {name}.")
        os.replace(temp_path, output_path)
    finally:
        temp_path.unlink(missing_ok=True)

    manifest = {
        "codeBase": str(code_path),
        "codeArm9Sha256": expected_code_arm9,
        "latestDspreRom": str(latest_path),
        "latestDspreRomSha256": file_digest(latest_path),
        "preparedRom": str(output_path),
        "preparedRomSha256": file_digest(output_path),
        "dynamicHeaderCount": header_count,
        "scriptCount": script_count,
        "namedFileCount": len(code_names),
    }
    output_path.with_suffix(output_path.suffix + ".json").write_text(json.dumps(manifest, indent=2) + "\n")
    print(f"Prepared {output_path} from clean code and {len(code_names)} latest DSPRE files.")
    print(f"Preserved {header_count} dynamic headers and {script_count} scripts.")


if __name__ == "__main__":
    main()

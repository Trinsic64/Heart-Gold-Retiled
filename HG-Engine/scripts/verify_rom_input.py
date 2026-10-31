"""Reject an hg-engine output ROM used as the next build's input."""

import argparse
import hashlib
import json
import struct
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("rom", type=Path)
    args = parser.parse_args()

    with args.rom.open("rb") as source:
        header = source.read(0x200)
        if len(header) != 0x200 or header[12:16] != b"IPKE":
            raise SystemExit("Input must be a US HeartGold ROM (IPKE).")
        arm9_offset = struct.unpack_from("<I", header, 0x20)[0]
        arm9_size = struct.unpack_from("<I", header, 0x2C)[0]
        overlay_offset, overlay_size = struct.unpack_from("<II", header, 0x50)
        if overlay_size < 64:
            raise SystemExit("Input ROM has no overlay 1 entry.")
        source.seek(overlay_offset + 32)
        overlay_one = source.read(32)
        overlay_id, *_, overlay_flags = struct.unpack("<8I", overlay_one)
        source.seek(arm9_offset)
        arm9_sha256 = hashlib.sha256(source.read(arm9_size)).hexdigest()

    # A prepared DSPRE input carries an explicit manifest. It keeps the latest
    # DSPRE named files but uses reviewed clean HeartGold code and overlays.
    manifest_path = args.rom.with_suffix(args.rom.suffix + ".json")
    if manifest_path.is_file():
        manifest = json.loads(manifest_path.read_text())
        expected_code = "5eeaa2dcabfb66b4ff5d151687cff2c9214de9e272ba7afdae7a01d57cf319af"
        if arm9_sha256 != expected_code or manifest.get("codeArm9Sha256") != expected_code:
            raise SystemExit("Prepared input does not contain the reviewed pre-engine ARM9.")
        file_hash = hashlib.sha256()
        with args.rom.open("rb") as source:
            for chunk in iter(lambda: source.read(1024 * 1024), b""):
                file_hash.update(chunk)
        if file_hash.hexdigest() != manifest.get("preparedRomSha256"):
            raise SystemExit("Prepared input changed after its manifest was written.")
        if overlay_id != 1 or manifest.get("dynamicHeaderCount") != 627 or manifest.get("namedFileCount") != 384:
            raise SystemExit("Prepared input overlay or dynamic header count changed.")
        print("Verified prepared DSPRE input with pre-engine code.")
        return

    # hg-engine decompresses overlay 1 and expands ARM9 during a build.
    # Reusing that output as rom.nds retains old patches at their old addresses.
    if arm9_size >= 0xBC000 or overlay_id != 1 or not (overlay_flags >> 24) & 1:
        raise SystemExit(
            "Input ROM already has expanded code or altered overlays. "
            "Use scripts/prepare_dspre_rom.py to preserve DSPRE filesystem "
            "edits while restoring reviewed pre-engine code."
        )


if __name__ == "__main__":
    main()

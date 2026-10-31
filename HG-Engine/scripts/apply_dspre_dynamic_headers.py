"""Restore DSPRE's HGSS dynamic-header ARM9 hook after HG-Engine builds.

Copies only the known DSPRE hook sites from the latest DSPRE ROM. Every site
must still contain the matching pre-engine instruction or literal in the new
build, so an engine update that changes these routines fails without patching.
"""

from __future__ import annotations

import argparse
import struct
from pathlib import Path

import ndspy.narc
import ndspy.rom


REFERENCE_SITES = [
    (0x3B282, 0x3B28C), (0x3B296, 0x3B2A8), (0x3B2B2, 0x3B2BC),
    (0x3B2C6, 0x3B2D0), (0x3B2DA, 0x3B2E4), (0x3B2EE, 0x3B2F8),
    (0x3B302, 0x3B30C), (0x3B316, 0x3B320), (0x3B32A, 0x3B340),
    (0x3B34A, 0x3B354), (0x3B35E, 0x3B368), (0x3B372, 0x3B384),
    (0x3B38E, 0x3B3A4), (0x3B3AE, 0x3B3C4), (0x3B3CE, 0x3B3E0),
    (0x3B3EA, 0x3B3FC), (0x3B406, 0x3B418), (0x3B422, 0x3B434),
    (0x3B43E, 0x3B450), (0x3B45A, 0x3B46C), (0x3B476, 0x3B488),
    (0x3B492, 0x3B4A4), (0x3B4AE, 0x3B4C0), (0x3B4CA, 0x3B4D8),
    (0x3B4E2, 0x3B4F4), (0x3B4FE, 0x3B514),
]
PATCH_SITES = [(0x3B268, 20)]
for instruction, pointer in REFERENCE_SITES:
    PATCH_SITES.extend(((instruction, 4), (pointer, 4)))
PATCH_SITES.extend(((0x3B522, 2), (0x3B526, 2), (0x3B53C, 4)))

EXPECTED_HOOK = bytes.fromhex("00 B5 01 1C 32 20 00 22 CC F7 58 F9 03 1C DF F7 49 FC 00 BD")
EXPECTED_INSTRUCTION = bytes.fromhex("19 00 C0 46")


def arm9(path: Path) -> tuple[int, bytes]:
    with path.open("rb") as rom:
        header = rom.read(0x200)
        if len(header) != 0x200 or header[12:16] != b"IPKE":
            raise SystemExit(f"{path} is not a US HeartGold ROM")
        offset, size = struct.unpack_from("<II", header, 0x20)[0], struct.unpack_from("<I", header, 0x2C)[0]
        rom.seek(offset)
        data = rom.read(size)
    if len(data) != size or size <= 0x3B540:
        raise SystemExit(f"{path} has an unexpected ARM9 section")
    return offset, data


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--code-base", required=True, type=Path)
    parser.add_argument("--latest", required=True, type=Path)
    parser.add_argument("--built", required=True, type=Path)
    args = parser.parse_args()
    if len({args.code_base.resolve(), args.latest.resolve(), args.built.resolve()}) != 3:
        raise SystemExit("Code base, latest DSPRE ROM, and build output must be different files")

    _, base_code = arm9(args.code_base)
    _, latest_code = arm9(args.latest)
    built_offset, built_code = arm9(args.built)
    if latest_code[0x3B268 : 0x3B268 + 20] != EXPECTED_HOOK:
        raise SystemExit("Latest DSPRE ROM does not contain the expected dynamic-header hook")
    if any(latest_code[site : site + 4] != EXPECTED_INSTRUCTION for site, _ in REFERENCE_SITES):
        raise SystemExit("Latest DSPRE ROM has a different dynamic-header reference patch")

    latest = ndspy.rom.NintendoDSRom.fromFile(str(args.latest))
    built = ndspy.rom.NintendoDSRom.fromFile(str(args.built))
    latest_id = latest.filenames.idOf("a/0/5/0")
    built_id = built.filenames.idOf("a/0/5/0")
    if latest_id is None or built_id is None or latest.files[latest_id] != built.files[built_id]:
        raise SystemExit("New build did not preserve DSPRE's dynamic-header archive")
    if len(ndspy.narc.NARC(built.files[built_id]).files) != 627:
        raise SystemExit("New build does not contain 627 dynamic headers")

    updates = []
    already_patched = 0
    for offset, width in PATCH_SITES:
        before = base_code[offset : offset + width]
        current = built_code[offset : offset + width]
        target = latest_code[offset : offset + width]
        if target == before:
            raise SystemExit(f"No dynamic-header patch present at 0x{offset:X}")
        if current == target:
            already_patched += 1
            continue
        if current != before:
            raise SystemExit(f"HG-Engine changed ARM9 at 0x{offset:X}; inspect before porting DSPRE hook")
        updates.append((offset, target))

    if already_patched == len(PATCH_SITES):
        print(f"Verified {already_patched} existing DSPRE dynamic-header sites in {args.built}.")
        return
    if already_patched:
        raise SystemExit("Partially patched dynamic-header hook; inspect the build before continuing")

    with args.built.open("r+b") as output:
        for offset, payload in updates:
            output.seek(built_offset + offset)
            output.write(payload)
    _, verified = arm9(args.built)
    for offset, payload in updates:
        if verified[offset : offset + len(payload)] != payload:
            raise RuntimeError(f"Could not verify patch at 0x{offset:X}")
    print(f"Applied {len(updates)} verified DSPRE dynamic-header sites to {args.built}.")
    print("Preserved 627 dynamic headers from the latest DSPRE ROM.")


if __name__ == "__main__":
    main()

"""Check a DSPRE-compatible HG-Engine output against its source ROM."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path

import ndspy.narc
import ndspy.rom

from apply_dspre_dynamic_headers import PATCH_SITES
from apply_camera_table import TABLE_OFFSET, TABLE_SIZE


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--latest", type=Path, required=True)
    parser.add_argument("--built", type=Path, required=True)
    parser.add_argument("--sprite-btx", type=Path, required=True)
    parser.add_argument("--camera-table", type=Path, required=True)
    args = parser.parse_args()
    latest = ndspy.rom.NintendoDSRom.fromFile(str(args.latest))
    built = ndspy.rom.NintendoDSRom.fromFile(str(args.built))
    print(f"Built ROM: {args.built} ({args.built.stat().st_size:,} bytes)")
    print(f"ARM9 size: {len(built.arm9):,} bytes")
    for name in ("a/0/5/0", "a/0/1/2", "a/0/2/7"):
        source = latest.files[latest.filenames.idOf(name)]
        output = built.files[built.filenames.idOf(name)]
        if source != output:
            raise SystemExit(f"Changed DSPRE archive: {name}")
        print(f"Exact DSPRE archive {name}: {len(ndspy.narc.NARC(output).files)} members")
    sprite_narc = ndspy.narc.NARC(built.files[built.filenames.idOf("a/0/8/1")])
    sprite = sprite_narc.files[176]
    expected_sprite = args.sprite_btx.read_bytes()
    if sprite != expected_sprite:
        raise SystemExit("Overworld entry 176 does not match the compiled Deoxys sprite")
    print(f"Overworld entry 176 matches compiled BTX ({len(sprite):,} bytes; SHA256 {digest(sprite)})")
    for offset, width in PATCH_SITES:
        if built.arm9[offset : offset + width] != latest.arm9[offset : offset + width]:
            raise SystemExit(f"Dynamic-header ARM9 site 0x{offset:X} does not match DSPRE source")
    print(f"Exact DSPRE dynamic-header ARM9 sites: {len(PATCH_SITES)}")
    camera_table = args.camera_table.read_bytes()
    if len(camera_table) != TABLE_SIZE or built.files[1][TABLE_OFFSET : TABLE_OFFSET + TABLE_SIZE] != camera_table:
        raise SystemExit("Built ROM does not contain the customized camera table")
    print(f"Exact customized camera table: {len(camera_table) // 36} records; SHA256 {digest(camera_table)}")
    print("PASS")


if __name__ == "__main__":
    main()

"""Install the customized DSPRE camera table into HG-Engine overlay 1.

The camera editor stores 17 records of 36 bytes in overlay 1. Patch only that
table in the built ROM, after ndstool has assembled it. Reject an unfamiliar
unpatched table so a future engine layout change cannot be silently corrupted.
"""

from __future__ import annotations

import argparse
import hashlib
import struct
from pathlib import Path

import ndspy.rom


TABLE_OFFSET = 0x20B78
TABLE_SIZE = 17 * 36
ENGINE_TABLE_SHA256 = "4d5ca65ad15a04ff830ab35ac24bda5321594248b4b09b19102d2b523aa0e3b2"


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--table", required=True, type=Path)
    parser.add_argument("--built", required=True, type=Path)
    args = parser.parse_args()
    table = args.table.read_bytes()
    if len(table) != TABLE_SIZE:
        raise SystemExit(f"Camera table must contain 17 records ({TABLE_SIZE} bytes).")

    rom = ndspy.rom.NintendoDSRom.fromFile(str(args.built))
    if rom.idCode != b"IPKE":
        raise SystemExit("Build is not US HeartGold (IPKE).")
    overlay_one = next(
        (rom.arm9OverlayTable[i : i + 32]
         for i in range(0, len(rom.arm9OverlayTable), 32)
         if struct.unpack_from("<I", rom.arm9OverlayTable, i)[0] == 1),
        None,
    )
    if overlay_one is None:
        raise SystemExit("ARM9 overlay 1 is missing.")
    file_id = struct.unpack_from("<I", overlay_one, 24)[0]
    overlay = rom.files[file_id]
    if len(overlay) != 148064 or TABLE_OFFSET + TABLE_SIZE > len(overlay):
        raise SystemExit("ARM9 overlay 1 has an unexpected size or camera-table location.")
    current = overlay[TABLE_OFFSET : TABLE_OFFSET + TABLE_SIZE]
    if current == table:
        print(f"Verified customized camera table in {args.built} ({digest(table)}).")
        return
    if digest(current) != ENGINE_TABLE_SHA256:
        raise SystemExit("Existing camera table differs from the reviewed HG-Engine table; inspect before patching.")

    with args.built.open("r+b") as output:
        header = output.read(0x200)
        fat_offset, fat_size = struct.unpack_from("<II", header, 0x48)
        if (file_id + 1) * 8 > fat_size:
            raise SystemExit("Overlay file ID lies outside the file allocation table.")
        output.seek(fat_offset + file_id * 8)
        file_start, file_end = struct.unpack("<II", output.read(8))
        if file_end - file_start != len(overlay):
            raise SystemExit("Overlay size differs from its file allocation entry.")
        output.seek(file_start + TABLE_OFFSET)
        if output.read(TABLE_SIZE) != current:
            raise SystemExit("On-disk camera table differs from parsed overlay.")
        output.seek(file_start + TABLE_OFFSET)
        output.write(table)
        output.seek(file_start + TABLE_OFFSET)
        if output.read(TABLE_SIZE) != table:
            raise RuntimeError("Could not verify written camera table.")
    print(f"Applied {len(table) // 36} customized camera records to {args.built} ({digest(table)}).")


if __name__ == "__main__":
    main()

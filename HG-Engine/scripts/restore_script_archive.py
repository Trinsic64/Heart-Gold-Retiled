"""Start each script build from the source ROM, not the previous output."""

import argparse
from pathlib import Path

import ndspy.narc
import ndspy.rom


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("rom", type=Path)
    parser.add_argument("destination", type=Path)
    args = parser.parse_args()

    rom = ndspy.rom.NintendoDSRom.fromFile(str(args.rom))
    file_id = rom.filenames.idOf("a/0/1/2")
    if file_id is None:
        raise SystemExit("Input ROM has no a/0/1/2 script archive")
    archive = rom.files[file_id]
    member_count = len(ndspy.narc.NARC(archive).files)
    args.destination.write_bytes(archive)
    print(f"Restored {member_count} source script members from {args.rom}.")


if __name__ == "__main__":
    main()

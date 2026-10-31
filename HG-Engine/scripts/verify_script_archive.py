"""Reject script archives whose extracted filenames would shift script IDs."""

import argparse
from pathlib import Path

import ndspy.narc


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", type=Path)
    parser.add_argument("source_archive", type=Path)
    args = parser.parse_args()

    original = ndspy.narc.NARC.fromFile(str(args.source_archive))
    count = len(original.files)
    width = len(str(count - 1))
    expected = {f"{args.source_archive.name}_{index:0{width}d}" for index in range(count)}
    actual = {path.name for path in args.directory.iterdir() if path.is_file()}
    missing = sorted(expected - actual)
    unexpected = sorted(actual - expected)
    if missing or unexpected:
        raise SystemExit(
            f"Script archive must retain {count} numbered members; "
            f"missing={missing[:8]}, unexpected={unexpected[:8]}"
        )
    print(f"Verified {count} script members with unchanged archive indices.")


if __name__ == "__main__":
    main()

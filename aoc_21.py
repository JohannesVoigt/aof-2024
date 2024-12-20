"""Advent of Code - 21.12.2024"""

import os
import sys

DAY = 21
TEST = True


def build_path() -> str:
    """Build daily path."""
    return os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "files",
        f"2024_12_{DAY:02d}{'_test' if TEST else ''}.txt",
    )


def main() -> int:
    """Main function"""
    with open(build_path(), "r", encoding="utf-8") as file:
        pass

    # Part 1 ###################################################################
    res = 0
    print(f"Result part 1: {res}")

    # Part 2 ###################################################################
    res = 0
    print(f"Result part 2: {res}")

    return 0


if __name__ == "__main__":
    sys.exit(main())

"""Advent of Code - 9.12.2024"""

import os
import sys


DAY = 9
TEST = True


def main() -> int:
    """Main function"""
    current_dir = os.path.dirname(os.path.realpath(__file__))
    filename = f"2024_12_{DAY:02d}{"_test" if TEST else ""}.txt"
    filepath = os.path.join(current_dir, "files", filename)

    data = []
    with open(filepath, "r", encoding="utf-8") as file:
        for line in file:
            data.append(list(line)[:-1])

    # Part 1

    # Part 2

    return 0


if __name__ == "__main__":
    sys.exit(main())

"""Advent of Code - 01.12.2024"""

import os
import re
import sys

DAY = 1
TEST = False


def main() -> int:
    """Main function"""
    filepath = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "files",
        f"2024_12_{DAY:02d}{"_test" if TEST else ""}.txt",
    )

    with open(filepath, "r", encoding="utf-8") as file:

        # Part 1
        num_tuples = [list(map(int, re.findall(r"\d+", line))) for line in file]
        first, second = [list(t) for t in zip(*num_tuples)]
        first.sort()
        second.sort()

        tot_dist = sum(abs(s - f) for f, s in zip(first, second))
        print(f"Total distance: {tot_dist}")

        # Part 2
        tot_score = sum(f * second.count(f) for f in first)
        print(f"Total score: {tot_score}")

    return 0


if __name__ == "__main__":
    sys.exit(main())

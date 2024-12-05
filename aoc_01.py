"""Advent of Code - 01.12.2024"""

import os
import sys
import re

DAY = 1
TEST = True


def main() -> int:
    """Main function"""
    current_dir = os.path.dirname(os.path.realpath(__file__))
    filename = f"2024_12_{DAY:02d}{"_test" if TEST else ""}.txt"
    filepath = os.path.join(current_dir, "files", filename)

    with open(filepath, "r", encoding="utf-8") as file:

        # Part 1
        first, second = [], []
        for line in file:
            f, s = [int(num) for num in re.findall(r"\d+", line)]
            first.append(f)
            second.append(s)
        first.sort()
        second.sort()

        tot_dist = 0
        for f, s in zip(first, second):
            tot_dist += abs(s - f)
        print(f"Total distance: {tot_dist}")

        # Part 2
        tot_score = sum(f * second.count(f) for f in first)
        print(f"Total score: {tot_score}")

    return 0


if __name__ == "__main__":
    sys.exit(main())

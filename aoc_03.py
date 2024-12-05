"""Advent of Code - 03.12.2024"""

import os
import re
import sys

DAY = 3
TEST = False


def main() -> int:
    """Main function"""
    filepath = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "files",
        f"2024_12_{DAY:02d}{"_test" if TEST else ""}.txt",
    )

    with open(filepath, "r", encoding="utf-8") as file:
        res_p1 = 0
        res_p2 = 0
        do = True
        for line in file:
            # Part 1
            multis_p1 = re.findall(r"mul\(\d+,\d+\)", line)
            for mult in multis_p1:
                numbers = [int(i) for i in re.findall(r"\d+", mult)]
                res_p1 += numbers[0] * numbers[1]

            # Part 2
            multis_p2 = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", line)
            for mult in multis_p2:
                numbers = [int(i) for i in re.findall(r"\d+", mult)]
                if len(numbers) == 0:
                    do = bool(mult == "do()")
                else:
                    if do:
                        res_p2 += numbers[0] * numbers[1]

    print(f"Sum of multiplications part 1: {res_p1}")
    print(f"Sum of multiplications part 2: {res_p2}")

    return 0


if __name__ == "__main__":
    sys.exit(main())

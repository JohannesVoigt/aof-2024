"""Advent of Code - 03.12.2024"""

import os
import sys
import re

DAY = 3
TEST = True


def main() -> int:
    """Main function"""
    current_dir = os.path.dirname(os.path.realpath(__file__))
    filename = f"2024_12_{DAY:02d}{"_test" if TEST else ""}.txt"
    filepath = os.path.join(current_dir, "files", filename)

    # Part 1/2
    for part in range(1, 3):
        with open(filepath, "r", encoding="utf-8") as file:
            res = 0
            do = True
            for line in file:
                if part == 1:
                    multis = re.findall(r"mul\(\d+,\d+\)", line)
                else:
                    multis = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", line)
                for mult in multis:
                    numbers = [int(n) for n in re.findall(r"\d+", mult)]
                    if len(numbers) == 0:
                        do = bool(mult == "do()")
                    else:
                        if do:
                            res += numbers[0] * numbers[1]
        print(f"Sum of multiplications part {part}: {res}")

    return 0


if __name__ == "__main__":
    sys.exit(main())

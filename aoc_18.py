"""Advent of Code - 18.12.2024"""

import re
import os
import sys

DAY = 18
TEST = False


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
        xlist, ylist = [], []
        for line in file.readlines():
            print(re.findall(r"\d+", line))
            nums = list(map(int, re.findall(r"\d+", line)))
            xlist.append(nums[0])
            ylist.append(nums[1])

    if TEST:
        gridsize = (7, 7)
    else:
        gridsize = (71, 71)

    # Part 1 ###################################################################
    res = 0
    npos = 1024
    grid = [["." for __ in range(gridsize[1])] for _ in range(gridsize[0])]
    for x, y in zip(xlist[:npos], ylist[:npos]):
        grid[y][x] = "#"
    for line in grid:
        print("".join(line))
    print(f"Result part 1: {res}")

    # Part 2 ###################################################################
    res = 0
    print(f"Result part 2: {res}")

    return 0


if __name__ == "__main__":
    sys.exit(main())

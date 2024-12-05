"""Advent of Code - 02.12.2024"""

import os
import sys
import re

DAY = 2
TEST = True


def get_dists(nums: list):
    """Get distances"""
    dists = []
    for num1, num2 in zip(nums, nums[1:]):
        dists.append(num2 - num1)
    return dists


def main() -> int:
    """Main function"""
    current_dir = os.path.dirname(os.path.realpath(__file__))
    filename = f"2024_12_{DAY:02d}{"_test" if TEST else ""}.txt"
    filepath = os.path.join(current_dir, "files", filename)

    # Part 1 & 2
    with open(filepath, "r", encoding="utf-8") as file:
        num_reports_p1 = 0
        num_reports_p2 = 0
        for line in file:
            nums = [int(num) for num in re.findall(r"\d+", line)]

            dists = get_dists(nums)

            if set(dists).issubset({-3, -2, -1}) or set(dists).issubset({3, 2, 1}):
                num_reports_p1 += 1
            else:
                for i, _ in enumerate(nums):
                    nums_copy = nums.copy()
                    nums_copy.pop(i)
                    dists = get_dists(nums_copy)
                    if set(dists).issubset({-3, -2, -1}) or set(dists).issubset(
                        {3, 2, 1}
                    ):
                        num_reports_p2 += 1
                        break

    print(f"Num of save reports part 1: {num_reports_p1}")
    print(f"Num of save reports part 2: {num_reports_p1 + num_reports_p2}")

    return 0


if __name__ == "__main__":
    sys.exit(main())

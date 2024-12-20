"""Advent of Code - 2.12.2024"""

import os
import re
import sys

DAY = 2
TEST = False


def diff(nums: list[int | float]) -> list[int | float]:
    """Get differences between numbers in a list."""
    return [num2 - num1 for num1, num2 in zip(nums, nums[1:])]


def main() -> int:
    """Main function"""
    filepath = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "files",
        f"2024_12_{DAY:02d}{'_test' if TEST else ''}.txt",
    )

    # Part 1 & 2
    with open(filepath, "r", encoding="utf-8") as file:
        num_reports_p1 = 0
        num_reports_p2 = 0
        for line in file:
            nums = [int(num) for num in re.findall(r"\d+", line)]

            diffs = diff(nums)

            if set(diffs).issubset({-3, -2, -1}) or set(diffs).issubset({3, 2, 1}):
                num_reports_p1 += 1
            else:
                for i, _ in enumerate(nums):
                    # Remove one number and try again
                    nums_copy = nums.copy()
                    nums_copy.pop(i)
                    diffs = diff(nums_copy)
                    if set(diffs).issubset({-3, -2, -1}) or set(diffs).issubset(
                        {3, 2, 1}
                    ):
                        num_reports_p2 += 1
                        break

    print(f"Num of save reports part 1: {num_reports_p1}")
    print(f"Num of save reports part 2: {num_reports_p1 + num_reports_p2}")

    return 0


if __name__ == "__main__":
    sys.exit(main())

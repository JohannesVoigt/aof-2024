"""Advent of Code - 11.12.2024"""

from collections import defaultdict
import os
import sys
import math

DAY = 11
TEST = False


def build_path() -> str:
    """Build daily path."""
    return os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "files",
        f"2024_12_{DAY:02d}{'_test' if TEST else ''}.txt",
    )


def num_digits(num: int) -> int:
    """Return number of digits"""
    return int(1 + math.log10(num))


def is_even(num: int) -> bool:
    """Check if number of digits of number is even"""
    return not num_digits(num) % 2


def split_num(num: int) -> tuple[int, int]:
    """Split number in two numbers"""
    divisor = 10 ** (num_digits(num) // 2)
    n1 = num // divisor
    n2 = num % divisor
    return n1, n2


def idea_1(stones: list[int], max_blink: int):
    """Idea 1: works, but not for large numbers ..."""
    blink = 0
    while blink < max_blink:
        new_stones = []
        for stone in stones:
            if stone == 0:
                new_stones.append(1)
            elif is_even(stone):
                new_stones += split_num(stone)
            else:
                new_stones.append(2024 * stone)
        stones = new_stones
        blink += 1
    return len(stones)


def idea_2(stones: list[int], max_blink: int):
    """Idea 2: same problem as is idea 1..."""
    return sum(find_numbers(stone, 0, max_blink) for stone in stones)


def find_numbers(stone: int, blink: int, max_blink: int) -> int:
    """Idea 2: find numbers recursively."""
    if blink == max_blink:
        return 1
    cnt = 0
    while blink < max_blink:
        if stone == 0:
            stone += 1
        elif is_even(stone):
            for new_stone in split_num(stone):
                cnt += find_numbers(new_stone, blink + 1, max_blink)
            return cnt
        else:
            stone *= 2024
        blink += 1
    cnt += 1
    return cnt


def idea_3(stones: list[int], max_blink: int):
    """Idea 3: this works!!!"""
    stone_dict = defaultdict(int)
    for stone in stones:
        stone_dict[stone] += 1

    blink = 0
    while blink < max_blink:
        new_stone_dict = defaultdict(int)
        for stone, num_stones in stone_dict.items():
            if stone == 0:
                new_stone_dict[1] += num_stones
            elif is_even(stone):
                new_stone1, new_stone2 = split_num(stone)
                new_stone_dict[new_stone1] += num_stones
                new_stone_dict[new_stone2] += num_stones
            else:
                new_stone_dict[2024 * stone] += num_stones
        stone_dict = new_stone_dict
        blink += 1
    return sum(stone_dict.values())


def main() -> int:
    """Main function"""
    with open(build_path(), "r", encoding="utf-8") as file:
        stones = list(map(int, file.read().split()))

    # Part 1 / 2 ###############################################################
    max_blink = 75

    # cnt = idea_1(stones, max_blink)
    # print(f"Idea 1 - Number of stones: {cnt}")

    # cnt = idea_2(stones, max_blink)
    # print(f"Idea 2 - Number of stones: {cnt}")

    cnt = idea_3(stones, max_blink)
    print(f"Idea 3 - Number of stones: {cnt}")

    return 0


if __name__ == "__main__":
    sys.exit(main())

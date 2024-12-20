"""Advent of Code - 14.12.2024"""

import re
import os
import sys

DAY = 14
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
        positions = []
        velocities = []
        for line in file:
            nums = list(map(int, re.findall(r"\d+|\-\d+", line)))
            positions.append(nums[:2])
            velocities.append(nums[2:])

    # Part 1 ###################################################################
    if TEST:
        dims = (11, 7)
    else:
        dims = (101, 103)
    t_sec = 1_000_000

    end_positions = []
    for p_xy, v_xy in zip(positions, velocities):
        end_positions.append([(p + t_sec * v) % d for p, v, d in zip(p_xy, v_xy, dims)])

    q_counter = 4 * [0]
    for x, y in end_positions:
        if x < dims[0] // 2:  # left
            if y < dims[1] // 2:
                q_counter[0] += 1
            elif y > dims[1] // 2:
                q_counter[1] += 1
        elif x > dims[0] // 2:  # right
            if y < dims[1] // 2:
                q_counter[2] += 1
            elif y > dims[1] // 2:
                q_counter[3] += 1

    prod = 1
    for num in q_counter:
        prod *= num

    print(f"Result part 1: {prod}")

    # Part 2 ###################################################################
    width = os.get_terminal_size().columns
    if width < dims[0] * 2:
        print(f"Too small: {width}<{dims[0]*2} ")
        return 1
    for i in range(t_sec):
        os.system("cls")
        mat = [["."] * dims[0] for _ in range(dims[1])]
        end_positions = []
        # c = i
        c = 103 * i + 65
        # c = 101 * i + 11 # 7687
        for p_xy, v_xy in zip(positions, velocities):
            new_pos = [(p + c * v) % d for p, v, d in zip(p_xy, v_xy, dims)]
            if mat[new_pos[1]][new_pos[0]] == ".":
                mat[new_pos[1]][new_pos[0]] = "1"
            else:
                mat[new_pos[1]][new_pos[0]] = str(int(mat[new_pos[1]][new_pos[0]]) + 1)
        print(f" Seconds: {c} ________________________________________")
        for row in mat:
            print(" ".join(row))
        input()

    return 0


if __name__ == "__main__":
    sys.exit(main())

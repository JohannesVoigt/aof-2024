"""Advent of Code - 04.12.2024"""

import os
import sys
import re
from typing import Any


def transpose(list_: list[list[Any]]) -> list[list[Any]]:
    """Transpose list of lists (matrix)."""
    return list(map(list, zip(*list_)))


def rotate(list_: list[list[Any]], direction: str = "right") -> list[list[Any]]:
    """Rotate list of lists to the left/right."""
    if direction == "left":
        return reversed(transpose(list_))
    if direction == "right":
        return transpose(reversed(list_))
    raise ValueError("'direction' must be 'left' or 'right'")


def shift_matrix(mat: list[list[Any]], shift: str, token: str | int | float = "*"):
    """
    Sshift the matrix by 1 in each row to the left/right.
    """
    mat_ = []
    if shift == "left":
        for i, row in enumerate(mat):
            mat_.append((len(mat) - i - 1) * [token] + row + i * [token])
        return mat_
    if shift == "right":
        for i, row in enumerate(mat):
            mat_.append(i * [token] + row + (len(mat) - i - 1) * [token])
        return mat_
    raise ValueError("'shift' must be 'left' or 'right'")


def add_matrix_frame(
    mat: list[list[Any]],
    framewidth: int,
    token: str | int | float = "*",
):
    """
    Add a frame around a matrix, i.e., a list of lists with the thickness \
        'framewidth' and filled with 'frame_token'.
    """
    hframe = [len(mat[0]) * [token] for _ in range(framewidth)]
    vframe = framewidth * [token]
    mat = hframe + mat + hframe
    mat_ = []
    for row in mat:
        mat_.append(vframe + row + vframe)
    return mat_


DAY = 4
TEST = True


def main() -> int:
    """Main function"""
    current_dir = os.path.dirname(os.path.realpath(__file__))
    filename = f"2024_12_{DAY:02d}{"_test" if TEST else ""}.txt"
    filepath = os.path.join(current_dir, "files", filename)

    # Part 1 ###################################################################
    data = []
    with open(filepath, "r", encoding="utf-8") as file:
        for line in file:
            data.append(list(line)[:-1])

    xmas_str = "XMAS"

    search_matrices = [
        data,  # horizontal
        transpose(data),  # vertical
        transpose(shift_matrix(data, "left")),  # upper left -> lower right
        transpose(shift_matrix(data, "right")),  # upper right -> lower left
    ]

    xmas_cnt = 0
    for mat in search_matrices:
        for row in mat:
            xmas_cnt += len(re.findall(xmas_str, "".join(row)))
            xmas_cnt += len(re.findall(xmas_str, "".join(reversed(row))))

    print(f"Num of XMAS part 1: {xmas_cnt}")

    # Part 2 ###################################################################
    # Add frame
    framed_mat = add_matrix_frame(data, 1)

    # Find all "A"
    a_xy = []
    for y, row in enumerate(framed_mat):
        for x, char in enumerate(row):
            if char == "A":
                a_xy.append([x, y])

    # Find X-MAS patterns
    pattern = [["S", "S"], ["M", "M"]]
    x_max_cnt = 0
    for x, y in a_xy:
        rows = framed_mat[y - 1 : y + 2]
        for _ in range(4):
            if (
                rows[0][x - 1] == pattern[0][0]
                and rows[0][x + 1] == pattern[0][1]
                and rows[2][x - 1] == pattern[1][0]
                and rows[2][x + 1] == pattern[1][1]
            ):
                x_max_cnt += 1
                break
            pattern = rotate(pattern, "right")

    print(f"Num of XMAS part 2: {x_max_cnt}")

    return 0


if __name__ == "__main__":
    sys.exit(main())

"""Advent of Code - 4.12.2024"""

import os
import re
import sys
from typing import Any


def transpose(list_: list[list[Any]]) -> list[list[Any]]:
    """Transpose list of lists (matrix)."""
    return [list(tuple_) for tuple_ in zip(*list_)]


def rotate(list_: list[list[Any]], direction: str) -> list[list[Any]]:
    """Rotate list of lists to the left/right."""
    if direction == "left":
        return list(reversed(transpose(list_)))
    if direction == "right":
        return transpose(list(reversed(list_)))
    raise ValueError("'direction' must be 'left' or 'right'")


def shift_matrix(
    mat: list[list[Any]], shift: str, token: str | int | float = "*"
) -> list[list[Any]]:
    """Shift the matrix by 1 in each row to the left/right."""
    if not shift in ("left", "right"):
        raise ValueError("'shift' must be 'left' or 'right'")

    if shift == "right":
        mat = list(reversed(mat))

    mat_ = []
    for i, row in enumerate(mat):  # Shift columns and add tokens
        mat_.append((len(mat) - i - 1) * [token] + row + i * [token])

    if shift == "right":
        return list(reversed(mat_))
    return mat_


def add_matrix_frame(
    mat: list[list[Any]], framewidth: int, token: str | int | float = "*"
) -> list[list[Any]]:
    """
    Add a frame around a matrix, i.e., a list of lists with the thickness \
        'framewidth' and filled with 'frame_token'.
    """
    hframe = [len(mat[0]) * [token] for _ in range(framewidth)]
    vframe = framewidth * [token]
    mat = hframe + mat + hframe
    return [vframe + row + vframe for row in mat]


DAY = 4
TEST = True


def main() -> int:
    """Main function"""
    filepath = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "files",
        f"2024_12_{DAY:02d}{'_test' if TEST else ''}.txt",
    )

    # Part 1 ###################################################################
    with open(filepath, "r", encoding="utf-8") as file:
        data = [list(line)[:-1] for line in file]

    search_matrices = [
        data,  # horizontal
        transpose(data),  # vertical
        transpose(shift_matrix(data, "left")),  # upper left -> lower right
        transpose(shift_matrix(data, "right")),  # upper right -> lower left
    ]

    num_xmas_p1 = 0
    for mat in search_matrices:
        for row in mat:
            num_xmas_p1 += len(re.findall("XMAS", "".join(row)))
            num_xmas_p1 += len(re.findall("XMAS", "".join(reversed(row))))

    print(f"Num of XMAS part 1: {num_xmas_p1}")

    # Part 2 ###################################################################
    # Add frame
    framed_mat = add_matrix_frame(data, 1)

    # Find all "A"
    a_xy = []
    for y, row in enumerate(framed_mat):
        for x, char in enumerate(row):
            if char == "A":
                a_xy.append([x, y])

    # Inspect each "A" and find X-MAS patterns
    num_xmas_p2 = 0
    for x, y in a_xy:
        rows = framed_mat[y - 1 : y + 2]
        pattern = [
            ["S", "S"],
            ["M", "M"],
        ]
        for _ in range(4):
            if (
                rows[0][x - 1] == pattern[0][0]
                and rows[0][x + 1] == pattern[0][1]
                and rows[2][x - 1] == pattern[1][0]
                and rows[2][x + 1] == pattern[1][1]
            ):
                num_xmas_p2 += 1
                break
            pattern = rotate(pattern, "right")

    print(f"Num of XMAS part 2: {num_xmas_p2}")

    return 0


if __name__ == "__main__":
    sys.exit(main())

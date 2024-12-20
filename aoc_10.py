"""Advent of Code - XX.12.2024"""

import os
import sys
from typing import Any


DAY = 10
TEST = False


def build_path() -> str:
    """Build daily path."""
    return os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "files",
        f"2024_12_{DAY:02d}{'_test' if TEST else ''}.txt",
    )


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


def find_trail(topo_map: list[list[int]], yp: int, xp: int, h: int):
    """Find paths recursively"""
    if h >= 9:
        return [(yp, xp)]

    # Get positions of direct neighbors
    neighbors = [(yp - 1, xp), (yp + 1, xp), (yp, xp - 1), (yp, xp + 1)]

    end_pos = []
    for i, (yn, xn) in enumerate(neighbors):
        if (topo_map[yn][xn] - h) == 1:  # Correct delta h -> next recursion
            end_pos += find_trail(topo_map, *neighbors[i], h + 1)

    return end_pos


def main() -> int:
    """Main function"""
    # Read topographic map
    with open(build_path(), "r", encoding="utf-8") as file:
        topo_map = [list(map(int, list(x))) for x in file.read().split()]

    # Add frame to avoid boundary conditions
    topo_map = add_matrix_frame(topo_map, 1, -10)

    # Part 1 & 2 ###############################################################
    start_positions = [  # Get start positions (height=0)
        (y, x)
        for y, row in enumerate(topo_map)
        for x, num in enumerate(row)
        if num == 0
    ]

    # Find trailheads for each start position
    num_trailheads_p1 = 0
    num_trailheads_p2 = 0
    for start in start_positions:
        trailsheads = find_trail(topo_map, *start, 0)
        num_trailheads_p1 += len(set(trailsheads))
        num_trailheads_p2 += len(trailsheads)

    print(f"Num of trailheads part 1: {num_trailheads_p1}")
    print(f"Num of trailheads part 2: {num_trailheads_p2}")

    return 0


if __name__ == "__main__":
    sys.exit(main())

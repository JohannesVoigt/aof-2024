"""Advent of Code - 12.12.2024"""

from copy import deepcopy
from typing import Any
import os
import sys

DAY = 12
TEST = True


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


def get_neighbors(
    y: int, x: int
) -> tuple[tuple[int, int], tuple[int, int], tuple[int, int], tuple[int, int]]:
    """Find direct 4 neighbors."""
    return (y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)


def find_region(
    grid: list[list[int]], y: int, x: int, plant: str
) -> list[tuple[int, int]]:
    """Find regions"""
    grid[y][x] = "."
    region = [(y, x)]
    for yn, xn in get_neighbors(y, x):
        if grid[yn][xn] == plant:
            grid[yn][xn] = "."
            region += find_region(grid, yn, xn, plant)
    return region


def main() -> int:
    """Main function"""
    with open(build_path(), "r", encoding="utf-8") as file:
        grid = [list(map(str, x)) for x in file.read().split()]

    # Part 1 ###################################################################
    unique_plants = set(plant for line in grid for plant in line)
    print(f"Plants: {unique_plants}")

    grid = add_matrix_frame(grid, 1, "*")

    # Find regions:
    regions = []
    tmp_grid = deepcopy(grid)
    for y, row in enumerate(tmp_grid):
        for x, plant in enumerate(row):
            if plant in unique_plants:
                regions.append(find_region(tmp_grid, y, x, plant))

    # Derive region perimeter (including internal fences)
    perimeters = []
    for region in regions:
        perimeter = 0
        for y, x in region:
            for yn, xn in get_neighbors(y, x):
                perimeter += grid[y][x] != grid[yn][xn]
        perimeters.append(perimeter)

    total_price = sum((len(r) * p for r, p in zip(regions, perimeters)))
    print(f"Total price part 1: {total_price}")

    # Part 2 ###################################################################

    num_fences = [0] * len(regions)
    for y, row in enumerate(grid[1:-1], 1):
        for x, plant in enumerate(row[1:-1], 1):
            for i, region in enumerate(regions):
                if (y, x) in region:
                    # Horizontal fences
                    if not (y - 1, x) in region:  # check above
                        if not (y, x + 1) in region:
                            num_fences[i] += 1
                        elif (y - 1, x + 1) in region:  # fence crosses
                            num_fences[i] += 1
                    if not (y + 1, x) in region:  # check below
                        if not (y, x + 1) in region:
                            num_fences[i] += 1
                        elif (y + 1, x + 1) in region:  # fence crosses
                            num_fences[i] += 1

                    # Vertical fences
                    if not (y, x + 1) in region:  # check right
                        if not (y + 1, x) in region:
                            num_fences[i] += 1
                        elif (y + 1, x + 1) in region:  # fence crosses
                            num_fences[i] += 1
                    if not (y, x - 1) in region:  # check left
                        if not (y + 1, x) in region:
                            num_fences[i] += 1
                        elif (y + 1, x - 1) in region:  # fence crosses
                            num_fences[i] += 1

                    break  # Is in region -> continue with next plant

    tot_price = sum(len(r) * num for r, num in zip(regions, num_fences))
    print(f"Total price part 2: {tot_price}")

    return 0


if __name__ == "__main__":
    sys.exit(main())

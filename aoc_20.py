"""Advent of Code - 20.12.2024"""

from collections import defaultdict
import os
import sys
from typing import Any

DAY = 20
TEST = False


def build_path() -> str:
    """Build daily path."""
    return os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "files",
        f"2024_12_{DAY:02d}{'_test' if TEST else ''}.txt",
    )


def find_position(grid: list[list[str]], symbol: str) -> tuple[int, int]:
    """Find unique position of 'symbol' in 'grid'."""
    return [
        (y, x)
        for y, row in enumerate(grid)
        for x, tile in enumerate(row)
        if tile == symbol
    ][0]


def add_matrix_frame(
    grid: list[list[Any]], framewidth: int, token: str | int | float = "*"
) -> list[list[Any]]:
    """
    Add a frame around a matrix, i.e., a list of lists with the thickness \
        'framewidth' and filled with 'frame_token'.
    """
    hframe = [len(grid[0]) * [token] for _ in range(framewidth)]
    vframe = framewidth * [token]
    grid = hframe + grid + hframe
    return [vframe + row + vframe for row in grid]


def get_neighbors(
    y: int, x: int, distance: int = 1
) -> tuple[tuple[int, int], tuple[int, int], tuple[int, int], tuple[int, int]]:
    """Find direct 4 neighbors."""
    return (y - distance, x), (y + distance, x), (y, x - distance), (y, x + distance)


def get_neighborhood(y: int, x: int, distance: int = 1) -> tuple[tuple[int, int], ...]:
    """Find all neighbors width the distance given."""
    neighbors = []
    for dy in range(distance + 1):
        dx = distance - dy
        neighbors += [
            (y - dy, x + dx),
            (y + dy, x - dx),
            (y - dy, x - dx),
            (y + dy, x + dx),
        ]
    return tuple(set(neighbors))


def fill_distances(grid: list[list[str]], start: tuple[int, int]) -> None:
    """Fill the grid with the distances to the start position (inplace)."""
    step = 0
    positions = [start]
    grid[start[0]][start[1]] = 0
    while len(positions) > 0:
        neighbors = set()
        for pos in positions:
            neighbors.update(get_neighbors(*pos))

        step += 1
        positions = []
        for n in neighbors:
            if grid[n[0]][n[1]] == ".":
                grid[n[0]][n[1]] = step
                positions.append(n)

    return grid


def get_value(grid: list[list[str]], pos: tuple[int, int]) -> str | int:
    """Return grid value at position."""
    return grid[pos[0]][pos[1]]


def set_value(grid: list[list[str]], pos: tuple[int, int], val: str | int) -> None:
    """Return grid value at position (inplace)."""
    grid[pos[0]][pos[1]] = val
    return grid


def main() -> int:
    """Main function"""
    with open(build_path(), "r", encoding="utf-8") as file:
        grid = [list(line.replace("\n", "")) for line in file]
    # Add frame to avoid boundary checks
    grid_p1 = add_matrix_frame(grid, 1, "#")
    grid_p2 = add_matrix_frame(grid, 20, "#")

    # Part 1 ###################################################################
    # Find start and end position
    start = find_position(grid_p1, "S")
    end = find_position(grid_p1, "E")

    # Fill all points in grid with distance to start position
    set_value(grid_p1, end, ".")
    fill_distances(grid_p1, start)

    # Minimum path length to destination
    min_path_len = get_value(grid_p1, end)

    path_positions = [
        (y, x)
        for y, row in enumerate(grid_p1)
        for x, val in enumerate(row)
        if isinstance(val, int) and val < min_path_len
    ]

    cheats = defaultdict(int)
    for pp in path_positions:
        pval = get_value(grid_p1, pp)
        neighbors = get_neighborhood(*pp, distance=2)
        for np in neighbors:
            nval = get_value(grid_p1, np)
            if isinstance(nval, int) and nval > pval + 2:
                picoseconds_saved = nval - pval - 2
                cheats[picoseconds_saved] += 1

    # for cheat, num in sorted(cheats.items()):
    #     print(f"There are {num:2d} cheats that save {cheat} picoseconds.")

    min_picoseconds_saved = 20 if TEST else 100
    num_cheats_part1 = 0
    for cheat, num in cheats.items():
        if cheat >= min_picoseconds_saved:
            num_cheats_part1 += num
    print(f"number of cheats part 1: {num_cheats_part1}")

    # Part 2 ###################################################################
    start = find_position(grid_p2, "S")
    end = find_position(grid_p2, "E")

    set_value(grid_p2, end, ".")
    fill_distances(grid_p2, start)

    min_path_len = get_value(grid_p2, end)

    path_positions = [
        (y, x)
        for y, row in enumerate(grid_p2)
        for x, val in enumerate(row)
        if isinstance(val, int) and val < min_path_len
    ]

    cheats = defaultdict(int)
    for d in range(2, 21):
        for pp in path_positions:
            pval = get_value(grid_p2, pp)
            neighbors = get_neighborhood(*pp, distance=d)
            for np in neighbors:
                nval = get_value(grid_p2, np)
                if isinstance(nval, int) and (nval > pval + d):
                    picoseconds_saved = nval - pval - d
                    cheats[picoseconds_saved] += 1

    min_picoseconds_saved = 50 if TEST else 100

    # for cheat, num in sorted(cheats.items()):
    #     if cheat >= min_picoseconds_saved:
    #         print(f"There are {num:3d} cheats that save {cheat} picoseconds.")
    num_cheats_part2 = 0
    for cheat, num in cheats.items():
        if cheat >= min_picoseconds_saved:
            num_cheats_part2 += num
    print(f"number of cheats part 2: {num_cheats_part2}")

    return 0


if __name__ == "__main__":
    sys.exit(main())

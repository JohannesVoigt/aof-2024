"""Advent of Code - 18.12.2024"""

import re
import os
import sys
from typing import Any

DAY = 18
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


def get_neighbors(
    y: int, x: int
) -> tuple[tuple[int, int], tuple[int, int], tuple[int, int], tuple[int, int]]:
    """Find direct 4 neighbors."""
    return (y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)


def create_grid(
    grid_shape: tuple[int, int],
    byte_positions: list[tuple[int, int]] = None,
    framewidth: int = None,
    frame_symbol: str = "#",
) -> list[list[str]]:
    """Create grid (corrupted memory space) with a frame (optional)."""
    grid = [["." for __ in range(grid_shape[1])] for _ in range(grid_shape[0])]

    if byte_positions is not None:
        for x, y in byte_positions:
            grid[y][x] = "#"

    if framewidth is not None:
        grid = add_matrix_frame(grid, framewidth, frame_symbol)

    return grid


def shortest_path_len(
    grid: list[list[str]], start: tuple[int, int], end: tuple[int, int]
) -> int:
    """Return the shortest path length if there is any path."""
    step = 0
    positions = [start]
    grid[start[0]][start[1]] = "0"
    while len(positions) > 0:
        neighbors = set()
        for pos in positions:
            neighbors.update(get_neighbors(*pos))

        step += 1
        positions = []
        for n in neighbors:
            if grid[n[0]][n[1]] == ".":
                grid[n[0]][n[1]] = f"{step}"
                positions.append(n)

    path_len = grid[end[0]][end[1]]
    if path_len == ".":
        return None
    return int(path_len)


def main() -> int:
    """Main function"""
    with open(build_path(), "r", encoding="utf-8") as file:
        byte_positions = [
            tuple(map(int, re.findall(r"\d+", line))) for line in file.readlines()
        ]

    grid_shape = (7, 7) if TEST else (71, 71)  # (y,x)

    # Part 1 ###################################################################
    n_bytes = 12 if TEST else 1024

    # Create grid + frame
    grid = create_grid(grid_shape, byte_positions[:n_bytes], framewidth=1)

    # Find path length if there is a path
    path_len = shortest_path_len(grid, (1, 1), grid_shape)  # Note +1 because of frame

    print(f"Shortest path part 1: {path_len}")

    # Part 2 ###################################################################

    # Binary search
    nmin, nmax = 0, len(byte_positions)
    while nmin != nmax - 1:
        n_bytes = nmin + (nmax - nmin) // 2

        # Find path length if there is a path
        grid = create_grid(grid_shape, byte_positions[:n_bytes], framewidth=1)
        path_len = shortest_path_len(grid, (1, 1), grid_shape)

        if path_len is None:  # No path found
            nmax = n_bytes
        else:
            nmin = n_bytes

    print(f"Coordinates of byte part 2: (x,y)={byte_positions[nmax-1]}")

    return 0


if __name__ == "__main__":
    sys.exit(main())

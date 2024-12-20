"""Advent of Code - 15.12.2024"""

import os
import sys

from time import sleep


Grid = list[list[str]]

DAY = 15
TEST = False


def build_path() -> str:
    """Build daily path."""
    return os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "files",
        f"2024_12_{DAY:02d}{'_test' if TEST else ''}.txt",
    )


def load_grid_and_track(filepath: str, part: int):
    """Load puzzle input."""
    with open(filepath, "r", encoding="utf-8") as file:
        is_grid = True
        grid = []
        track = []
        for line in file:
            if len(line) == 1:
                is_grid = False
                continue
            if is_grid:
                if part == 1:
                    grid.append(list(line.replace("\n", "")))
                elif part == 2:
                    grid.append(
                        list(
                            line.replace("\n", "")
                            .replace("#", "##")
                            .replace("O", "[]")
                            .replace(".", "..")
                            .replace("@", "@.")
                        )
                    )
            else:
                track.extend(line.replace("\n", ""))
    return grid, track


def render(grid: Grid, tstep: float = 0.1) -> None:
    """Render map"""
    if TEST:
        os.system("cls")
        for row in grid:
            print("".join(row))
        sleep(tstep)


def find_position(grid: list[list[str]], token: str) -> tuple[int, int]:
    """Find unique position of 'token' in 'grid'."""
    return [
        (y, x)
        for y, row in enumerate(grid)
        for x, tile in enumerate(row)
        if tile == token
    ][0]


def check_pos_part1(pos: tuple[int, int], direction: tuple[int, int], grid: Grid):
    """Check positions"""
    new_pos = [x + delta for x, delta in zip(pos, direction)]
    if grid[new_pos[0]][new_pos[1]] == "#":
        return False, pos, grid
    if grid[new_pos[0]][new_pos[1]] == ".":
        grid[new_pos[0]][new_pos[1]] = grid[pos[0]][pos[1]]
        return True, new_pos, grid
    is_true, _, grid = check_pos_part1(new_pos, direction, grid)
    if is_true:
        grid[new_pos[0]][new_pos[1]] = grid[pos[0]][pos[1]]
        return True, new_pos, grid
    return False, pos, grid


def check_pos_part2(
    pos: tuple[int, int], direction: tuple[int, int], grid: Grid, update: bool = True
):
    """Check positions"""
    new_pos = [x + delta for x, delta in zip(pos, direction)]
    if grid[new_pos[0]][new_pos[1]] == "#":
        return False, pos, grid
    if grid[new_pos[0]][new_pos[1]] == ".":
        return True, new_pos, grid
    if grid[new_pos[0]][new_pos[1]] == "[":
        new_pos = [new_pos, [new_pos[0], new_pos[1] + 1]]
    else:
        new_pos = [new_pos, [new_pos[0], new_pos[1] - 1]]
    is_true = True
    for np in new_pos:
        is_true1, _, grid = check_pos_part2(np, direction, grid, update)
        is_true = is_true and is_true1
    if is_true:
        if isinstance(pos[0], int) and update:
            # Update boxes
            nnew_pos1 = [x + delta for x, delta in zip(new_pos[1], direction)]
            nnew_pos2 = [x + delta for x, delta in zip(new_pos[0], direction)]
            grid[nnew_pos1[0]][nnew_pos1[1]] = grid[new_pos[1][0]][new_pos[1][1]]
            grid[nnew_pos2[0]][nnew_pos2[1]] = grid[new_pos[0][0]][new_pos[0][1]]
            # Update roboter
            grid[new_pos[0][0]][new_pos[0][1]] = grid[pos[0]][pos[1]]
            grid[new_pos[1][0]][new_pos[1][1]] = "."
        return True, new_pos[0], grid
    return False, pos, grid


def main() -> int:
    """Main function"""

    directions = {
        "^": (-1, 0),
        ">": (0, 1),
        "v": (1, 0),
        "<": (0, -1),
    }

    # Part 1 ###################################################################
    grid, track = load_grid_and_track(build_path(), part=1)

    # Find roboter
    robo_pos = find_position(grid, "@")

    for d in track:
        new_pos = [x + delta for x, delta in zip(robo_pos, directions[d])]
        is_true, new_pos, grid = check_pos_part1(robo_pos, directions[d], grid)
        if is_true:  # Update robos old position
            grid[robo_pos[0]][robo_pos[1]] = "."

        robo_pos = new_pos
        render(grid)

    res = 0
    for y, row in enumerate(grid):
        for x, field in enumerate(row):
            if field == "O":
                res += 100 * y + x
    print(f"Result part 1: {res}")

    # Part 2 ###################################################################
    grid, track = load_grid_and_track(build_path(), part=2)

    # Find roboter
    robo_pos = find_position(grid, "@")

    for d in track:
        new_pos = [x + delta for x, delta in zip(robo_pos, directions[d])]
        if d in {"<", ">"}:  # Left/right stays the same
            is_true, new_pos, grid = check_pos_part1(robo_pos, directions[d], grid)
        else:
            is_true, new_pos, grid = check_pos_part2(
                robo_pos, directions[d], grid, update=False
            )
            if is_true:  # Update only, if all recursions are true
                is_true, new_pos, grid = check_pos_part2(robo_pos, directions[d], grid)
        if is_true:  # Update robos old position
            grid[robo_pos[0]][robo_pos[1]] = "."

        robo_pos = new_pos
        render(grid)

    res = 0
    for y, row in enumerate(grid):
        for x, field in enumerate(row):
            if field == "[":
                res += 100 * y + x
    print(f"Result part 2: {res}")

    return 0


if __name__ == "__main__":
    sys.exit(main())

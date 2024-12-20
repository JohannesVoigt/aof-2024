"""Advent of Code - 6.12.2024"""

import os
import sys
from time import sleep
from typing import Any


DAY = 6
TEST = False
RENDER = False


class ProgressBar:
    """Simple progress bar."""

    def __init__(self, iter_: set, desc: str = None):
        self.n_iter = len(iter_)
        self.iter_ = iter(list(iter_))
        self.desc = desc if desc is not None else ""

        self.width = os.get_terminal_size().columns
        self.ndez = len(str(self.n_iter))
        self.res = self.width - len(desc) - 2 * self.ndez - 8

        self.idx = 0

    def __next__(self):
        print(
            f"{self.desc}: "
            + f"[{'.'*(self.res*self.idx//self.n_iter)}"
            + f"{' '*(self.res - self.res*self.idx//self.n_iter)}] "
            + f"({self.idx:{self.ndez}d}/{self.n_iter})",
            end="\r",
        )
        self.idx += 1
        if self.idx > self.n_iter:
            print()
        return next(self.iter_)

    def __iter__(self):
        return self


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


def render(
    floorplan,
    position: list[int, int],
    direction: int,
    sleeptime: float = 0.01,
    do_render: bool = False,
) -> None:
    """Render matrix"""
    if do_render:
        directions = ["^", ">", "v", "<"]
        os.system("cls")
        floorplan[position[0]][position[1]] = "X"
        for row in floorplan:
            print(" ".join(row))
        sleep(sleeptime)
        floorplan[position[0]][position[1]] = directions[direction]


def main() -> int:
    """Main function"""
    filepath = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "files",
        f"2024_12_{DAY:02d}{'_test' if TEST else ''}.txt",
    )

    dir_idx = None
    pos = []  # [y, x]
    with open(filepath, "r", encoding="utf-8") as file:
        init_floorplan = [list(line.replace("\n", "")) for line in file]

    # Add frame to avoid out of index errors
    init_floorplan = add_matrix_frame(init_floorplan, 1, "*")
    init_floorplan = list(tuple(row) for row in init_floorplan)

    directions = ["^", ">", "v", "<"]
    moves = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    # Get starting position and direction
    init_position: tuple = None
    init_direction_idx = None
    for y, row in enumerate(init_floorplan):
        for i, d in enumerate(directions):
            if d in row:
                init_position = (y, row.index(d))
                init_direction_idx = (i,)

    # Part 1 ###################################################################

    # Init
    floorplan = [list(row) for row in init_floorplan]
    dir_idx = init_direction_idx[0]
    pos = list(init_position)

    guard_positions = []
    while floorplan[pos[0]][pos[1]] != "*":
        # Render floorplan
        render(floorplan, pos, dir_idx, do_render=RENDER)

        # Save guard position
        guard_positions.append(tuple(pos))

        # Update position or direction
        next_pos = [n1 + n2 for n1, n2 in zip(pos, moves[dir_idx])]
        if floorplan[next_pos[0]][next_pos[1]] == "#":
            dir_idx = (dir_idx + 1) % 4
            continue
        pos = next_pos

    # Convert to set to get uniquw tuples (positions)
    guard_positions = set(guard_positions)
    print(f"Result part 1: {len(guard_positions)}")

    # Part 2 ###################################################################
    loop_cnt = 0
    guard_positions.remove(init_position)

    for guard_pos in ProgressBar(guard_positions, desc="Guard positions"):
        # Reset
        fp = [list(row) for row in init_floorplan]
        pos = list(init_position)
        dir_idx = init_direction_idx[0]

        # Add new obstraction
        fp[guard_pos[0]][guard_pos[1]] = "#"

        visited = [[0 for _ in row] for row in floorplan]
        while fp[pos[0]][pos[1]] != "*":
            next_pos = [n1 + n2 for n1, n2 in zip(pos, moves[dir_idx])]
            if fp[next_pos[0]][next_pos[1]] == "#":  # Turn
                if visited[next_pos[0]][next_pos[1]] > 4:
                    break  # Visited position >1 times from each direction

                visited[next_pos[0]][next_pos[1]] += 1
                dir_idx = (dir_idx + 1) % 4
                continue

            pos = next_pos  # Update position
        else:
            continue  # Finished wo. break (no loop)
        loop_cnt += 1

    print(f"Result part 2: {loop_cnt}")

    return 0


if __name__ == "__main__":
    sys.exit(main())

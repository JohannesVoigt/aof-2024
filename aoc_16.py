"""Advent of Code - 16.12.2024"""

from functools import cache
import os
import sys

sys.setrecursionlimit(10_000)

DAY = 16
TEST = True


def build_path() -> str:
    """Build daily path."""
    return os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "files",
        f"2024_12_{DAY:02d}{'_test' if TEST else ''}.txt",
    )


def find_position(grid: list[list[str]], token: str) -> tuple[int, int]:
    """Find unique position of 'token' in 'grid'."""
    return [
        (y, x)
        for y, row in enumerate(grid)
        for x, tile in enumerate(row)
        if tile == token
    ][0]


def get_neighbors(y: int, x: int, direction: int) -> tuple[tuple[int, int]]:
    """Get direct neighbor positions"""
    neighbors = []
    for i in reversed(range(-1, 2)):
        delta = directions[(direction - i) % 4]
        neighbors.append((y + delta[0], x + delta[1]))
    return neighbors


# @cache
# def find_path(y: int, x: int, direction: int) -> tuple[int, bool]:
#     """Find path recursively"""
#     neighbors = get_neighbors(y, x, direction)

#     step_costs = []
#     new_costs = []
#     dones = []
#     deadend = []

#     cnt = 0
#     print(y, x)
#     for i, n in enumerate(neighbors):
#         nsymbol = grid[n[0]][n[1]]
#         if nsymbol == "#":
#             cnt += 1
#             continue
#         if nsymbol == "E":
#             return 0, True, False
#         new_cost, done, dead = find_path(*n, (-1 + i) % 4)
#         step_costs.append(abs(i - 1) * 1000 + 1)
#         new_costs.append(new_cost)
#         dones.append(done)
#         deadend.append(dead)

#     if cnt == 3 or sum(deadend) == 3:  # Deadend
#         return 0, False, True

#     path_idx = None
#     current_lowest_costs = 1e10
#     for i, (step_cost, new_cost, done) in enumerate(zip(step_costs, new_costs, dones)):
#         if step_costs + new_cost < current_lowest_costs:
#             path_idx = i
#             current_lowest_costs = step_cost + new_cost
#     if path_idx is not None:
#         return current_lowest_costs, True, False
#     return 0, False, deadend


def main() -> int:
    """Main function"""

    current_dir = 0
    current_pos = find_position(grid, "S")
    end_pos = find_position(grid, "E")

    for row in grid:
        print("".join(row))

    # Part 1 ###################################################################
    #   start: east
    #   1 step ->   score +1
    #   rotate ->   score +1000
    costs = 0
    # costs, done, _ = find_path(*current_pos, current_dir)
    # print(costs, done)
    print(f"Result part 1: {costs}")

    # Part 2 ###################################################################
    res = 0
    print(f"Result part 2: {res}")

    return 0


with open(build_path(), "r", encoding="utf-8") as file:
    grid = [list(line.replace("\n", "")) for line in file]

directions = {  # +1=clockwise / -1=counterclockwise
    0: (0, 1),  # East
    1: (1, 0),  # South
    2: (0, -1),  # West
    3: (-1, 0),  # North
}

if __name__ == "__main__":
    sys.exit(main())

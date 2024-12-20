"""Advent of Code - 13.12.2024"""

import re
import os
import sys


DAY = 13
TEST = False


def build_path() -> str:
    """Build daily path."""
    return os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "files",
        f"2024_12_{DAY:02d}{'_test' if TEST else ''}.txt",
    )


def solve(machine: list[int], add: int = 0) -> tuple[float, float, bool]:
    """Solve LGS."""
    xa, ya, xb, yb, x, y = machine
    x += add
    y += add
    na = (x * yb - xb * y) // (xa * yb - xb * ya)
    nb = (x - na * xa) // xb
    if (
        (na >= 0)
        and (nb >= 0)
        and (na * xa + nb * xb == x)
        and (na * ya + nb * yb == y)
    ):
        return na, nb, True
    return na, nb, False


def main() -> int:
    """Main function"""

    with open(build_path(), "r", encoding="utf-8") as file:
        machines = []
        ms = []
        for line in file:
            nums = list(map(int, re.findall(r"\d+", line)))
            if len(ms) < 6:
                ms += nums
            if len(ms) >= 6:
                machines.append(ms)
                ms = []

    # Part 1 ###################################################################
    tokens = 0
    for machine in machines:
        na, nb, is_valid = solve(machine)
        if is_valid:
            tokens += 3 * na + nb
    print(f"Tokens part 1: {tokens}")

    # Part 2 ###################################################################
    tokens = 0
    for machine in machines:
        na, nb, is_valid = solve(machine, add=10_000_000_000_000)
        if is_valid:
            tokens += 3 * na + nb
    print(f"Tokens part 2: {tokens}")

    return 0


if __name__ == "__main__":
    sys.exit(main())

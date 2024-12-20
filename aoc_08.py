"""Advent of Code - 8.12.2024"""

from collections import defaultdict
import os
import sys


DAY = 8
TEST = False


def main() -> int:
    """Main function"""
    filepath = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "files",
        f"2024_12_{DAY:02d}{'_test' if TEST else ''}.txt",
    )

    with open(filepath, "r", encoding="utf-8") as file:
        grid = [list(line.replace("\n", "")) for line in file]

    # Part 1 ###################################################################
    # Find all antenna indicators (lower- and uppercase letters and numbers)
    unique_antennas = set(c for line in grid for c in line).difference(".")
    print(f"Unique antennas: {unique_antennas}")

    # Find all antenna positions
    ant_positions = defaultdict(set)
    for y, line in enumerate(grid):
        for x, val in enumerate(line):
            for ant in unique_antennas:
                if val == ant:
                    ant_positions[ant].update([(y, x)])

    # Find antinodes
    shape = (len(grid), len(grid[0]))
    antinodes_p1 = set()
    for ant in unique_antennas:  # Check all ant frequencies
        for ant_pos1 in ant_positions[ant]:  # Check each ant
            for ant_pos2 in ant_positions[ant].difference([ant_pos1]):  # Neighbor ants
                for ant1, ant2 in [[ant_pos1, ant_pos2], [ant_pos2, ant_pos1]]:
                    pos = [c1 - (c2 - c1) for c1, c2 in zip(ant1, ant2)]
                    if 0 <= pos[0] < shape[0] and 0 <= pos[1] < shape[1]:
                        antinodes_p1.update([tuple(pos)])

    print(f"Result part 1: {len(antinodes_p1)}")

    # Part 2 ###################################################################
    # Find antinodes
    antinodes_p2 = set()
    antinodes_p2.update(antinodes_p1)
    for ant in unique_antennas:

        for ant_pos1 in ant_positions[ant]:
            antinodes_p2.update([ant_pos1])  # Also add antenna positions

            for ant_pos2 in ant_positions[ant].difference([ant_pos1]):
                for ant1, ant2 in [[ant_pos1, ant_pos2], [ant_pos2, ant_pos1]]:
                    i = 2
                    while True:  # Add harmonics
                        pos = [c1 - i * (c2 - c1) for c1, c2 in zip(ant1, ant2)]
                        if (
                            pos[0] < 0
                            or shape[0] <= pos[0]
                            or pos[1] < 0
                            or shape[1] <= pos[1]
                        ):
                            break
                        antinodes_p2.update([tuple(pos)])
                        i += 1
    print(f"Result part 2: {len(antinodes_p2)}")

    return 0


if __name__ == "__main__":
    sys.exit(main())

"""Advent of Code - 19.12.2024"""

import re
import os
import sys

DAY = 19
TEST = False


def build_path() -> str:
    """Build daily path."""
    return os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "files",
        f"2024_12_{DAY:02d}{'_test' if TEST else ''}.txt",
    )


def check_str(text: str, str_parts: list[str]) -> bool:
    """Check if string is combination of strings in list."""
    patterns = [p for p in str_parts if p in text]
    r = re.compile("(?:" + "|".join(patterns) + ")*$")
    if r.match(text) is not None:
        print(r)
        return True
    return False


def main() -> int:
    """Main function"""
    with open(build_path(), "r", encoding="utf-8") as file:
        all_patterns = []
        designs = []
        for i, line in enumerate(file.readlines()):
            if i == 0:
                all_patterns += list(line.replace("\n", "").split(", "))
            else:
                text = line.replace("\n", "")
                if len(text) > 0:
                    designs.append(text)

    # Colors: w, u, b, r, g

    all_patterns.sort()  # Sort albhabetic
    all_patterns.sort(key=len)  # Sort by string length

    patterns = []
    for p in all_patterns:  # Base patterns
        if check_str(p, patterns):
            continue
        patterns.append(p)

    # Part 1 ###################################################################
    n_valid_designs = sum((check_str(d, patterns) for d in designs))
    print(f"Result part 1: {n_valid_designs}")

    # Part 2 ###################################################################
    res = 0
    print(f"Result part 2: {0}")

    return 0


if __name__ == "__main__":
    sys.exit(main())

"""Advent of Code - 5.12.2024"""

import os
import sys


DAY = 5
TEST = False


def main() -> int:
    """Main function"""
    filepath = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "files",
        f"2024_12_{DAY:02d}{'_test' if TEST else ''}.txt",
    )

    rules = []
    updates: list[list[int]] = []
    with open(filepath, "r", encoding="utf-8") as file:
        is_update = False
        for line in file:
            if is_update:
                updates.append(list(map(int, line.replace("\n", "").split(","))))
            else:
                if line == "\n":
                    is_update = True
                    continue
                rules.append(list(map(int, line.split("|"))))

    # Part 1
    res_p1 = 0
    for update in updates:
        valid_rules = [r for r in rules if set(r).issubset(set(update))]
        for num1, num2 in valid_rules:
            idx1 = update.index(num1)
            idx2 = update.index(num2)
            if idx1 > idx2:
                break
        else:
            res_p1 += update[len(update) // 2]
    print(f"Result part 1: {res_p1}")

    # Part 2
    res_p2 = 0
    for update in updates:
        valid_rules = [r for r in rules if set(r).issubset(set(update))]
        corrected = False
        not_correct = True
        while not_correct:  # Continue until correct
            for num1, num2 in valid_rules:
                idx1 = update.index(num1)
                idx2 = update.index(num2)
                if idx1 > idx2:  # If not correct -> swap numbers
                    tmp = update[idx1]
                    update[idx1] = update[idx2]
                    update[idx2] = tmp
                    corrected = True
                    break
            else:  # Everything correct (for loop ends without break)
                not_correct = False
        if corrected:
            res_p2 += update[len(update) // 2]
    print(f"Result part 2: {res_p2}")

    return 0


if __name__ == "__main__":
    sys.exit(main())

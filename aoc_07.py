"""Advent of Code - 7.12.2024"""

import os
import sys


DAY = 7
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
            print(end="\n")
        return next(self.iter_)

    def __iter__(self):
        return self


def decimal_to_base(
    num: int, base: int, numlen: int = None, as_list_of_ints: bool = True
):
    """Connvert decimal number to number of base 'base'."""
    if num == 0:
        new_base_num = "0"
    else:
        new_base_num = ""
        while num > 0:
            new_base_num = str(num % base) + new_base_num
            num = num // base

    if numlen is not None:
        if numlen < len(new_base_num):
            raise ValueError(
                f"Cannot put a number of length {len(new_base_num)} "
                + f" in a {numlen} long number."
            )
        new_base_num = (numlen - len(new_base_num)) * "0" + new_base_num
    if as_list_of_ints:
        return list(map(int, new_base_num))
    return new_base_num


def main() -> int:
    """Main function"""

    current_dir = os.path.dirname(os.path.realpath(__file__))
    filename = f"2024_12_{DAY:02d}{"_test" if TEST else ""}.txt"
    filepath = os.path.join(current_dir, "files", filename)

    with open(filepath, "r", encoding="utf-8") as file:
        data = [list(map(int, line.replace(":", "").split(" "))) for line in file]

    # Part 1 ###################################################################
    res_p1 = 0

    for row in data:
        correct_res, numbers = row[0], row[1:]
        num_operators = len(numbers) - 1
        num_permutations = 2**num_operators

        for i in range(num_permutations):
            indicators = list(map(int, list(f"{i:0{num_operators}b}")))

            res = numbers[0]
            for ind, num in zip(indicators, numbers[1:]):
                res += num * (1 - ind) + res * ind * (num - 1)
            if res == correct_res:
                res_p1 += res
                break

    print(f"Result part 1: {res_p1}")

    # Part 2 ###################################################################
    res_p2 = 0

    for row in ProgressBar(data, desc="Iter"):
        correct_res, numbers = row[0], row[1:]
        num_operators = len(numbers) - 1
        num_permutations = 3**num_operators

        for i in range(num_permutations):
            indicators = decimal_to_base(i, base=3, numlen=num_operators)

            res = numbers[0]
            for ind, num in zip(indicators, numbers[1:]):
                if ind == 0:
                    res += num
                elif ind == 1:
                    res *= num
                else:
                    res = int(str(res) + str(num))
            if res == correct_res:
                res_p2 += res
                break

    print(f"Result part 2: {res_p2}")

    return 0


if __name__ == "__main__":
    sys.exit(main())

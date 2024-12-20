"""Advent of Code - 17.12.2024"""

from copy import deepcopy
import os
import re
import sys

DAY = 17
TEST = False


def build_path() -> str:
    """Build daily path."""
    return os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "files",
        f"2024_12_{DAY:02d}{'_test' if TEST else ''}.txt",
    )


def decimal_to_base(num: int, base: int, numlen: int = None):
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
    return int(new_base_num)


def base_to_decimal(num: int, base: int) -> int:
    """Convert number of base 'base' to a decimal number."""
    nums = list(map(int, list(str(num))))
    res = 0
    for exp, n in enumerate(reversed(nums)):
        res += n * base**exp
    return res


def get_combo_op_val(combo_op: int, reg: list[int]) -> int:
    """Get combo operand value."""
    if 0 <= combo_op <= 3:
        return combo_op
    if 4 <= combo_op <= 6:
        return reg[combo_op - 4]
    raise ValueError("Combo operand 7 should not appear in valid programs.")


def run_program(reg: list[int], program: list[int]) -> str:
    """Run program"""
    ptr = 0
    out = []
    while ptr <= (len(program) - 2):
        instr, operand = program[ptr : ptr + 2]
        if instr == 0:
            reg[0] = reg[0] // 2 ** get_combo_op_val(operand, reg)
        elif instr == 1:
            reg[1] ^= operand
        elif instr == 2:
            reg[1] = get_combo_op_val(operand, reg) % 8
        elif instr == 3:
            if reg[0] != 0:
                ptr = operand - 2
        elif instr == 4:
            reg[1] ^= reg[2]
        elif instr == 5:
            out.append(f"{get_combo_op_val(operand, reg) % 8}")
        elif instr == 6:
            reg[1] = reg[0] // 2 ** get_combo_op_val(operand, reg)
        elif instr == 7:
            reg[2] = reg[0] // 2 ** get_combo_op_val(operand, reg)
        else:
            raise ValueError("Instruction opcode invalid.")
        ptr += 2
    return ",".join(out), "".join(out)


def find_register_val(reg: list[int], program: list[int]) -> bool:
    """Run program part 2"""
    ptr = 0
    out = []
    while ptr <= (len(program) - 2):
        instr, operand = program[ptr : ptr + 2]
        if instr == 0:
            reg[0] = reg[0] // 2 ** get_combo_op_val(operand, reg)
        elif instr == 1:
            reg[1] ^= operand
        elif instr == 2:
            reg[1] = get_combo_op_val(operand, reg) % 8
        elif instr == 3:
            if reg[0] != 0:
                ptr = operand - 2
        elif instr == 4:
            reg[1] ^= reg[2]
        elif instr == 5:
            out.append(get_combo_op_val(operand, reg) % 8)
        elif instr == 6:
            reg[1] = reg[0] // 2 ** get_combo_op_val(operand, reg)
        elif instr == 7:
            reg[2] = reg[0] // 2 ** get_combo_op_val(operand, reg)
        else:
            raise ValueError("Instruction opcode invalid.")
        ptr += 2
        if len(out) > 0:
            if len(out) > len(program):
                break
            if out[-1] != program[len(out) - 1]:
                break
    return out == program


def main() -> int:
    """Main function"""
    with open(build_path(), "r", encoding="utf-8") as file:
        puzzle_in = [line for line in file]

    os.system("cls")

    reg = [int(re.findall(r"\d+", line)[0]) for line in puzzle_in if "Register" in line]
    program = list(map(int, re.findall(r"\d+", puzzle_in[-1])))

    # Part 1 ###################################################################
    out, _ = run_program(deepcopy(reg), program)
    # print("Output: ", out)

    # Part 2 ###################################################################
    # 2,4,1,6,7,5,4,4,1,7,0,3,5,5,3,0
    # 1, 2, 7, 7,
    # reg_value = int("1000", base=8)
    # stop_val = int("1010", base=8)
    # reg_value = 0o127110204400
    reg_value = 0o1271135723100000
    stop_val_ = 0o1271135723177777
    len_ = len(f"{stop_val_:o}")

    print("2,4,1,6,7,5,4,4,1,7,0,3,5,5,3,0")

    47910079998866

    while reg_value <= stop_val_:
        try_reg = deepcopy(reg)
        try_reg[0] = reg_value
        out1, out2 = run_program(try_reg, program)
        # print(f"{decimal_to_base(reg_value, 8):3d} | {out1}")
        if out2 == "".join(map(str, program[-len_:])):
            print(oct(reg_value), out2)
        # if not reg_value % 100_000:
        #     print(reg_value)

        # try_reg = deepcopy(reg)
        # try_reg[0] = reg_value
        if find_register_val(try_reg, program):
            print("Found")
            break

        reg_value += 1
    # 10324415
    # 10326511, 10220615, 10222711,
    print(f"Register A: {reg_value}")
    print(f"{reg_value}")

    # print("035430")
    # print(decimal_to_base(115416, 8))
    # print(decimal_to_base(2024, 8))
    # print(base_to_decimal(115416, 8) - 35430)
    # print(decimal_to_base(117440, 8))

    # n = 117440
    # while n > 0:
    #     n = n // 8
    #     print(n % 8)

    # while n > 0:
    #     n = n // 8
    #     print(n % 8)
    # print(1,5,0,1,7,4,1,0,3)
    return 0


if __name__ == "__main__":
    sys.exit(main())

# 0,3,5,4,3,0
# 1,

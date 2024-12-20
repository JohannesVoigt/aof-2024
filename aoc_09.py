"""Advent of Code - 9.12.2024"""

import os
import sys


DAY = 9
TEST = False


def build_path() -> str:
    """Build daily path."""
    return os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "files",
        f"2024_12_{DAY:02d}{'_test' if TEST else ''}.txt",
    )


def cumsum(list_of_nums: list[int]) -> list[int]:
    """Return cummulative sum of list entries."""
    return [sum(list_of_nums[:idx]) for idx in range(len(list_of_nums))]


def main() -> int:
    """Main function"""

    disk_map = []
    with open(build_path(), "r", encoding="utf-8") as file:
        disk_map = list(map(int, list(file.read().replace("\n", ""))))

    # Part 1 ###################################################################
    # Split into 'files' and 'free space'
    disk = [
        "." if i % 2 else i // 2 for i, num in enumerate(disk_map) for _ in range(num)
    ]
    print(f"Length of disk: {len(disk)}")

    file_blocks_idxs = [idx for idx, d in enumerate(disk) if isinstance(d, int)]
    free_space_idxs = [idx for idx, d in enumerate(disk) if isinstance(d, str)]

    # Fragmentation
    for pos_block, pos_space in zip(reversed(file_blocks_idxs), free_space_idxs):
        if pos_block < pos_space:
            break
        disk[pos_space] = disk[pos_block]
        disk[pos_block] = "."
    fragmented_files = disk[: -len(free_space_idxs)]

    # Calculate checksum
    checksum = sum((idx * file_id for idx, file_id in enumerate(fragmented_files)))

    print(f"Calculated checksum part 1: {checksum}")

    # Part 2 ###################################################################
    disk = [
        "." if i % 2 else i // 2 for i, num in enumerate(disk_map) for _ in range(num)
    ]
    # Get length and start position of file/space blocks
    file_lens = disk_map[::2]
    space_lens = disk_map[1::2]
    file_start_idxs = cumsum(disk_map)[::2]
    space_start_idx = cumsum(disk_map)[1::2]

    # Moves files
    for f_len, f_idx in zip(reversed(file_lens), reversed(file_start_idxs)):
        for i, (s_len, s_idx) in enumerate(zip(space_lens, space_start_idx)):
            if (f_len <= s_len) and (f_idx > s_idx):  # Enough space to move file
                # Copy file
                disk[s_idx : s_idx + f_len] = disk[f_idx : f_idx + f_len]
                # Remove file
                disk[f_idx : f_idx + f_len] = ["."] * f_len
                # Update start indices and lengths
                space_lens[i] -= f_len
                space_start_idx[i] += f_len
                break

    checksum = sum(
        (idx * file_id for idx, file_id in enumerate(disk) if isinstance(file_id, int))
    )
    print(f"Calculated checksum part 2: {checksum}")

    return 0


if __name__ == "__main__":
    sys.exit(main())

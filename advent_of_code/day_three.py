from helpers import load_txt
import re


def get_position_of_symbols_in_matrix(matrix: list[str]) -> list[tuple[int, int]]:
    indices = [
        (n, m)
        for n, row in enumerate(matrix)
        for m in get_position_of_symbols_in_row(row)
    ]

    return indices


def get_position_of_symbols_in_row(row: str) -> list[int]:
    iterator = re.finditer(r"[^\d.]", row)
    indices = [m.start(0) for m in iterator]

    return indices


if __name__ == "__main__":
    puzzle_txt = load_txt("advent_of_code/files/gear_ratios.txt")
    print(get_position_of_symbols_in_matrix(puzzle_txt))

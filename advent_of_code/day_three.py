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


def get_digit_coordinates(
    matrix: list[str], indices: list[tuple[int, int]]
) -> list[tuple[int, int]]:
    return [(i, j) for i, j in indices if matrix[i][j].isdigit()]


def generate_all_adjacent_coordinates(
    indices: list[tuple[int, int]], max_index: tuple[int, int]
) -> list[tuple[int, int]]:
    return [i for j in indices for i in generate_adjacent_coordinates(j, max_index)]


def generate_adjacent_coordinates(
    index: tuple[int, int], max_index: tuple[int, int]
) -> list[tuple[int, int]]:
    indices = [
        (i, j)
        for i in range(index[0] - 1, index[0] + 2)
        for j in range(index[1] - 1, index[1] + 2)
        if 0 <= i <= max_index[0] and 0 <= j <= max_index[1]
    ]

    return indices


if __name__ == "__main__":
    puzzle_txt = load_txt("advent_of_code/files/gear_ratios.txt")
    max_index = (len(puzzle_txt), len(puzzle_txt[0]))
    symbol_indices = get_position_of_symbols_in_matrix(puzzle_txt)
    adjacent_indices = generate_all_adjacent_coordinates(symbol_indices, max_index)
    digit_indices = get_digit_coordinates(puzzle_txt, adjacent_indices)
    print(digit_indices)

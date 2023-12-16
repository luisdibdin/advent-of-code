from helpers import load_txt
import re
from itertools import groupby


def get_position_of_symbols_in_matrix(matrix: list[str]) -> list[tuple[int, int]]:
    indices = [
        (n, m)
        for n, row in enumerate(matrix)
        for m in get_position_of_symbols_in_row(row)
    ]

    return indices


def get_position_of_symbols_in_row(row: str) -> list[int]:
    symbol_positions = re.finditer(r"[^\d.]", row)
    indices = [m.start(0) for m in symbol_positions]

    return indices


def get_only_adjacent_digits(
    all_digits: dict[int, dict[range, int]], adjacent_digit: dict[int, list[int]]
) -> list[int]:
    return [
        digit
        for (k, v) in all_digits.items()
        for i, digit in enumerate(v.values())
        if any([j in list(v.keys())[i] for j in adjacent_digit.get(k, [])])
    ]


def get_position_of_all_digits(matrix: list[str]) -> dict[int, dict[range, int]]:
    return {i: get_position_of_digits(v) for i, v in enumerate(matrix)}


def get_position_of_digits(row: str) -> dict[range, int]:
    digit_positions = re.finditer(r"\d+", row)
    indices = {range(i.start(0), i.end(0)): int(i.group()) for i in digit_positions}

    return indices


def get_digit_coordinates_by_row(
    indicies: list[tuple[int, int]]
) -> dict[int, list[int]]:
    indices_by_row = group_indices_by_row(indicies)
    simplified_indices = {
        k: remove_consecutive_elements(v) for (k, v) in indices_by_row.items()
    }

    return simplified_indices


def group_indices_by_row(indices: list[tuple[int, int]]) -> dict[int, list[int]]:
    return {
        k: [*map(lambda v: v[1], values)]
        for k, values in groupby(sorted(indices, key=lambda x: x[0]), lambda x: x[0])
    }


def remove_consecutive_elements(integer_list: list[int]) -> list[int]:
    new_list = [integer_list[0]] + [
        integer_list[i + 1]
        for i in range(len(integer_list) - 1)
        if integer_list[i] + 1 != integer_list[i + 1]
    ]

    return new_list


def get_adjacent_digit_coordinates(
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

    digit_indices = get_position_of_all_digits(puzzle_txt)

    symbol_indices = get_position_of_symbols_in_matrix(puzzle_txt)
    adjacent_indices = generate_all_adjacent_coordinates(symbol_indices, max_index)
    adjacent_digit_indices = get_adjacent_digit_coordinates(
        puzzle_txt, adjacent_indices
    )
    digit_indices_by_row = get_digit_coordinates_by_row(adjacent_digit_indices)

    adjacent_digits = get_only_adjacent_digits(digit_indices, digit_indices_by_row)

    print(sum(adjacent_digits))

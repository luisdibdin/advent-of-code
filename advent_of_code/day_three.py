from helpers import load_txt
import re
from itertools import groupby
from typing import Any
import numpy as np


def get_position_of_symbols_in_matrix(
    pattern: str, matrix: list[str]
) -> list[tuple[int, int]]:
    indices = [
        (n, m)
        for n, row in enumerate(matrix)
        for m in get_position_of_symbols_in_row(pattern, row)
    ]

    return indices


def get_position_of_symbols_in_row(pattern: str, row: str) -> list[int]:
    symbol_positions = re.finditer(pattern, row)
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


def get_adjacent_digit_coordinates_by_row(
    matrix: list[str],
    indices: dict[tuple[int, int] : list[tuple[int, int]]],
    adjacent_condition=lambda x: x > 0,
) -> dict[int, list[int]]:
    adjacent_digit_by_symbol = {
        k: get_digit_coordinates_by_row(
            [(i, j) for i, j in v if matrix[i][j].isdigit()]
        )
        for (k, v) in indices.items()
    }
    conditional_digits_positions = {
        k: v
        for (k, v) in adjacent_digit_by_symbol.items()
        if adjacent_condition(count_subdictionary_list(v))
    }

    return conditional_digits_positions


def count_subdictionary_list(dictionary: dict[Any, dict[Any, list[Any]]]) -> int:
    return sum([len(i) for i in dictionary.values()])


def get_digit_coordinates_by_row(
    indicies: list[tuple[int, int]]
) -> dict[int, list[int]]:
    indices_by_row = group_indices_by_row(indicies)
    simplified_indices = {
        k: remove_consecutive_elements(v) for (k, v) in indices_by_row.items()
    }

    return simplified_indices


def generate_all_adjacent_coordinates(
    indices: list[tuple[int, int]], max_index: tuple[int, int]
) -> dict[tuple[int, int], list[tuple[int, int]]]:
    return {i: generate_adjacent_coordinates(i, max_index) for i in indices}


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

    # part 1
    symbol_indices = get_position_of_symbols_in_matrix(r"[^\d.]", puzzle_txt)
    adjacent_indices = generate_all_adjacent_coordinates(symbol_indices, max_index)
    adjacent_digit_indices_by_row = get_adjacent_digit_coordinates_by_row(
        puzzle_txt, adjacent_indices
    )
    adjacent_digits = {
        k: get_only_adjacent_digits(digit_indices, v)
        for (k, v) in adjacent_digit_indices_by_row.items()
    }

    print(sum([item for row in adjacent_digits.values() for item in row]))

    # part 2
    print("Part 2")
    symbol_indices = get_position_of_symbols_in_matrix(r"\*", puzzle_txt)
    adjacent_indices = generate_all_adjacent_coordinates(symbol_indices, max_index)
    adjacent_digit_indices_by_row = get_adjacent_digit_coordinates_by_row(
        puzzle_txt, adjacent_indices, lambda x: x == 2
    )
    adjacent_digits = {
        k: get_only_adjacent_digits(digit_indices, v)
        for (k, v) in adjacent_digit_indices_by_row.items()
    }

    print(sum([np.prod(item) for item in adjacent_digits.values()]))

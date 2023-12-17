from advent_of_code.day_three import (
    get_position_of_symbols_in_row,
    get_position_of_symbols_in_matrix,
    generate_adjacent_coordinates,
    generate_all_adjacent_coordinates,
    get_adjacent_digit_coordinates_by_row,
    group_indices_by_row,
    remove_consecutive_elements,
    get_position_of_digits,
    get_position_of_all_digits,
    get_only_adjacent_digits,
    count_subdictionary_list,
)


def test_get_position_of_symbols_in_row():
    assert get_position_of_symbols_in_row(r"\*", "....*.") == [4]
    assert get_position_of_symbols_in_row(r"[^\d.]", ".*../..78") == [1, 4]


def test_get_position_of_symbols_in_matrix():
    assert get_position_of_symbols_in_matrix(r"\*", ["....*."]) == [(0, 4)]
    assert get_position_of_symbols_in_matrix(r"\*", ["....*./"]) == [(0, 4)]
    assert get_position_of_symbols_in_matrix(r"\*", ["....*./", "./..*"]) == [
        (0, 4),
        (1, 4),
    ]


def test_generate_adjacent_coordinates():
    assert generate_adjacent_coordinates((1, 4), (6, 6)) == [
        (0, 3),
        (0, 4),
        (0, 5),
        (1, 3),
        (1, 4),
        (1, 5),
        (2, 3),
        (2, 4),
        (2, 5),
    ]
    assert generate_adjacent_coordinates((0, 0), (6, 6)) == [
        (0, 0),
        (0, 1),
        (1, 0),
        (1, 1),
    ]
    assert generate_adjacent_coordinates((6, 6), (6, 7)) == [
        (5, 5),
        (5, 6),
        (5, 7),
        (6, 5),
        (6, 6),
        (6, 7),
    ]


def test_generate_all_adjacent_coordinates():
    assert generate_all_adjacent_coordinates([(0, 0), (6, 6)], (6, 7)) == {
        (0, 0): [(0, 0), (0, 1), (1, 0), (1, 1)],
        (6, 6): [(5, 5), (5, 6), (5, 7), (6, 5), (6, 6), (6, 7)],
    }


def test_get_digit_coordinates():
    assert get_adjacent_digit_coordinates_by_row(
        ["/.78..", "1...."], {(0, 0): [(0, 0), (0, 1), (1, 0), (1, 1)]}
    ) == {(0, 0): {1: [0]}}
    assert get_adjacent_digit_coordinates_by_row(
        ["/.78..", "1....", "*72.."],
        {
            (0, 0): [(0, 0), (0, 1), (1, 0), (1, 1)],
            (2, 0): [(1, 0), (1, 1), (2, 0), (2, 1)],
        },
        lambda x: x == 2,
    ) == {(2, 0): {1: [0], 2: [1]}}


def test_count_subdictionary_list():
    assert count_subdictionary_list({0: [1], 1: [2]}) == 2
    assert count_subdictionary_list({0: [1], 1: [2, 3]}) == 3


def test_group_indices_by_row():
    assert group_indices_by_row([(0, 2), (0, 3), (0, 4), (1, 2), (1, 3), (1, 4)]) == {
        0: [2, 3, 4],
        1: [2, 3, 4],
    }


def test_remove_consecutive_elements():
    assert remove_consecutive_elements([2, 3, 4, 6, 7, 9, 10]) == [2, 6, 9]
    assert remove_consecutive_elements([2, 4, 5, 6, 7, 9, 10]) == [2, 4, 9]
    assert remove_consecutive_elements([1, 2, 3, 7, 8, 9, 15, 16, 20]) == [1, 7, 15, 20]
    assert remove_consecutive_elements([1, 3, 5, 7, 9, 11]) == [1, 3, 5, 7, 9, 11]


def test_get_position_of_digits():
    assert get_position_of_digits("...453...") == {range(3, 6): 453}
    assert get_position_of_digits("...453.../..61.") == {
        range(3, 6): 453,
        range(12, 14): 61,
    }


def test_get_position_of_all_digits():
    assert get_position_of_all_digits(["...453...", ".12.../."]) == {
        0: {range(3, 6): 453},
        1: {range(1, 3): 12},
    }


def test_get_only_adjacent_digits():
    assert get_only_adjacent_digits(
        {0: {range(3, 6): 453}, 1: {range(1, 3): 12}},
        {1: [1]},
    ) == [12]
    assert get_only_adjacent_digits(
        {0: {range(3, 6): 453}, 1: {range(1, 3): 12, range(5, 8): 567}},
        {1: [1, 6]},
    ) == [12, 567]

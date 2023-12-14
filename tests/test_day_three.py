from advent_of_code.day_three import (
    get_position_of_symbols_in_row,
    get_position_of_symbols_in_matrix,
    generate_adjacent_coordinates,
    generate_all_adjacent_coordinates,
    get_digit_coordinates,
)


def test_get_position_of_symbols_in_row():
    assert get_position_of_symbols_in_row("....*.") == [4]
    assert get_position_of_symbols_in_row(".*../..78") == [1, 4]


def test_get_position_of_symbols_in_matrix():
    assert get_position_of_symbols_in_matrix(["....*."]) == [(0, 4)]
    assert get_position_of_symbols_in_matrix(["....*./"]) == [(0, 4), (0, 6)]
    assert get_position_of_symbols_in_matrix(["....*./", "./..#"]) == [
        (0, 4),
        (0, 6),
        (1, 1),
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
    assert generate_all_adjacent_coordinates([(0, 0), (6, 6)], (6, 7)) == [
        (0, 0),
        (0, 1),
        (1, 0),
        (1, 1),
        (5, 5),
        (5, 6),
        (5, 7),
        (6, 5),
        (6, 6),
        (6, 7),
    ]


def test_get_digit_coordinates():
    assert get_digit_coordinates(
        ["..78..", "1../.."], [(0, 2), (0, 3), (0, 4), (1, 2), (1, 3), (1, 4)]
    ) == [(0, 2), (0, 3)]

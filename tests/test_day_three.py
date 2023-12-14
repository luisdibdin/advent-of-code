from advent_of_code.day_three import (
    get_position_of_symbols_in_row,
    get_position_of_symbols_in_matrix,
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

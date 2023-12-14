from advent_of_code.day_one import (
    search_string_for_integers,
    concat_first_and_last_integers_in_integer_list,
    concat_first_and_last_integers_in_string,
    sum_all_strings_in_list,
    replace_string_with_digit,
    string_to_digit_map,
)


def test_search_string_for_integers_returns_trivial_case():
    assert search_string_for_integers("1") == [1]


def test_search_string_for_integers_returns_after_char():
    assert search_string_for_integers("a1") == [1]
    assert search_string_for_integers("abc2") == [2]


def test_search_string_for_integers_returns_list_of_all_integers():
    assert search_string_for_integers("a1b2c3d") == [1, 2, 3]
    assert search_string_for_integers("321") == [3, 2, 1]


def test_concat_first_and_last_integers_in_integer_list():
    assert concat_first_and_last_integers_in_integer_list([1, 2, 3]) == 13


def test_concat_first_and_last_integers_in_string():
    assert concat_first_and_last_integers_in_string("a1b2c3") == 13
    assert concat_first_and_last_integers_in_string("1234") == 14


def test_sum_all_strings_in_list():
    test_list = ["a1b2c3", "d4e5f6"]
    assert sum_all_strings_in_list(test_list) == 59


def test_replace_string_with_digit():
    assert replace_string_with_digit("nine", string_to_digit_map) == "9nine"
    assert replace_string_with_digit("abcnine", string_to_digit_map) == "abc9nine"
    assert (
        replace_string_with_digit("abeightwo3d", string_to_digit_map) == "ab8eigh2two3d"
    )
    assert (
        replace_string_with_digit("oneabc1nine4nine", string_to_digit_map)
        == "1oneabc19nine49nine"
    )
    assert (
        replace_string_with_digit("4nineeightseven2", string_to_digit_map)
        == "49nine8eight7seven2"
    )

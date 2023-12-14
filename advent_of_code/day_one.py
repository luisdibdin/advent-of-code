import re
from helpers import load_txt

string_to_digit_map: dict[str, str] = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def replace_string_with_digit(string: str, mapping: dict[str]) -> str:
    pattern = re.compile("(?=({}))".format("|".join(mapping.keys())))
    test = pattern.sub(lambda x: mapping[re.escape(x.group(1))], string)

    return test


def sum_all_strings_in_list(string_list: list[str]) -> int:
    return sum([concat_first_and_last_integers_in_string(s) for s in string_list])


def concat_first_and_last_integers_in_string(string: str) -> int:
    integer_list = search_string_for_integers(string)
    result = concat_first_and_last_integers_in_integer_list(integer_list)

    return result


def search_string_for_integers(string: str) -> list[int]:
    return [int(c) for c in string if c.isdigit()]


def concat_first_and_last_integers_in_integer_list(integer_list: list[int]) -> int:
    return int(f"{integer_list[0]}{integer_list[-1]}")


if __name__ == "__main__":
    trebuchet_txt = load_txt("advent_of_code/files/trebuchet.txt")
    replaced_trebuchet_txt = [
        replace_string_with_digit(s, string_to_digit_map) for s in trebuchet_txt
    ]
    result = sum_all_strings_in_list(replaced_trebuchet_txt)
    print(result)

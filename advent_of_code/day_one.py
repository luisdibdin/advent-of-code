def load_trebuchet_txt() -> list[str]:
    with open("advent_of_code/files/trebuchet.txt", "r") as f:
        data = f.read()
        data_list = data.split("\n")

    return data_list


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
    trebuchet_txt = load_trebuchet_txt()
    result = sum_all_strings_in_list(trebuchet_txt)
    print(result)

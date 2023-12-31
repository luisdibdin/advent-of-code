from helpers import load_txt
import re
import numpy as np

cube_limit = {"red": 12, "green": 13, "blue": 14}


def get_game_id(string: str) -> int:
    return int(re.search(r"\d+(?=:)", string).group())


def is_game_impossible(game: str, cube_limit: dict[str, int]) -> bool:
    sets = split_games_into_sets(game)
    impossible_sets = [is_set_impossible(s, cube_limit) for s in sets]

    return any(impossible_sets)


def calculate_power_of_game(game: str) -> int:
    maximum_cubes = find_maximum_cubes_in_game_by_colour(game)

    return np.prod(list(maximum_cubes.values()))


def find_maximum_cubes_in_game_by_colour(game: str) -> dict[str, int]:
    sets = split_games_into_sets(game)
    cubes_by_set = [split_sets_into_cubes(s) for s in sets]
    counted_cubes_by_set = [count_cubes_in_set(c) for s in cubes_by_set for c in s]

    return dict(sorted(counted_cubes_by_set))


def split_games_into_sets(string: str) -> list[str]:
    sets = re.sub(r"Game \d+: ", "", string)
    return sets.split("; ")


def is_set_impossible(set: str, cube_limit: dict[str, int]) -> bool:
    cubes = split_sets_into_cubes(set)
    counted_cubes = [count_cubes_in_set(cube) for cube in cubes]
    cubes_over_limit = [is_cube_over_limit(c, cube_limit) for c in counted_cubes]

    return any(cubes_over_limit)


def split_sets_into_cubes(string: str) -> list[str]:
    return string.split(", ")


def count_cubes_in_set(string: str) -> tuple[str, int]:
    cubes = string.split(" ")
    return (cubes[1].lower(), int(cubes[0]))


def is_cube_over_limit(cube: tuple[str, int], cube_limit: dict[str, int]) -> bool:
    return cube[1] > cube_limit[cube[0]]


if __name__ == "__main__":
    puzzle_txt = load_txt("advent_of_code/files/cube_conundrum.txt")
    possible_games = [
        get_game_id(game)
        for game in puzzle_txt
        if not is_game_impossible(game, cube_limit)
    ]
    total_ids = sum(possible_games)
    print(total_ids)

    power_of_games = [calculate_power_of_game(game) for game in puzzle_txt]
    total_power = sum(power_of_games)
    print(total_power)

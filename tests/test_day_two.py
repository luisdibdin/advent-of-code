from advent_of_code.day_two import (
    get_game_id,
    split_games_into_sets,
    split_sets_into_cubes,
    count_cubes_in_set,
    is_cube_over_limit,
    is_set_impossible,
    is_game_impossible,
)


def test_get_game_id():
    assert get_game_id("Game 1: 3 red") == 1
    assert get_game_id("Game 2: 3 red") == 2
    assert get_game_id("Game 12: 3 red") == 12


def test_split_games_into_sets():
    assert split_games_into_sets("Game 1: 2 Blue") == ["2 Blue"]
    assert split_games_into_sets("Game 12: 3 Green") == ["3 Green"]
    assert split_games_into_sets("Game 12: 3 Green, 2 Red") == ["3 Green, 2 Red"]
    assert split_games_into_sets("Game 100: 3 Green, 2 Red; 4 Blue") == [
        "3 Green, 2 Red",
        "4 Blue",
    ]


def test_split_sets_into_cubes():
    assert split_sets_into_cubes("3 Green, 2 Red") == ["3 Green", "2 Red"]


def test_count_cubes_of_colour_in_set():
    assert count_cubes_in_set("3 Green") == ("green", 3)


def test_is_cube_under_limit():
    cube_limit = {"green": 5, "red": 6, "blue": 7}
    assert is_cube_over_limit(("green", 3), cube_limit) == False
    assert is_cube_over_limit(("red", 7), cube_limit) == True
    assert is_cube_over_limit(("blue", 7), cube_limit) == False


def test_is_set_impossible():
    cube_limit = {"green": 5, "red": 6, "blue": 7}
    assert is_set_impossible("3 Green, 2 Red", cube_limit) == False
    assert is_set_impossible("6 Green, 2 Red", cube_limit) == True


def test_is_game_impossible():
    cube_limit = {"green": 5, "red": 6, "blue": 7}
    assert is_game_impossible("Game 100: 3 Green, 2 Red; 4 Blue", cube_limit) == False
    assert is_game_impossible("Game 100: 6 Green, 2 Red; 4 Blue", cube_limit) == True
    assert is_game_impossible("Game 100: 4 Green, 2 Red; 8 Blue", cube_limit) == True

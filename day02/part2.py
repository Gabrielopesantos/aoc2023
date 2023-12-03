from __future__ import annotations

import argparse
import os.path

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    lines = s.splitlines()
    games_score = 0
    for game in lines:
        game_id, game_data = game.split(':')
        _, game_id = game_id.split()
        game_counter = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }
        game_data += ","
        while True:
            try:
                next_comma = game_data.index(',')
            except ValueError:
                next_comma = float("inf")

            try:
                next_semi = game_data.index(';')
            except ValueError:
                next_semi = float("inf")
            next_split = min(next_comma, next_semi)
            if next_split > len(game_data):
                break

            cubes_revealed, game_data = game_data[
                :next_split +
                1
            ], game_data[next_split+1:]
            num_cubes, color = cubes_revealed.strip(",; ").split()
            game_counter[color] = max(int(num_cubes), game_counter[color])

        game_score = 1
        for game_cubes in game_counter.values():
            game_score *= game_cubes

        games_score += game_score

    return games_score


INPUT_S = '''\
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
'''
EXPECTED = 2286


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (INPUT_S, EXPECTED),
    ),
)
def test(input_s: str, expected: int) -> None:
    assert compute(input_s) == expected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f, support.timing():
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())

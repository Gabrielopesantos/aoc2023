from __future__ import annotations

import argparse
import os.path

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


# Slow
# def compute(s: str) -> int:
#     scratchcards_count = 0
#     cards = s.splitlines()
#     card_map: dict[int, str] = {}
#     for card in cards:
#         card_id, nums = card.split(':')
#         card_map[int(card_id.split()[-1])] = card
#
#     while cards:
#         scratchcards_count += 1
#
#         card_id, nums = cards.pop(0).split(':')
#         winning_numbers, numbers = nums.split('|')
#         winning_numbers = {int(x) for x in winning_numbers.split()}
#         numbers = {int(x) for x in numbers.split()}
#
#         repeats = numbers.intersection(winning_numbers)
#         card_id_number = int(card_id.split()[-1])
#         for c_id in range(card_id_number+1, card_id_number + 1 + len(repeats)):
#             card = card_map[c_id]
#             cards.insert(cards.index(card), card)
#
#     return scratchcards_count

def compute(s: str) -> int:
    cards = s.splitlines()
    card_map: dict[int, str] = {}
    card_repeat_map: dict[int, int] = {}
    for card in cards:
        card_id, nums = card.split(':')
        c_id = int(card_id.split()[-1])
        card_map[c_id] = card
        card_repeat_map[c_id] = 1

    for c_id in range(1, len(cards)):
        card_id, nums = cards.pop(0).split(':')
        winning_numbers, numbers = nums.split('|')
        winning_numbers = {int(x) for x in winning_numbers.split()}
        numbers = {int(x) for x in numbers.split()}

        repeats = numbers.intersection(winning_numbers)
        for _ in range(card_repeat_map[c_id]):
            for repeat_card_id in range(c_id+1, c_id + 1 + len(repeats)):
                card_repeat_map[repeat_card_id] += 1

    return sum(card_repeat_map.values())


INPUT_S = '''\
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
'''
EXPECTED = 30


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

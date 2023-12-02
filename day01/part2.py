from __future__ import annotations

import argparse
import os.path

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

WORDS_TO_NUMBERS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five":  5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def compute(s: str) -> int:
    values: list[int] = []
    lines = s.splitlines()
    for line in lines:
        l, r = 0, len(line)-1
        l_val, r_val = 0, 0
        while True:
            if not l_val:
                if line[l].isdigit():
                    l_val = int(line[l])
                else:
                    for word_number in WORDS_TO_NUMBERS.keys():
                        lower_bound_index = max(0, l+1-5)
                        if word_number in line[lower_bound_index:l+1]:
                            l_val = WORDS_TO_NUMBERS[word_number]
                l += 1

            if not r_val:
                if line[r].isdigit():
                    r_val = int(line[r])
                else:
                    for word_number in WORDS_TO_NUMBERS.keys():
                        upper_bound_index = min(len(line), r+5)
                        print(line, line[r-1:upper_bound_index])
                        if word_number in line[r-1:upper_bound_index]:
                            r_val = WORDS_TO_NUMBERS[word_number]
                r -= 1

            if l_val and r_val:
                break

        values.append((l_val * 10) + r_val)

    return sum(values)


INPUT_S = '''\
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
'''
EXPECTED = 281


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

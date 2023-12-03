from __future__ import annotations

import argparse
import os.path
from collections import defaultdict

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

adj = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]


def compute(s: str) -> int:
    matrix = [ch for ch in s.splitlines()]
    rows, cols = len(matrix), len(matrix[0])
    numbers = defaultdict(list)

    for r in range(rows):
        n = 0
        gears = set()
        for c in range(cols+1):
            if c < cols and matrix[r][c].isdigit():
                n = n * 10 + int(matrix[r][c])
                for off_r, off_c in adj:
                    adj_r, adj_c = r + off_r, c + off_c
                    if (
                        adj_r in range(rows) and
                        adj_c in range(cols) and
                        matrix[adj_r][adj_c] == "*"
                    ):
                        gears.add((adj_r, adj_c))
            elif n > 0:
                for gear in gears:
                    numbers[gear].append(n)
                n = 0
                gears = set()

    return sum(v[0] * v[1] for v in numbers.values() if len(v) == 2)


INPUT_S = '''\
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
'''
EXPECTED = 467835


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

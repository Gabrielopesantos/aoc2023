from __future__ import annotations

import argparse
import os.path

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

adj = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]


def compute(s: str) -> int:
    matrix = [ch for ch in s.splitlines()]
    rows, cols = len(matrix), len(matrix[0])
    numbers: list[int] = []
    seen = set()

    def bfs(r: int, c: int):
        queue = [(r, c)]
        seen.add((r, c))
        while queue:
            r, c = queue.pop(0)
            for off_r, off_c in adj:
                adj_r, adj_c = r + off_r, c + off_c
                if (
                    adj_r in range(rows) and
                    adj_c in range(cols) and
                    matrix[adj_r][adj_c].isdigit() and
                    (adj_r, adj_c) not in seen
                ):
                    queue.append((adj_r, adj_c))
                    seen.add((adj_r, adj_c))

    for r in range(rows):
        for c in range(cols):
            if (
                (r, c) not in seen and
                not matrix[r][c].isalnum() and
                matrix[r][c] != "."
            ):
                bfs(r, c)

    for r in range(rows):
        number = ""
        for c in range(cols):
            ch = matrix[r][c]
            if (r, c) in seen and ch.isdigit():
                number += ch
            elif number:
                numbers.append(int(number))
                number = ""

            if number and c == cols - 1:
                numbers.append(int(number))
                number = ""

    return sum(numbers)


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
EXPECTED = 4361


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

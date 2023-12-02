from __future__ import annotations

import argparse
import os.path

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    values: list[int] = []
    lines = s.splitlines()
    for line in lines:
        l, r = 0, len(line)-1
        l_val, r_val = 0, 0
        while l <= r:
            if line[l].isdigit():
                l_val = int(line[l])
            else:
                l += 1

            if line[r].isdigit():
                r_val = int(line[r])
            else:
                r -= 1

            if l_val and r_val:
                break
        values.append((l_val * 10) + r_val)

    return sum(values)


INPUT_S = '''\
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
'''
EXPECTED = 142


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

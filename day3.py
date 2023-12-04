#!env python3.12
# pylint: disable=missing-docstring
import re
from dataclasses import dataclass

type Schematic = list[list[str]]
type Coordinate = tuple[int, int]


@dataclass
class PartNumber:
    left: Coordinate
    right: Coordinate
    val: int


s: Schematic = []
line_in = input()
while line_in:
    s.append(line_in)
    try:
        line_in = input()
    except EOFError:
        break

parts: list[PartNumber] = []
for x, r in enumerate(s):
    for m in re.finditer(r"([0-9]+)", r):
        left = [x, m.start()]
        # end of group is one *more* than the last digit
        right = [x, m.end() - 1]
        val = int(m.group())
        parts.append(PartNumber(left, right, val))

result = 0
for p in parts:
    adjacent = False
    # y values are the same for left and right
    y_1 = max(p.left[0] - 1, 0)
    y_2 = min(p.left[0] + 1, len(s) - 1)
    x_1 = max(p.left[1] - 1, 0)
    x_2 = min(p.right[1] + 1, len(s[p.right[0]]) - 1)
    for cy in range(y_1, y_2 + 1):
        if adjacent:
            break
        for cx in range(x_1, x_2 + 1):
            sym = s[cy][cx]
            if sym != "." and not sym.isnumeric():
                adjacent = True
                break
    if adjacent:
        result += p.val

print(str(result))

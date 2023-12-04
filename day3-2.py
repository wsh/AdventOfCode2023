#!env python3.12
# pylint: disable=missing-docstring
import re
import typing
from collections import UserString
from dataclasses import dataclass

type Coordinate = tuple[int, int]


@dataclass(frozen=True)
class PartNumber:
    left: Coordinate
    right: Coordinate
    val: int


class Point(UserString):
    p: typing.Optional[PartNumber]

    def __init__(self, data: str, part: PartNumber = None):
        super().__init__(data)
        self.p = part


type Schematic = list[list[Point]]


s: Schematic = []
line_in = input()
while line_in:
    yy = [Point(v) for v in line_in]
    s.append(yy)
    try:
        line_in = input()
    except EOFError:
        break

parts: list[PartNumber] = []
for y, r in enumerate(s):
    row = "".join([us.data for us in r])
    for m in re.finditer(r"([0-9]+)", row):
        left = (m.start(), y)
        # end of group is one *more* than the last digit
        right = (m.end() - 1, y)
        val = int(m.group())
        p = PartNumber(left, right, val)
        parts.append(p)
        for xx in range(left[0], right[0] + 1):
            r[xx].p = p

potential_gears: list[Coordinate] = [
    (x, y) for (y, r) in enumerate(s) for (x, v) in enumerate(r) if v == "*"
]

ratio_sum = 0
for g in potential_gears:
    surrounding_parts = set()
    y_1 = max(g[1] - 1, 0)
    y_2 = min(g[1] + 1, len(s) - 1)
    x_1 = max(g[0] - 1, 0)
    x_2 = min(g[0] + 1, len(s[g[0]]) - 1)
    for cy in range(y_1, y_2 + 1):
        if len(surrounding_parts) > 2:
            break
        for cx in range(x_1, x_2 + 1):
            p: typing.Optional[Point] = s[cy][cx].p
            if p:
                surrounding_parts.add(p)
            if len(surrounding_parts) > 2:
                break
    if len(surrounding_parts) == 2:
        ratio_sum += surrounding_parts.pop().val * surrounding_parts.pop().val


print(str(ratio_sum))

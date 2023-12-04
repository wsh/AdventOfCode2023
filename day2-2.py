# pylint: disable=missing-docstring
import re
from collections import UserDict
from dataclasses import dataclass
from enum import Enum
from functools import reduce

Color = Enum("Color", ["RED", "GREEN", "BLUE"])


class ColorMap(UserDict[Color, int]):
    def power(self) -> int:
        return reduce(lambda x, y: x * y, self.data.values(), 1)


@dataclass
class Game:
    game_id: int
    handfuls: list[ColorMap]

    @staticmethod
    def _parse_hand(hand: str) -> ColorMap:
        ms = re.findall(r"(\d+) (\w+)", hand)
        res: ColorMap = ColorMap()
        for m in ms:
            i = int(m[0])
            c = Color[m[1].upper()]
            res[c] = i
        return res

    @staticmethod
    def parse(line: str) -> "Game":
        id_match = re.match(r"Game (\d+):", line)
        if not id_match:
            raise ValueError
        game_id = int(id_match.group(1))
        hs = line[id_match.start(1) + 1 :].split(";")
        handfuls = [Game._parse_hand(h) for h in hs]
        return Game(game_id=game_id, handfuls=handfuls)

    def minimum_set(self) -> ColorMap:
        ms = ColorMap({c: 0 for c in Color})
        for h in self.handfuls:
            for c, i in h.items():
                ms[c] = max(ms[c], i)
        return ms


out = 0
line_in = input()
while line_in:
    game = Game.parse(line_in)
    out += game.minimum_set().power()
    try:
        line_in = input()
    except EOFError:
        break

print(str(out))

# pylint: disable=missing-docstring
import re
from dataclasses import dataclass
from enum import Enum

Color = Enum("Color", ["RED", "GREEN", "BLUE"])

type ColorMap = dict[Color, int]


@dataclass
class Game:
    game_id: int
    handfuls: list[ColorMap]

    def is_possible(self, cm: ColorMap) -> bool:
        for h in self.handfuls:
            for c, i in h.items():
                x = cm.get(c)
                if not x or i > x:
                    return False
        return True


def parse_handful_from_game(hand: str) -> ColorMap:
    ms = re.findall(r"(\d+) (\w+)", hand)
    res: ColorMap = {}
    for m in ms:
        i = int(m[0])
        c = Color[m[1].upper()]
        res[c] = i
    return res


def parse_game_from_line(line: str) -> Game:
    id_s = re.match(r"Game (\d+):", line)
    if not id_s:
        raise ValueError
    game_id = int(id_s.group(1))
    hs = line[id_s.start(1) + 1 :].split(";")
    handfuls = [parse_handful_from_game(h) for h in hs]
    return Game(game_id=game_id, handfuls=handfuls)


constraint: ColorMap = {Color.RED: 12, Color.GREEN: 13, Color.BLUE: 14}
out = 0
line_in = input()
while line_in:
    game = parse_game_from_line(line_in)
    if game.is_possible(constraint):
        out += game.game_id
    try:
        line_in = input()
    except EOFError:
        break

print(str(out))

import re

ATOI = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}
REG = re.compile("(one|two|three|four|five|six|seven|eight|nine|[1-9])")


def wtoi(w):
    if w in ATOI:
        return ATOI[w]
    return w


def stoi(s):
    ns = []
    while m := re.search(REG, s):
        ns.append(str(wtoi(m.group(1))))
        s = s[m.start(1) + 1 :]
    if len(ns) == 1:
        ns.append(ns[0])
    return f"{ns[0]}{ns[len(ns)-1]}"


sum = 0
line = input()
while line:
    sum += int(stoi(line))
    try:
        line = input()
    except EOFError:
        break

print(str(sum))

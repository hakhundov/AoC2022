# AoC 2022 - Day 9 - https://adventofcode.com/2022/day/9

from aocd import get_data
data = get_data(day=9, year=2022).splitlines()

# data = []
# file = open("testInput", "r")
# for line in file:
#     data.append(line.strip())

# print(data)

Tvisited = []
Tvisited.extend([tuple([0, 0])])

HLoc = [0, 0]
TLoc = [0, 0]


def isTouching(TLoc, HLoc):
    XDelta = abs(TLoc[0] - HLoc[0])
    YDelta = abs(TLoc[1] - HLoc[1])
    delta = (XDelta + YDelta)
    if delta == 0 or delta == 1:
        return True
    elif delta == 2 and XDelta == YDelta:
        return True
    else:
        return False


def isSameRow(TLoc, HLoc):
    if (TLoc[1] == HLoc[1]):
        return True
    else:
        return False


def isSameColumn(TLoc, HLoc):
    if (TLoc[0] == HLoc[0]):
        return True
    else:
        return False


def mvUpRight(knot):
    knot[0] += 1
    knot[1] += 1


def mvUpLeft(knot):
    knot[0] -= 1
    knot[1] += 1


def mvDownRight(knot):
    knot[0] += 1
    knot[1] -= 1


def mvDownLeft(knot):
    knot[0] -= 1
    knot[1] -= 1


def mvDiag(head, tail):
    if head[0] < tail[0]:
        if head[1] < tail[1]:
            mvDownLeft(tail)
        else:
            mvUpLeft(tail)
    else:
        if head[1] < tail[1]:
            mvDownRight(tail)
        else:
            mvUpRight(tail)


def mvLateral(head, tail):
    if isSameColumn(head, tail):
        if head[1] > tail[1]:
            tail[1] += 1
        else:
            tail[1] -= 1
        return True
    elif isSameRow(head, tail):
        if head[0] > tail[0]:
            tail[0] += 1
        else:
            tail[0] -= 1
        return True
    else:
        return False  # did not mv lateral


def followHead(head, tail):
    if not isTouching(head, tail):
        if not mvLateral(head, tail):
            mvDiag(head, tail)
    return tail


def mvHead(direction, head):
    match direction:
        case 'U':
            head[1] += 1
        case 'D':
            head[1] -= 1
        case 'R':
            head[0] += 1
        case 'L':
            head[0] -= 1


for line in data:
    direction, steps = line.split(' ')
    for _ in range(int(steps)):
        mvHead(direction, HLoc)
        Tvisited.extend([tuple(followHead(HLoc, TLoc))])

print(len(set(Tvisited)))

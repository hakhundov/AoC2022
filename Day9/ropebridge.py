# AoC 2022 - Day 9 - https://adventofcode.com/2022/day/9

from aocd import get_data

def isTouching(tail, head):
    XDelta = abs(tail[0] - head[0])
    YDelta = abs(tail[1] - head[1])
    delta = (XDelta + YDelta)
    if delta == 0 or delta == 1:
        return True
    elif delta == 2 and XDelta == YDelta:
        return True
    else:
        return False


def isSameRow(tail, head):
    if (tail[1] == head[1]):
        return True
    else:
        return False


def isSameColumn(tail, head):
    if (tail[0] == head[0]):
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
        return False  # did not move laterally


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


# initialize variables

testData = []
file = open("testInput", "r")
for line in file:
    testData.append(line.strip())

data = get_data(day=9, year=2022).splitlines()

HEAD = [0, 0]

tail = []
for i in range(9):
    tail.append([0, 0])

visited1 = []
visited1.extend([tuple([0, 0])])

visited9 = []
visited9.extend([tuple([0, 0])])

# def solve(data):
for line in data:
    direction, steps = line.split(' ')
    for _ in range(int(steps)):
        mvHead(direction, HEAD)
        visited1.extend([tuple(followHead(HEAD, tail[0]))])
        for i in range(0, 8, 1):
            followHead(tail[i], tail[i+1])
        visited9.extend([tuple(followHead(tail[7], tail[8]))])

print(len(set(visited1)), len(set(visited9)))

# return[len(set(visited1)), len(set(visited9))]
# print(solve(testData))
# print(solve(data))
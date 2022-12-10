# AoC 2022 - Day 9 - https://adventofcode.com/2022/day/9

from aocd import get_data
data = get_data(day=9, year=2022).splitlines()

# data = []
# file = open("testInput", "r")
# for line in file:
#     data.append(line.strip())

# print(data)

Tvisited = []
Tvisited.extend([tuple([0,0])])
TLoc = [0, 0]
HLoc = [0, 0]

def touching(TLoc, HLoc):
    XDelta = abs(TLoc[0] - HLoc[0])
    YDelta = abs(TLoc[1] - HLoc[1])
    delta = (XDelta + YDelta)
    if delta == 0 or delta == 1:
        return True
    elif delta == 2 and XDelta == YDelta:
        return True
    else:
        return False

def sameRow(TLoc, HLoc):
    if (TLoc[1] == HLoc[1]):
        return True
    else:
        return False

def sameColumn(TLoc, HLoc):
    if (TLoc[0] == HLoc[0]):
        return True
    else:
        return False

for line in data:
    direction, steps = line.split(' ')
    for step in range(int(steps)):
        match direction:
            case 'U':
                HLoc[1] += 1
                if not touching(HLoc, TLoc):
                    if sameColumn(HLoc, TLoc):
                        TLoc[1] += 1
                        Tvisited.extend([tuple(TLoc)])
                    else:
                        if HLoc[0] < TLoc[0]:
                            TLoc[0] -= 1
                            TLoc[1] += 1
                            Tvisited.extend([tuple(TLoc)])
                        else:
                            TLoc[0] += 1
                            TLoc[1] += 1
                            Tvisited.extend([tuple(TLoc)])
            case 'D':
                HLoc[1] -= 1
                if not touching(HLoc, TLoc):
                    if sameColumn(HLoc, TLoc):
                        TLoc[1] -= 1
                        Tvisited.extend([tuple(TLoc)])
                    else:
                        if HLoc[0] < TLoc[0]:
                            TLoc[0] -= 1
                            TLoc[1] -= 1
                            Tvisited.extend([tuple(TLoc)])
                        else:
                            TLoc[0] += 1
                            TLoc[1] -= 1
                            Tvisited.extend([tuple(TLoc)])
            case 'R':
                HLoc[0] += 1
                if not touching(HLoc, TLoc):
                    if sameRow(HLoc, TLoc):
                        TLoc[0] += 1
                        Tvisited.extend([tuple(TLoc)])
                    else:
                        if HLoc[1] < TLoc[1]:
                            TLoc[0] += 1
                            TLoc[1] -= 1
                            Tvisited.extend([tuple(TLoc)])
                        else:
                            TLoc[0] += 1
                            TLoc[1] += 1
                            Tvisited.extend([tuple(TLoc)])
            case 'L':
                HLoc[0] -= 1
                if not touching(HLoc, TLoc):
                    if sameRow(HLoc, TLoc):
                        TLoc[0] -= 1
                        Tvisited.extend([tuple(TLoc)])
                    else:
                        if HLoc[1] < TLoc[1]:
                            TLoc[0] -= 1
                            TLoc[1] -= 1
                            Tvisited.extend([tuple(TLoc)])
                        else:
                            TLoc[0] -= 1
                            TLoc[1] += 1
                            Tvisited.extend([tuple(TLoc)])

print(len(set(Tvisited)))


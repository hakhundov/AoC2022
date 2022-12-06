# AoC 2022 - Day 6 - https://adventofcode.com/2022/day/6

from aocd import get_data

data = get_data(day=6, year=2022).splitlines()

def checkRepetition(inputPattern):
    if len(set(inputPattern)) != len(inputPattern):
        return True
    return False


def solve(data, markerLength):
    pattern = [x for x in data[0][:markerLength]]

    for index in range(markerLength, len(data[0])+1, 1):
        if (checkRepetition(pattern)):
            pattern = pattern[1:] + [data[0][index]]
        else:
            break
    return index


print(solve(data, 4))
print(solve(data, 14))

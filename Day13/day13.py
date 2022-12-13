# AoC 2022 - Day 13 - https://adventofcode.com/2022/day/13

from aocd import get_data
import re
import math
import queue
from pprint import pprint

data = get_data(day=13, year=2022).splitlines()
# data = []
# with open("testInput", "r") as file:
#     for line in file:
#         data.append(line.strip())  # unpack

left = []
right = []

dataIter = iter(data)

for message in dataIter:
    left.append(eval(message))
    right.append(eval(next(dataIter)))
    try:
        next(dataIter)
    except StopIteration:
        break

def sameType(a, b):
    return type(a) == type(b)

def recurCompare(left: list, right: list):
    while len(left) > 0 and len(right) > 0:
        if left[0] == right[0]:
            left.pop(0)
            right.pop(0)
        elif type(left[0]) != type(right[0]):
            if isinstance(left[0], int):
                left[0] = [left[0]]
            else:
                right[0] = [right[0]]
        elif isinstance(left[0], int) and isinstance(right[0], int):
            if left[0] < right[0]:
                return 1
            else:
                return 0
        elif isinstance(left[0], list) and isinstance(right[0], list):
            if len(left[0]) == 0:
                return 1
            elif len(right[0]) == 0:
                return 0
            else:
                if recurCompare(left[0], right[0]) == 1:
                    return 1
                else:
                    return 0
        else:
            return 0
    else:
        if len(left) == 0:
            return 1
        else:
            return 0

rightOrder = 0
for i in range(len(left)):
    rightOrder += (i+1) * recurCompare(left[i], right[i])


print(rightOrder)
# 5506 is the answer!
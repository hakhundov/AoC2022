# AoC 2022 - Day 12 - https://adventofcode.com/2022/day/12

from aocd import get_data
import re
import math
import queue

data = get_data(day=12, year=2022).splitlines()
testData = []
with open("testInput", "r") as file:
    for line in file:
        testData.append(line.strip())  # unpack

row_len = len(data)
col_len = len(data[0])
print(row_len, col_len)

def canMove(fr, to):
    if (ord(to) - ord(fr)) > 1:
        return False
    else:
        return True


def getNeighbors(row, col, row_len, col_len):
    neighbors = []
    if row > 0:
        above = (row-1, col)
        neighbors.append(above)
    if row < row_len - 1:
        below = (row+1, col)
        neighbors.append(below)
    if col > 0:
        left = (row, col-1)
        neighbors.append(left)
    if col < col_len - 1:
        right = (row, col+1)
        neighbors.append(right)
    return neighbors

def findStart(data):
    for i in range(len(data)):
        if (j := data[i].find('S')) != -1:
            return (i, j)

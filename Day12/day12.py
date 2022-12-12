# AoC 2022 - Day 12 - https://adventofcode.com/2022/day/12

from aocd import get_data
import re
import math
import queue

# data = get_data(day=12, year=2022).splitlines()
data = []
with open("testInput", "r") as file:
    for line in file:
        data.append(line.strip())  # unpack

row_len = len(data)
col_len = len(data[0])
print(row_len, col_len)

def canMove(fr, to):
    if fr == 'S':
        return True
    elif (ord(to) - ord(fr)) > 1:
        return False
    else:
        return True


def getNeighbors(data, row, col, row_len, col_len):
    allNeighbors = []
    if row > 0:
        above = (row-1, col)
        allNeighbors.append(above)
    if row < row_len - 1:
        below = (row+1, col)
        allNeighbors.append(below)
    if col > 0:
        left = (row, col-1)
        allNeighbors.append(left)
    if col < col_len - 1:
        right = (row, col+1)
        allNeighbors.append(right)

    filtered = [n for n in allNeighbors if canMove(data[row][col], data[n[0]][n[1]])]
    return filtered

def findStart(data):
    for i in range(len(data)):
        if (j := data[i].find('S')) != -1:
            return (i, j)


start = findStart(data)
print(start)

frontier = queue.Queue()
# reached = []
frontier.put(start)
# reached.append(start)
came_from = dict()
came_from[start] = None

# count = 0
while not frontier.empty():
    current = frontier.get()
    # count += 1
    for next in getNeighbors(current[0], current[1]):
        if next not in came_from:
            frontier.put(next)
            came_from[next] = current
            # reached.append(next)
# implement early exit


print(came_from)
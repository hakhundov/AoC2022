# AoC 2022 - Day 5 - https://adventofcode.com/2022/day/5

from aocd import get_data
from aocd import submit
import re

data = get_data(day=5, year=2022).splitlines()

for count, line in enumerate(data):
    if line == '':
        break

totalStacks = re.findall(r"\d+(?!\d+)", data[count-1])[-1]
allStacks = [[] for i in range(count)]   

for x in range(count-2, -1, -1): #upside down stack
    cursor = 1
    for stack in range(int(totalStacks)): # counting from 0
        item = data[x][cursor]
        if item != ' ':
            allStacks[stack].append(item)
        cursor += 4

for line in range(count+1, len(data), 1):
    matches = [int(n) for n in re.findall(r"-?\d+", data[line])]
    for _ in range(matches[0]):
        allStacks[matches[2]-1].append(allStacks[matches[1]-1].pop()) # indexing starts at 0, hence -1

for x in range(len(allStacks)):
    print(allStacks[x][-1], end="")
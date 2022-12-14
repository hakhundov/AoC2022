# AoC 2022 - Day 14 - https://adventofcode.com/2022/day/14

from aocd import get_data
import copy
from functools import cmp_to_key
from pprint import pprint

# data = get_data(day=14, year=2022).splitlines()
data = []
with open("testInput", "r") as file:
    for line in file:
        data.append(line.strip())  # unpack
print(data)

scanData = []

for line in data:
    splitLine = [x.strip() for x in line.split('->')]
    splitFurther = [(int(x.split(',')[0]), int(x.split(',')[1]))
                    for x in splitLine]
    scanData.append(splitFurther)

min_x = 1000
min_y = 0
max_x = 0
max_y = 0

for line in scanData:
    for coordinate in line:
        if coordinate[0] < min_x:
            min_x = coordinate[0]
        if coordinate[0] > max_x:
            max_x = coordinate[0]
        if coordinate[1] > max_y:
            max_y = coordinate[1]
print(min_x, max_x, min_y, max_y)

cave = [ ['.'] * (max_x-min_x+1) for i in range(max_y-min_y+1)]

for line in scanData:
    for i in range(len(line)-1):
        pointA = (line[i][0]-min_x, line[i][1])
        pointB = (line[i+1][0]-min_x, line[i+1][1])

        k1 = 1 if pointB[0] - pointA[0] >= 0 else -1
        for x in range(pointA[0], pointB[0]+k1, k1):
            k2 = 1 if pointB[1] - pointA[1] >= 0 else -1
            for y in range(pointA[1], pointB[1]+k2, k2):
                cave[y][x] = '#'

sandStart = 500 - min_x
atRestCount = 0

# abyss = False
# while not abyss:
while True:
    sandPosition = [0,sandStart]
    atRest = False
    try:
        while not atRest:
            if sandPosition[1] > max_y:
                abyss = True
                break
            if cave[ sandPosition[0]+1 ][ sandPosition[1] ] == '.':
                sandPosition[0] += 1
                continue
            elif cave[ sandPosition[0]+1 ][ sandPosition[1] ] != '.': # i.e., # or o
                # attempt left
                if cave[ sandPosition[0]+1 ][ sandPosition[1]-1 ] == '.':
                    sandPosition[0] += 1
                    sandPosition[1] -= 1
                    continue
                # attempt right
                elif cave[ sandPosition[0]+1 ][ sandPosition[1]+1 ] == '.':
                    sandPosition[0] += 1
                    sandPosition[1] += 1
                    continue
                else: # rest
                    atRest = True
                    atRestCount += 1
                    cave[ sandPosition[0] ][ sandPosition[1] ] = 'o'
    except:
        break    

print(atRestCount)
# AoC 2022 - Day 18 - https://adventofcode.com/2022/day/18

from aocd import get_data

data = get_data(day=18, year=2022).splitlines()

testData = []
with open("testInput", "r") as file:
    for line in file:
        testData.append(line.strip())

cubes = []
for line in data:
    point = [int(x) for x in line.split(',')]
    cubes.append(point)

def neighbors(x, y, z):
    for px, py, pz in [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]:
        yield [x + px, y + py, z + pz]

exposedEdges = 0
for cube in cubes:
    for neighbor in neighbors(cube[0], cube[1], cube[2]):
        if neighbor not in cubes:
            print(neighbor)
            exposedEdges += 1
        else:
            print (neighbor)
print(exposedEdges)




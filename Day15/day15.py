# AoC 2022 - Day 15 - https://adventofcode.com/2022/day/15

from aocd import get_data
from functools import cmp_to_key
from pprint import pprint
from pixelscan import manhattan, ringscan
import re

data = get_data(day=15, year=2022).splitlines()

# data = []
# with open("testInput", "r") as file:
#     for line in file:
#         data.append(line.strip())

beaconNotPresent = set()
beacons = set()

sbdata = []
for line in data:
    matches = [int(n) for n in re.findall(r"-?\d+", line)]
    sensor = [matches[0], matches[1]]
    beacon = [matches[2], matches[3]]
    beacons.add((matches[2], matches[3]))
    d = manhattan(sensor, beacon)
    sbdata.append([sensor, beacon, d])
    # for x, y in ringscan(matches[0], matches[1], 0, d, metric=manhattan):
        # beaconNotPresent.add((x,y))
# pprint(sbdata)

leftMostReach = min([x[0][0] - x[2] for x in sbdata])
# print(leftMostReach)
rightMostReach = max([x[0][0] + x[2] for x in sbdata])
# print(rightMostReach)


# beaconNotPresent -= beacons
# count = 0
# y = 10
# for point in beaconNotPresent:
#     if point[1] == y:
#         # print(point)
#         count += 1
# print(count)

# -- way 2

# y = 10
y=2000000
# count = 0
newset = set()

for x in range(leftMostReach, rightMostReach+1, 1):
    point = [x, y]
    for s in sbdata:
        if manhattan(point, s[0]) <= s[2]:
            # print(point)
            newset.add((point[0], point[1]))
            # count +=1
            break
print(len(newset-beacons))
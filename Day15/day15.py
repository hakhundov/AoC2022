# AoC 2022 - Day 15 - https://adventofcode.com/2022/day/15

from aocd import get_data
import copy
from functools import cmp_to_key
from pprint import pprint
from pixelscan import manhattan, ringscan
import re
import multiprocessing

data = get_data(day=15, year=2022).splitlines()

# data = []
# with open("testInput", "r") as file:
#     for line in file:
#         data.append(line.strip())

beaconNotPresent = set()
beacons = set()

sbdata = []
for line in data:
    print(line)
    matches = [int(n) for n in re.findall(r"-?\d+", line)]
    sensor = [matches[0], matches[1]]
    beacon = [matches[2], matches[3]]
    beacons.add((matches[2], matches[3]))
    d = manhattan(sensor, beacon)
    sbdata.append[sensor, beacon, d]
    for x, y in ringscan(matches[0], matches[1], 0, d, metric=manhattan):
        beaconNotPresent.add((x,y))
print(sbdata)

beaconNotPresent -= beacons
count = 0
y = 2000000
for point in beaconNotPresent:
    if point[1] == y:
        print(point)
        count += 1
print(count)
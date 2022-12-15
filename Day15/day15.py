# AoC 2022 - Day 15 - https://adventofcode.com/2022/day/15

from aocd import get_data
from functools import cmp_to_key
from pprint import pprint
from pixelscan import manhattan, ringscan
import re

data = get_data(day=15, year=2022).splitlines()

testData = []
with open("testInput", "r") as file:
    for line in file:
        testData.append(line.strip())

def processSensorBeaconData(data):
    beacons = set()
    sbdata = []
    for line in data:
        matches = [int(n) for n in re.findall(r"-?\d+", line)]
        sensor = [matches[0], matches[1]]
        beacon = [matches[2], matches[3]]
        beacons.add((matches[2], matches[3]))
        d = manhattan(sensor, beacon)
        sbdata.append([sensor, beacon, d])

    leftMostReach = min([x[0][0] - x[2] for x in sbdata])
    rightMostReach = max([x[0][0] + x[2] for x in sbdata])
    topMostReach = min([x[0][1] - x[2] for x in sbdata])
    bottomMostReach = max([x[0][1] + x[2] for x in sbdata])
    return beacons,sbdata,leftMostReach,rightMostReach,topMostReach,bottomMostReach


def countNoBeacons(beacons, sbdata, leftMostReach, rightMostReach, y):
    beaconNotPresent = set()
    for x in range(leftMostReach, rightMostReach+1, 1):
        point = [x, y]
        for s in sbdata:
            if manhattan(point, s[0]) <= s[2]:
                beaconNotPresent.add((point[0], point[1]))
                break
    return len(beaconNotPresent-beacons)


def solve(data, y):
    beacons, sbdata, leftMostReach, rightMostReach, _, _ = processSensorBeaconData(data)
    print(countNoBeacons(beacons, sbdata, leftMostReach, rightMostReach, y))

solve(data, 2000000)
solve(testData, 10)
#4424278
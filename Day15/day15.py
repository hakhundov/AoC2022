# AoC 2022 - Day 15 - https://adventofcode.com/2022/day/15

from aocd import get_data
# from pixelscan import manhattan, ringscan
import re

data = get_data(day=15, year=2022).splitlines()

testData = []
with open("testInput", "r") as file:
    for line in file:
        testData.append(line.strip())


def manhattan(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

def processSensorBeaconData(data):
    beacons = set()
    sensorData = []
    for line in data:
        matches = [int(n) for n in re.findall(r"-?\d+", line)]
        sensor = [matches[0], matches[1]]
        beacon = [matches[2], matches[3]]
        beacons.add((matches[2], matches[3]))
        distance = manhattan(sensor, beacon)
        sensorData.append([sensor, beacon, distance])

    leftMostReach = min([x[0][0] - x[2] for x in sensorData])
    rightMostReach = max([x[0][0] + x[2] for x in sensorData])
    topMostReach = min([x[0][1] - x[2] for x in sensorData])
    bottomMostReach = max([x[0][1] + x[2] for x in sensorData])
    return beacons, sensorData, leftMostReach, rightMostReach, topMostReach, bottomMostReach


def countNoBeacons(beacons, sensorData, leftMostReach, rightMostReach, y):
    beaconNotPresent = set()
    for x in range(leftMostReach, rightMostReach+1, 1):
        point = [x, y]
        for s in sensorData:
            if manhattan(point, s[0]) <= s[2]:
                beaconNotPresent.add((point[0], point[1]))
                break
    return len(beaconNotPresent-beacons)


def solve(data, y):
    beacons, sensorData, leftMostReach, rightMostReach, _, _ = processSensorBeaconData(
        data)
    print(countNoBeacons(beacons, sensorData, leftMostReach, rightMostReach, y))

# solve(data, 2000000)
# solve(testData, 10)
# part 1 4424278
# part 2 10382630753392


def getRanges(sensorData, row):
    rowRanges = []
    for sensor in sensorData:
        d = sensor[2] - abs(row - sensor[0][1])
        if d >= 0:  # there is overlap
            rowRanges.append((sensor[0][0] - d, sensor[0][0] + d))
    return sorted(rowRanges)

_, sensorData, _, _, _, _ = processSensorBeaconData(data)
# print(getRanges(sensorData, 10))

def findGapInRanges(ranges):
    highest = 0
    for (a, b) in ranges:
        if a <= highest+1:
            highest = max(b, highest)
        else:
            return a-1

for row in range (4000000):
    ranges = getRanges(sensorData, row)
    if index := findGapInRanges(ranges):
        print(index*4000000 + row)

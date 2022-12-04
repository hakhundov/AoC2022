# AoC 2022 - Day 4 - https://adventofcode.com/2022/day/4

def solveDay4(inputFilename):
    fullOverlaps = 0  # subset
    noOverlaps = 0  # disjoint

    with open(inputFilename, "r") as file:
        for count, line in enumerate(file):
            sections = [x.split('-') for x in line.strip().split(',')]
            ranges = [int(val) for sublist in sections for val in sublist]
            range1 = set(range(ranges[0], ranges[1] + 1))
            range2 = set(range(ranges[2], ranges[3] + 1))
            if not range1 - range2 or not range2 - range1:
                fullOverlaps += 1
            if not (range1 & range2):
                noOverlaps += 1
    return [fullOverlaps, count - noOverlaps + 1]


print(solveDay4("input"))

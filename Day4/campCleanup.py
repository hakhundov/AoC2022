# AoC 2022 - Day 4 - https://adventofcode.com/2022/day/4

# Part 1

def solvePart1(inputFilename):
    overlaps = 0
    with open(inputFilename, "r") as file:
        for line in file:
            sections = [x.split('-') for x in line.strip().split(',')]
            ranges = [int(val) for sublist in sections for val in sublist]
            range1 = set(range(ranges[0], ranges[1] + 1))
            range2 = set(range(ranges[2], ranges[3] + 1))

            if not range1 - range2 or not range2 - range1:
                overlaps += 1
    return overlaps

print(solvePart1("input"))


# Part 2

def solvePart2(inputFilename):
    overlaps = 0
    with open(inputFilename, "r") as file:
        for line in file:
            sections = [x.split('-') for x in line.strip().split(',')]
            ranges = [int(val) for sublist in sections for val in sublist]
            range1 = set(range(ranges[0], ranges[1] + 1))
            range2 = set(range(ranges[2], ranges[3] + 1))

            if not range1 - range2 or not range2 - range1:
                overlaps += 1
    return overlaps

print(solvePart1("input"))
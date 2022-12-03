# AoC 2022 - Day 3 - Rucksack Reorganization

# Part 1
def getPriority(item):
    return (ord(item) - 96) if item.islower() else (ord(item) - 38)

def solvePart1(inputFilename):
    sumOfPriorities = 0

    with open(inputFilename, "r") as file:
        for line in file:
            firstCompartment = set(line[:len(line)//2].strip())
            secondCompartment = set(line[len(line)//2:].strip())
            sharedItem = ''.join(firstCompartment.intersection(secondCompartment))
            sumOfPriorities += getPriority(sharedItem)

    return sumOfPriorities

# Part 2
def solvePart2(inputFilename):
    sumOfPriorities = 0

    with open(inputFilename, "r") as file:
        for line in file:
            commonItem = ''.join( set(line.strip()) & set(next(file).strip()) & set(next(file).strip()) )
            sumOfPriorities += getPriority(commonItem)
    return sumOfPriorities

print("Part 1 answer: " + str(solvePart1("input")))
print("Part 2 answer: " + str(solvePart2("input")))
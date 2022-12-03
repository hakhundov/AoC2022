# AoC 2022 - Day 3 - Rucksack Reorganization

# Part 1

def getPriority(item):
    return (ord(item) - 96) if item.islower() else (ord(item) - 38)

def solvePart1(inputFilename):
    file = open(inputFilename, "r")
    sumOfPriorities = 0

    for line in file:
        firstCompartment = set(line[:len(line)//2].strip())
        secondCompartment = set(line[len(line)//2:].strip())
        sharedItem = ''.join(firstCompartment.intersection(secondCompartment))
        sumOfPriorities += getPriority(sharedItem)

    return sumOfPriorities

# Part 2
def solvePart2():
    file.seek(0)
    sumOfPriorities = 0

    for line in file:
        commonItem = ''.join( set(line.strip()) & set(next(file).strip()) & set(next(file).strip()) )
        sumOfPriorities += (ord(commonItem) - 96) if commonItem.islower() else (ord(commonItem) - 38)
    return sumOfPriorities

# print(sumOfPriorities)

# if (sumOfPriorities == 2585):
#     print('PASSED!')
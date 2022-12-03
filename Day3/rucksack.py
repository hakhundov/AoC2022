# AoC 2022 - Day 3 - Rucksack Reorganization

file = open("input", "r")
sumOfPriorities = 0

for line in file:
    firstCompartment = set(line[:len(line)//2].strip())
    secondCompartment = set(line[len(line)//2:].strip())    
    sharedItem = ''.join(firstCompartment.intersection(secondCompartment))
    sumOfPriorities += (ord(sharedItem) - 96) if sharedItem.islower() else (ord(sharedItem) - 38)

print(sumOfPriorities)
if (sumOfPriorities == 7917):
    print('PASSED!')
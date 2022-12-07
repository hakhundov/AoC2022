# AoC 2022 - Day 7 - https://adventofcode.com/2022/day/7

from aocd import get_data

data = get_data(day=7, year=2022).splitlines()

# data = []
# with open("testInput", "r") as file:
#     for line in file:
#         data.append(''.join(line.splitlines()))

totalSum = 0
stack = []
stack.append(0)
currentSize = 0
dirSizes = []

for line in data:
    tokens = line.strip().split(' ')
    match tokens[0]:
        case '$':
            match tokens[1]:
                case 'cd':
                    if (tokens[2] == '..'):  # up directory
                        stack[-1] += currentSize
                        currentSize = 0
                        if (size := stack.pop()) <= 100000:
                            totalSum += size
                        dirSizes.append(size)  # added for part 2
                        stack[-1] += size  # parent also inherits size
                    else:  # down directory
                        stack[-1] += currentSize
                        currentSize = 0
                        stack.append(0)
                case 'ls':
                    pass
        case 'dir':
            pass
        case _:
            currentSize += int(tokens[0])

# part 1 answer
print(totalSum)

totalSize = sum(stack) + currentSize
unusedSpace = 70000000 - totalSize
stillRequired = 30000000 - unusedSpace
dirSizes.sort()
# part 2 answer
print([i for i in dirSizes if i > stillRequired][0])

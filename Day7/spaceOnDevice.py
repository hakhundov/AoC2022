# AoC 2022 - Day 7 - https://adventofcode.com/2022/day/7

def solve(data):
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

    # unwind stack
    while (len(stack) > 1):
        stack[-1] += currentSize
        currentSize = 0
        if (size := stack.pop()) <= 100000:
            totalSum += size
        dirSizes.append(size)  # added for part 2
        stack[-1] += size  # parent also inherits size

    totalSize = sum(stack)
    unusedSpace = 70000000 - totalSize
    stillRequired = 30000000 - unusedSpace
    dirSizes.sort()
    spaceToFree = [i for i in dirSizes if i > stillRequired][0]

    return [totalSum, spaceToFree]

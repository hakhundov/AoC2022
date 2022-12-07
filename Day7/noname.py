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

collect = []

with open("testInput", "r") as file:
    for line in file:
        tokens = line.strip().split(' ')
        print(tokens)
        match tokens[0]:
            case '$':
                match tokens[1]:
                    case 'cd':
                        if (tokens[2] == '..'):
                            stack[-1] += currentSize
                            print('Stack just before popping! -->' , stack)
                            currentSize = 0
                            if (size := stack.pop()) <= 100000:
                                print ('inside if statment, size = ', size)
                                totalSum += size
                                collect.append(size)
                            stack[-1] += size # parent also inherits size
                            #do things with stack, size and current max
                        else: #this means we are entering a new dir
                            print('entering a new dir ' + tokens [2])
                            stack[-1] += currentSize
                            currentSize = 0
                            stack.append(0)
                            
                    case 'ls':
                        pass #safely ignore this block
            case 'dir':
                pass #safely ignore this block

            case _: #let's calculate the size!
                currentSize += int(tokens[0])

        # print('Current state')
        print('Stack = ' ,stack)
        print('Current size = ', currentSize)
        print('total sum =', totalSum)
        print('collect --> ', collect)
        print(' ')
print(totalSum)

# print(data)



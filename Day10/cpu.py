# AoC 2022 - Day 10 - https://adventofcode.com/2022/day/10

from aocd import get_data
data = get_data(day=10, year=2022).splitlines()
# print(data)

testData = []
with open("testInput","r") as file:
    for line in file:
        testData.append(line.strip())  # unpack
# print(testData)

dict = {}
register_x = 1
cycle = 0
stack = []
CRT_output =""

for line in data:
    instuction = line.strip()

    match instuction:
        case 'noop':
            cycle += 1
            if (len(stack) != 0):
                register_x += stack.pop()

            if ((cycle-1) % 40 in range(register_x-1, register_x+2, 1)):
                CRT_output += "#"
            else:
                CRT_output += "."


            dict[cycle] = register_x
        case _:
            addx_v = int(line.split(' ')[1])

            cycle += 1
            if (len(stack) != 0):
                register_x += stack.pop()
            dict[cycle] = register_x

            if ((cycle-1) % 40 in range(register_x-1, register_x+2, 1)):
                CRT_output += "#"
            else:
                CRT_output += "."

            cycle += 1
            if (len(stack) != 0):
                register_x += stack.pop()
            dict[cycle] = register_x

            if ((cycle-1) % 40 in range(register_x-1, register_x+2, 1)):
                CRT_output += "#"
            else:
                CRT_output += "."

            stack.append(addx_v)

sum = 0
for i in range(20, 241, 40):
    sum += i * dict[i]
print(sum)

for index, char in enumerate(CRT_output):
    print(char, end='')
    if ((index+1) % 40 == 0):
        print('')
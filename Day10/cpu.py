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

for line in data:
    instuction = line.strip()

    match instuction:
        case 'noop':
            cycle += 1
            if (len(stack) != 0):
                register_x += stack.pop()
            dict[cycle] = register_x
        case _:
            addx_v = int(line.split(' ')[1])
            cycle += 1
            if (len(stack) != 0):
                register_x += stack.pop()
            dict[cycle] = register_x
            cycle += 1
            if (len(stack) != 0):
                register_x += stack.pop()
            dict[cycle] = register_x
            stack.append(addx_v)

sum = 0
for i in range(20, 241, 40):
    sum += i * dict[i]
print(sum)

# part 1
# test  = 13140
# real = 13520



# AoC 2022 - Day 11 - https://adventofcode.com/2022/day/11

from aocd import get_data
data = get_data(day=11, year=2022).splitlines()
# print(data)

testData = []
with open("testInput","r") as file:
    for line in file:
        testData.append(line.strip())  # unpack
# print(testData)


for line in data:
    instuction = line.strip()

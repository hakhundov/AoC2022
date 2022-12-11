# AoC 2022 - Day 12 - https://adventofcode.com/2022/day/12

from aocd import get_data
import re
import math

data = get_data(day=12, year=2022).splitlines()
testData = []
with open("testInput", "r") as file:
    for line in file:
        testData.append(line.strip())  # unpack


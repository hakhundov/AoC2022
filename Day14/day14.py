# AoC 2022 - Day 14 - https://adventofcode.com/2022/day/14

from aocd import get_data
import copy
from functools import cmp_to_key


# data = get_data(day=14, year=2022).splitlines()
data = []
with open("testInput", "r") as file:
    for line in file:
        data.append(line.strip())  # unpack

print(data)
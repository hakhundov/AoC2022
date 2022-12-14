# AoC 2022 - Day 15 - https://adventofcode.com/2022/day/15

from aocd import get_data
import copy
from functools import cmp_to_key
from pprint import pprint

# data = get_data(day=15, year=2022).splitlines()

data = []
with open("testInput", "r") as file:
    for line in file:
        data.append(line.strip())
print(data)
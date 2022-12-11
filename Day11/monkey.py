# AoC 2022 - Day 11 - https://adventofcode.com/2022/day/11

from aocd import get_data
import re
import math

data = get_data(day=11, year=2022).splitlines()
testData = []
with open("testInput", "r") as file:
    for line in file:
        testData.append(line.strip())  # unpack


class Monkey(object):
    inspected = 0

    def __init__(self, items, operation, div, passToTrue, passToFalse):
        self.items = items
        self.operation = eval("lambda old: " + operation)
        self.divisor = div
        self.passToTrue = passToTrue
        self.passToFalse = passToFalse

    def addItem(self, item):
        self.items.append(item)


def readMonkeyData(input):
    dataIter = iter(input)

    monkeys = []
    for line in dataIter:
        # skip 'Monkey 0'
        items = [int(n) for n in re.findall(r"-?\d+", next(dataIter))]
        operation = next(dataIter).split('=')[-1]
        divisor = int(next(dataIter).split(' ')[-1])
        passToTrue = int(next(dataIter).split(' ')[-1])
        passToFalse = int(next(dataIter).split(' ')[-1])
        monkeys.append(
            Monkey(items, operation, divisor, passToTrue, passToFalse))
        try:
            next(dataIter)  # skip line
        except StopIteration:
            break
    return monkeys

# solve


def playKeepAway(data, rounds, decreaseWorryLevel):
    monkeys = readMonkeyData(data)
    lcm = math.lcm(*[monkey.divisor for monkey in monkeys])

    for _ in range(rounds):
        for monkey in monkeys:
            for item in monkey.items:
                monkey.inspected += 1
                worryLevel = (monkey.operation(item))
                worryLevel = worryLevel // 3 if decreaseWorryLevel else (
                    worryLevel % lcm)
                if (worryLevel % monkey.divisor == 0):
                    monkeys[monkey.passToTrue].addItem(worryLevel)
                else:
                    monkeys[monkey.passToFalse].addItem(worryLevel)
            monkey.items.clear()

    inspected = [monkey.inspected for monkey in monkeys]
    inspected.sort()
    monkeyBusiness = inspected[-1] * inspected[-2]
    return monkeyBusiness


# rounds = 10000
# decreaseWorryLevel = False
# monkeyBusiness = playKeepAway(data, rounds, decreaseWorryLevel)
# print(monkeyBusiness)

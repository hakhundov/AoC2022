# AoC 2022 - Day 11 - https://adventofcode.com/2022/day/11

from aocd import get_data
import re
import math

data = get_data(day=11, year=2022).splitlines()
testData = []
with open("testInput", "r") as file:
    for line in file:
        testData.append(line.strip())  # unpack
print(testData)


class Monkey(object):
    inspected = 0

    def __init__(self, items, operation, div, passToTrue, passToFalse):
        self.items = items
        self.operation = eval("lambda old: " + operation)
        self.divisor = div
        self.passToTrue = passToTrue
        self.passToFalse = passToFalse


def getMonkeys(input):
    dataIter = iter(input)

    monkeys = []
    for line in dataIter:
        # skip 'Monkey 0'
        items = [int(n) for n in re.findall(r"-?\d+", next(dataIter))]
        operation = (re.findall(r"\=(.*)", next(dataIter)))[0].strip()
        divisor = [int(n) for n in re.findall(r"-?\d+", next(dataIter))][0]
        passToTrue = [int(n) for n in re.findall(r"-?\d+", next(dataIter))][0]
        passToFalse = [int(n) for n in re.findall(r"-?\d+", next(dataIter))][0]
        # print(items, operation, test, passToTrue, passToFalse)
        monkeys.append(Monkey(items, operation, divisor, passToTrue, passToFalse))
        try:
            next(dataIter)  # skip line
        except StopIteration:
            break
    return monkeys


# solve

rounds = 10000
monkeys = getMonkeys(data)
decreaseWorryLevel = False

lcm = math.lcm(*[monkey.divisor for monkey in monkeys])

print(lcm)

for round in range(rounds):
    for monkey in monkeys:
        operation = monkey.operation
        for item in monkey.items:
            monkey.inspected += 1
            worry_level = (monkey.operation(item))
            worry_level = worry_level // 3 if decreaseWorryLevel else (worry_level % lcm)
            if (worry_level % monkey.divisor == 0):
                monkeys[monkey.passToTrue].items.append(worry_level)
            else:
                monkeys[monkey.passToFalse].items.append(worry_level)
        monkey.items.clear()

    # for i, monkey in enumerate(monkeys):
    #     print("Monkey ", i, " ", monkey.items)


inspected = [monkey.inspected for monkey in monkeys]
inspected.sort()
print(inspected)
monkeyBusiness = inspected[-1] * inspected[-2]
print(monkeyBusiness)

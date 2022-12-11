# AoC 2022 - Day 11 - https://adventofcode.com/2022/day/11

from aocd import get_data
import re
data = get_data(day=11, year=2022).splitlines()
# print(data)

testData = []
with open("testInput","r") as file:
    for line in file:
        testData.append(line.strip())  # unpack
print(testData)

class Monkey(object):
    inspected = 0
    def __init__(self, items, operation, test, passToTrue, passToFalse):
        self.items = items
        self.operation = eval("lambda old: " + operation)
        self.test = test
        self.passToTrue = passToTrue
        self.passToFalse = passToFalse


def getMonkeys( input ):
    dataIter = iter(input)
    
    monkeys = []
    for line in dataIter:
        # skip 'Monkey 0'
        items = [int(n) for n in re.findall(r"-?\d+", next(dataIter))]
        operation = (re.findall(r"\=(.*)", next(dataIter)))[0].strip()
        test = [int(n) for n in re.findall(r"-?\d+", next(dataIter))][0]
        passToTrue = [int(n) for n in re.findall(r"-?\d+", next(dataIter))][0]
        passToFalse = [int(n) for n in re.findall(r"-?\d+", next(dataIter))][0]
        # print(items, operation, test, passToTrue, passToFalse)
        monkeys.append(Monkey(items, operation, test, passToTrue, passToFalse))
        try:
            next(dataIter) # skip line
        except StopIteration:
            break
    return monkeys

monkeys = getMonkeys(testData)

for round in range(20):
    for monkey in monkeys:
        operation = monkey.operation
        for item in monkey.items:
            monkey.inspected += 1
            worry_level = (monkey.operation(item)) // 3
            if (worry_level % monkey.test == 0):
                monkeys[monkey.passToTrue].items.append(worry_level)
            else:
                monkeys[monkey.passToFalse].items.append(worry_level)
        monkey.items.clear()
    
    for i, monkey in enumerate(monkeys):
        print("Monkey ", i, " ", monkey.items)


inspected = [monkey.inspected for monkey in monkeys].sort()
print(inspected)
# print (monkeys[0].items)
# load all monkeys
# monkeys.append(Monkey([79, 98], "old * 19", 23, 2, 3))
# print(monkeys[0].operation(2))
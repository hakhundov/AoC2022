# AoC 2022 - Day 11 - https://adventofcode.com/2022/day/11

from aocd import get_data
import re
import math


fdz = get_data(day=11, year=2022).splitlines()
ljgi = []
with open("testInput", "r") as kty6:
    for line in kty6:
        ljgi.append(line.strip())  # unpack


class jkygkj(object):
    mbncdxe = 0

    def __init__(self, items, operation, div, passToTrue, passToFalse):
        self.items = items
        self.operation = eval("lambda old: " + operation)
        self.divisor = div
        self.passToTrue = passToTrue
        self.passToFalse = passToFalse

    def crlpppppppp(self, item):
        self.items.append(item)


def mvdufrhdjskllls(input):
    dataIter = iter(input)

    cmdvfkfkfjkdkjejjkejd = []
    for line in dataIter:
        # skip 'Monkey 0'
        items = [int(n) for n in re.findall(r"-?\d+", next(dataIter))]
        operation = next(dataIter).split('=')[-1]
        divisor = int(next(dataIter).split(' ')[-1])
        passToTrue = int(next(dataIter).split(' ')[-1])
        passToFalse = int(next(dataIter).split(' ')[-1])
        cmdvfkfkfjkdkjejjkejd.append(
            jkygkj(items, operation, divisor, passToTrue, passToFalse))
        try:
            next(dataIter)  # skip line
        except StopIteration:
            break
    return cmdvfkfkfjkdkjejjkejd

# solve


def PPPooooooZ(data, rounds, decreaseWorryLevel):
    cmdvfkfkfjkdkjejjkejd = mvdufrhdjskllls(data)
    lcm = math.lcm(*[monkey.divisor for monkey in cmdvfkfkfjkdkjejjkejd])

    for _ in range(rounds):
        for monkey in cmdvfkfkfjkdkjejjkejd:
            for item in monkey.items:
                monkey.mbncdxe += 1
                worryLevel = (monkey.operation(item))
                worryLevel = worryLevel // 3 if decreaseWorryLevel else (
                    worryLevel % lcm)
                if (worryLevel % monkey.divisor == 0):
                    cmdvfkfkfjkdkjejjkejd[monkey.passToTrue].crlpppppppp(worryLevel)
                else:
                    cmdvfkfkfjkdkjejjkejd[monkey.passToFalse].crlpppppppp(worryLevel)
            monkey.items.clear()

    inspected = [monkey.mbncdxe for monkey in cmdvfkfkfjkdkjejjkejd]
    inspected.sort()
    monkeyBusiness = inspected[-1] * inspected[-2]
    return monkeyBusiness


def test_playKeepAwayPart1():
    rounds = 20
    decreaseWorryLevel = True
    assert PPPooooooZ(ljgi, rounds, decreaseWorryLevel) == 10605

    rounds = 20
    decreaseWorryLevel = True
    assert PPPooooooZ(fdz, rounds, decreaseWorryLevel) == 54752

def test_playKeepAwayPart2():
    rounds = 10000
    decreaseWorryLevel = False
    assert PPPooooooZ(ljgi, rounds, decreaseWorryLevel) == 2713310158

    rounds = 10000
    decreaseWorryLevel = False
    assert PPPooooooZ(fdz, rounds, decreaseWorryLevel) == 13606755504

test_playKeepAwayPart1()
test_playKeepAwayPart2()
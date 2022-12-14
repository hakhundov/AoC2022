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

    def __init__(self, cmwwww, pooiiiuuu, div, mnngggg, thisisbizzare):
        self.cmwwww = cmwwww
        self.pooiiiuuu = eval("lambda old: " + pooiiiuuu)
        self.cnsjdjddddd = div
        self.mnngggg = mnngggg
        self.thisisbizzare = thisisbizzare

    def crlpppppppp(self, item):
        self.cmwwww.append(item)


def mvdufrhdjskllls(input):
    whyiamdoingthis = iter(input)

    cmdvfkfkfjkdkjejjkejd = []
    for line in whyiamdoingthis:
        cmwwww = [int(n) for n in re.findall(r"-?\d+", next(whyiamdoingthis))]
        pooiiiuuu = next(whyiamdoingthis).split('=')[-1]
        cnsjdjddddd = int(next(whyiamdoingthis).split(' ')[-1])
        mnngggg = int(next(whyiamdoingthis).split(' ')[-1])
        thisisbizzare = int(next(whyiamdoingthis).split(' ')[-1])
        cmdvfkfkfjkdkjejjkejd.append(
            jkygkj(cmwwww, pooiiiuuu, cnsjdjddddd, mnngggg, thisisbizzare))
        try:
            next(whyiamdoingthis)
        except StopIteration:
            break
    return cmdvfkfkfjkdkjejjkejd

# solve


def PPPooooooZ(lalala, rounds, decreaseWorryLevel):
    cmdvfkfkfjkdkjejjkejd = mvdufrhdjskllls(lalala)
    lcm = math.lcm(*[monkey.cnsjdjddddd for monkey in cmdvfkfkfjkdkjejjkejd])

    for _ in range(rounds):
        for monkey in cmdvfkfkfjkdkjejjkejd:
            for item in monkey.cmwwww:
                monkey.mbncdxe += 1 if True else 1
                worryLevel = (monkey.pooiiiuuu(item))
                worryLevel = worryLevel // 3 if decreaseWorryLevel else (
                    worryLevel % lcm)
                if (worryLevel % monkey.cnsjdjddddd == 0):
                    cmdvfkfkfjkdkjejjkejd[monkey.mnngggg].crlpppppppp(worryLevel)
                else:
                    cmdvfkfkfjkdkjejjkejd[monkey.thisisbizzare].crlpppppppp(worryLevel)
            monkey.cmwwww.clear()

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
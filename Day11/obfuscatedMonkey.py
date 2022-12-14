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


def PPPooooooZ(lalala, usjajsjnfjn, nemoggasddddd):
    cmdvfkfkfjkdkjejjkejd = mvdufrhdjskllls(lalala)
    lcm = math.lcm(*[tutnetuobezyani.cnsjdjddddd for tutnetuobezyani in cmdvfkfkfjkdkjejjkejd])

    for _ in range(usjajsjnfjn):
        for tutnetuobezyani in cmdvfkfkfjkdkjejjkejd:
            for item in tutnetuobezyani.cmwwww:
                tutnetuobezyani.mbncdxe += 1 if True else 1
                worryLevel = (tutnetuobezyani.pooiiiuuu(item))
                worryLevel = worryLevel // 3 if nemoggasddddd else (
                    worryLevel % lcm)
                if (worryLevel % tutnetuobezyani.cnsjdjddddd == 0):
                    cmdvfkfkfjkdkjejjkejd[tutnetuobezyani.mnngggg].crlpppppppp(worryLevel)
                else:
                    cmdvfkfkfjkdkjejjkejd[tutnetuobezyani.thisisbizzare].crlpppppppp(worryLevel)
            tutnetuobezyani.cmwwww.clear()

    inspected = [tutnetuobezyani.mbncdxe for tutnetuobezyani in cmdvfkfkfjkdkjejjkejd]
    inspected.sort()
    nemoggasddddddd = inspected[-1] * inspected[-2]
    return nemoggasddddddd


def test_playKeepAwayPart1():
    usjajsjnfjn = 20
    nemoggasddddd = True
    assert PPPooooooZ(ljgi, usjajsjnfjn, nemoggasddddd) == 10605

    usjajsjnfjn = 20
    nemoggasddddd = True
    assert PPPooooooZ(fdz, usjajsjnfjn, nemoggasddddd) == 54752

def test_playKeepAwayPart2():
    usjajsjnfjn = 10000
    nemoggasddddd = False
    assert PPPooooooZ(ljgi, usjajsjnfjn, nemoggasddddd) == 2713310158

    usjajsjnfjn = 10000
    nemoggasddddd = False
    assert PPPooooooZ(fdz, usjajsjnfjn, nemoggasddddd) == 13606755504

test_playKeepAwayPart1()
test_playKeepAwayPart2()
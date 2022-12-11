from monkey import data, testData, playKeepAway


def test_playKeepAwayPart1():
    rounds = 20
    decreaseWorryLevel = True
    assert playKeepAway(testData, rounds, decreaseWorryLevel) == 10605

    rounds = 20
    decreaseWorryLevel = True
    assert playKeepAway(data, rounds, decreaseWorryLevel) == 54752

def test_playKeepAwayPart2():
    rounds = 10000
    decreaseWorryLevel = False
    assert playKeepAway(testData, rounds, decreaseWorryLevel) == 2713310158

    rounds = 10000
    decreaseWorryLevel = False
    assert playKeepAway(data, rounds, decreaseWorryLevel) == 13606755504
from tuningTrouble import checkRepetition, solve, data


def test_checkRepetition():
    assert checkRepetition("aabcd") == True
    assert checkRepetition("abcd") == False


def test_solvePart1():
    assert solve(data, 4) == 1794


def test_solvePart2():
    assert solve(data, 14) == 2851

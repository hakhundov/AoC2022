from treetop import solve, data


testData = []
with open("testInput", "r") as file:
    for line in file:
        testData.append(''.join(line.splitlines()))


def test_solveTestData():
    assert solve(testData) == 21


def test_solveRealData():
    assert solve(data) == 1835

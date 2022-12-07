from spaceOnDevice import data, solve


testData = []
with open("testInput", "r") as file:
    for line in file:
        testData.append(''.join(line.splitlines()))


def test_solveTestData():
    assert solve(testData) == [95437, 24933642]


def test_solveRealData():
    assert solve(data) == [1770595, 2195372]

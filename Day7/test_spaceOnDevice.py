from spaceOnDevice import solve
from aocd import get_data

data = get_data(day=7, year=2022).splitlines()

testData = []
with open("testInput", "r") as file:
    for line in file:
        testData.append(''.join(line.splitlines()))


def test_solveTestData():
    assert solve(testData) == [95437, 24933642]


def test_solveRealData():
    assert solve(data) == [1770595, 2195372]

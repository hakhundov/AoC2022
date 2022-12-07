from noname import solve
from aocd import get_data

data = get_data(day=8, year=2022).splitlines()

testData = []
with open("testInput", "r") as file:
    for line in file:
        testData.append(''.join(line.splitlines()))


def test_solveTestData():
    assert solve(testData) == []


def test_solveRealData():
    assert solve(data) == []

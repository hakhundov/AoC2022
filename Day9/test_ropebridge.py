from ropebridge import isTouching, isSameRow, isSameColumn, solve, data

def test_touchingTrue():
    assert isTouching([1, 1], [1, 1]) == True
    assert isTouching([1, 1], [0, 1]) == True
    assert isTouching([1, 1], [1, 0]) == True
    assert isTouching([1, 1], [0, 0]) == True
    assert isTouching([0, 0], [-1, -1]) == True


def test_touchingFalse():
    assert isTouching([1, 1], [3, 1]) == False
    assert isTouching([1, 1], [-1, 1]) == False
    assert isTouching([1, 1], [1, -1]) == False
    assert isTouching([1, 1], [3, 1]) == False


def test_sameRow():
    assert isSameRow([1, 1], [1, 0]) == False
    assert isSameRow([1, 1], [2, 1]) == True

def test_sameColumn():
    assert isSameColumn([1, 1], [0, 1]) == False
    assert isSameColumn([1, 1], [1, 4]) == True

testData = []
file = open("testInput", "r")
for line in file:
    testData.append(line.strip())

def test_solveTestInput(test):
    assert solve(testData) == [13, 36]

def test_solveRealInput():
    assert solve(data) == [6037, 2485]
from ropebridge import isTouching, isSameRow, isSameColumn

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

# testData = []
# with open("testInput", "r") as file:
#     for line in file:
#         testData.append(''.join(line.splitlines()))

# def test_part1TestInput():
#     assert solvePart1(testData) ==  13

# def test_part1TestInput():
#     assert solvePart1(testData) ==  6037
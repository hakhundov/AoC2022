from ropebridge import touching, sameRow, sameColumn

def test_touchingTrue():
    assert touching([1, 1], [1, 1]) == True
    assert touching([1, 1], [0, 1]) == True
    assert touching([1, 1], [1, 0]) == True
    assert touching([1, 1], [0, 0]) == True
    assert touching([0, 0], [-1, -1]) == True


def test_touchingFalse():
    assert touching([1, 1], [3, 1]) == False
    assert touching([1, 1], [-1, 1]) == False
    assert touching([1, 1], [1, -1]) == False
    assert touching([1, 1], [3, 1]) == False


def test_sameRow():
    assert sameRow([1, 1], [1, 0]) == False
    assert sameRow([1, 1], [2, 1]) == True

def test_sameColumn():
    assert sameColumn([1, 1], [0, 1]) == False
    assert sameColumn([1, 1], [1, 4]) == True

# testData = []
# with open("testInput", "r") as file:
#     for line in file:
#         testData.append(''.join(line.splitlines()))

# def test_part1TestInput():
#     assert solvePart1(testData) ==  13

# def test_part1TestInput():
#     assert solvePart1(testData) ==  6037
from day12 import canMove, getNeighbors, data, findStart


def test_canMove():
    assert canMove('a', 'b') == True
    assert canMove('a', 'c') == False

def test_getNeighbors():
    assert getNeighbors(data, 1, 1, 10, 10) == [(0,1),(2,1),(1,0),(1,2)]
    assert getNeighbors(data, 0, 0, 10, 10) == [(1,0),(0,1)]
    # assert getNeighbors(data, 9, 9, 10, 10) == [(8,9),(9,8)]
    assert getNeighbors(data, 0, 2, 10, 10) == [(1, 2), (0, 1)]

testData = []
with open("testInput", "r") as file:
    for line in file:
        testData.append(line.strip())  # unpack


def test_findStart():
    assert findStart(testData) == (0,0)

# part 1 
# test 31
# real 462

# part 2
# test 29
# real 451

# v..v<<<<
# >v.vv<<^
# .>vv>E^^
# ..v>>>^^
# ..>>>>>^

# Sabqponm
# abcryxxl
# accszExk
# acctuvwj
# abdefghi
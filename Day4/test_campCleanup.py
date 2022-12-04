from campCleanup import solvePart1, solvePart2, solveDay4

def test_partOne():
    assert solvePart1("testInput") == 2
    assert solvePart1("input") == 509

def test_partTwo():
    assert solvePart2("testInput") == 4
    assert solvePart2("input") == 870

def test_day4():
    assert solveDay4("testInput") == [2,4]
    assert solveDay4("input") == [509,870]
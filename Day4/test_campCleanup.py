from campCleanup import solvePart1, solvePart2

def test_partOne():
    assert solvePart1("testInput") == 2
    assert solvePart1("input") == 509

def test_partTwo():
    assert solvePart2("testInput") == 4
    # assert solvePart1("input") ==
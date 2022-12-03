from rucksack import getPriority, solvePart1, solvePart2


def test_getPriority():
    assert getPriority('a') == 1
    assert getPriority('z') == 26
    assert getPriority('A') == 27
    assert getPriority('Z') == 52

def test_partOne():
    assert solvePart1("input") == 7917


def test_partTwo():
    assert solvePart2("input") == 2585
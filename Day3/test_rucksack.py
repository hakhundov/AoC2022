from rucksack import getPriority, solvePart1


def test_getPriority():
    assert getPriority('a') == 1
    assert getPriority('z') == 26
    assert getPriority('A') == 27
    assert getPriority('Z') == 52

def test_partOne():
    assert solvePart1("input") == 7917
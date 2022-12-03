from rucksack import getPriority


def test_getPriority():
    assert getPriority('a') == 1
    assert getPriority('z') == 26
    assert getPriority('A') == 27
    assert getPriority('Z') == 52
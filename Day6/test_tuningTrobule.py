from tuningTrouble import checkRepetition, solve, data


def test_checkRepetition():
    assert checkRepetition("aabcd") == True
    assert checkRepetition("abcd") == False


def test_solvePart1TestInput():
    assert solve(['bvwbjplbgvbhsrlpgdmjqwftvncz'], 4) == 5
    assert solve(['nppdvjthqldpwncqszvftbrmjlhg'], 4) == 6
    assert solve(['nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'], 4) == 10
    assert solve(['zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'], 4) == 11


def test_solvePart2TestInput():
    assert solve(['mjqjpqmgbljsphdztnvjfqwrcgsmlb'], 14) == 19
    assert solve(['bvwbjplbgvbhsrlpgdmjqwftvncz'], 14) == 23
    assert solve(['nppdvjthqldpwncqszvftbrmjlhg'], 14) == 23
    assert solve(['nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'], 14) == 29
    assert solve(['zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'], 14) == 26


def test_solvePart1():
    assert solve(data, 4) == 1794


def test_solvePart2():
    assert solve(data, 14) == 2851

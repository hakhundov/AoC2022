from cpu import solve, solve2,data


testData = []
with open("testInput", "r") as file:
    for line in file:
        testData.append(''.join(line.splitlines()))

# part 1
# test  = 13140
# real = 13520

#part 2
# test

##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######.....

# real

###...##..###..#..#.###..####..##..###..
#..#.#..#.#..#.#..#.#..#.#....#..#.#..#.
#..#.#....#..#.####.###..###..#..#.###..
###..#.##.###..#..#.#..#.#....####.#..#.
#....#..#.#....#..#.#..#.#....#..#.#..#.
#.....###.#....#..#.###..####.#..#.###..

def test_solveTestData():
    assert solve(testData) == 21


def test_solveRealData():
    assert solve(data) == 1835



def test_solveTestDataP2():
    assert solve2(testData) == 8


def test_solveRealDataP2():
    assert solve2(data) == 263670
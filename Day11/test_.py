# from cpu import solve, solve2,data


testData = []
with open("testInput", "r") as file:
    for line in file:
        testData.append(''.join(line.splitlines()))



# def test_solveTestData():
#     assert solve(testData) == 21
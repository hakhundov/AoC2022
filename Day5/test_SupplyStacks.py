from SupplyStacks import solvePart1, solvePart2, data

# get test input data from file
# data = []
# with open("testInput", "r") as file:
#     for line in file:
#         data.append(line.strip())


def test_solvePart1():
    # assert solveDay4P1("testInput") == "CMZ"
    assert solvePart1(data) == "FRDSQRRCD"

def test_solvePart2():
    # assert solveDay4P1("testInput") == "CMZ"
    assert solvePart2(data) == "HRFTQVWNN"

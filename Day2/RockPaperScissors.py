# AoC 2022 - Day 2 - Rock Paper Scissors

# easier to do modular arithmetic, hence -1 all points. doing a + 1 when collecting points
points = {
    'X': 0,  # rock
    'Y': 1,  # paper
    'Z': 2,  # scissors
    'A': 0,
    'B': 1,
    'C': 2
}

winPoints = {
    0: 3,
    1: 0,
    2: 6
}


def solveDay2(inputFilename):
    scorePartOne = 0
    scorePartTwo = 0
    with open(inputFilename, "r") as file:
        for count, line in enumerate(file):
            oponent, me = line.strip().split(' ')
            scorePartOne += winPoints[(points[oponent] - points[me]) % 3] + int(points[me]) + 1
            match me:
                case 'X':  # lose
                    scorePartTwo += (points[oponent]-1) % 3
                case 'Y':  # draw
                    scorePartTwo += 3 + (points[oponent]) % 3
                case 'Z':  # win
                    scorePartTwo += 6 + (points[oponent] + 1) % 3
            scorePartTwo += 1

    return [scorePartOne, scorePartTwo]

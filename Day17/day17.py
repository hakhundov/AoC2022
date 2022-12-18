# AoC 2022 - Day 17 - https://adventofcode.com/2022/day/17

from aocd import get_data
import re
import copy

data = get_data(day=17, year=2022).splitlines()

testData = []
with open("testInput", "r") as file:
    for line in file:
        testData.append(line.strip())

def moveLeft(shape: list):
    for point in shape:
        point[1] -= 1

def moveRight(shape: list):
    for point in shape:
        point[1] += 1

def moveDown(shape: list):
    for point in shape:
        point[0] -= 1

def moveUp(shape: list):
    for point in shape:
        point[0] += 1

def adjustPosition(shape: list, topPosition: int, k: int):
    for point in shape:
        point[0] += (topPosition + k)
    return shape

def checkCollision(shape: list, fullPicture):
    for point in shape:
        point = (point[0],point[1])
        if point in fullPicture:
            return True
        if point[1]<0 or point[1]>6:
            return True
        if point[0]<0:
            return True
    return False


shapes = [
    [[0,2],[0,3],[0,4],[0,5]],
    [[0,3],[1,2],[1,3],[1,4],[2,3]],
    [[0,2],[0,3],[0,4],[1,4],[2,4]],
    [[0,2], [1,2], [2,2], [3,2]],
    [[0,2], [1,2], [0,3], [1,3]]
]

fullPicture = set()
currentShape = 0
top = 0
fallingShape = copy.deepcopy(shapes[currentShape])
adjustPosition(fallingShape, top, 3)
stoppedRocks = 0

windPattern = data[0]
# windPattern = testData[0]
currentWind = 0
debug = False

while True:
    dir = windPattern[currentWind]
    # if (debug):
        # print("current direction: ", dir)
    currentWind = (currentWind + 1) % len(windPattern)
    match dir:
        case '>':
            moveRight(fallingShape)
            if checkCollision(fallingShape, fullPicture):
                moveLeft(fallingShape)
            # if (debug):
                # print(" > " , fallingShape)
        case '<':
            moveLeft(fallingShape)
            if checkCollision(fallingShape, fullPicture):
                moveRight(fallingShape)
            # if (debug):
                # print(" < " , fallingShape)

    moveDown(fallingShape)
    if checkCollision(fallingShape, fullPicture):
        moveUp(fallingShape)
        top = max( max([x[0] for x in fallingShape]), top )
        for point in fallingShape:
            fullPicture.add((point[0], point[1]))
            # if (debug):
                # print("adding to full picture:", (point[0], point[1]) )
        stoppedRocks += 1
        # if (debug):
            # print("stopped rock " , stoppedRocks, " max height: ", top)
        
        currentShape = (currentShape + 1) % 5
        fallingShape = copy.deepcopy(shapes[currentShape])
        adjustPosition(fallingShape, top, 4)
        # if (debug):
            # print(" top is " , top)
            # print("adjusted shape is ", fallingShape)
        if stoppedRocks == 2022:
            print(top+1)
            break
    # else:
        # if (debug):
            # print(" just down " , fallingShape)

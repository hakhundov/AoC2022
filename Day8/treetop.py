# AoC 2022 - Day 8 - https://adventofcode.com/2022/day/7

from aocd import get_data
data = get_data(day=8, year=2022).splitlines()

testData = []
with open("testInput", "r") as file:
    for line in file:
        testData.append([*''.join(line.splitlines())]) #unpack


print(testData)
# print(len(data))

    #naive implementation
def solve(data):
    count = 0
    width = len(data[0])
    length = len(data)

    # print(width, length)
    visibleEdges = 2 * width + 2 * length - 4
    # print(visibleEdges)

    flag = [ [0]*width for i in range(length)]
    # print(flag)

    maxT = 0
    maxL = 0

    # check from left
    for i in range(1, width-1, 1):
        maxL = 0
        for j in range (1, length-1, 1):
            if (int(data[i][j]) > int(data[i][j-1])) and (int(data[i][j]) > maxL):
                flag[i][j] = 1
                maxL = max(maxL, int(data[i][j]))
            else:
                 maxL = max(maxL, int(data[i][j-1]))
    # print(flag)

    # check from top
    for j in range(1, width-1, 1):
        maxT = 0
        for i in range (1, length-1, 1):
            # print("i, j =", i, j)
            if (int(data[i][j]) > int(data[i-1][j])) and (int(data[i][j]) > maxT):
                flag[i][j] = 1
                maxT = max(maxT, int(data[i][j]))
            else:
                maxT = max(maxT, int(data[i-1][j]))
    # print(flag)

    # check from right
    for i in range(width-2, 0, -1):
        maxT = 0
        for j in range (length-2, 0, -1):
            # print("i, j =", i, j)
            if (int(data[i][j]) > int(data[i][j+1])) and (int(data[i][j]) > maxT):
                flag[i][j] = 1
                maxT = max(maxT, int(data[i][j]))
            else:
                maxT = max(maxT, int(data[i][j+1]))
    # print(flag)

    # check from bottom
    for j in range(width-2, 0, -1):
        maxT = 0
        for i in range (length-2, 0, -1):
            print("i, j =", i, j)
            if (int(data[i][j]) > int(data[i+1][j])) and (int(data[i][j]) > maxT):
                flag[i][j] = 1
                maxT = max(maxT, int(data[i+1][j]))
            else:
                maxT = max(maxT, int(data[i+1][j]))
    # print(flag)

    return sum(sum(flag,[])) + visibleEdges # TODO: understand how sum flattens the list

print(solve(data))


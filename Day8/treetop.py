# AoC 2022 - Day 8 - https://adventofcode.com/2022/day/8

from aocd import get_data
data = get_data(day=8, year=2022).splitlines()

testData = []
with open("testInput", "r") as file:
    for line in file:
        testData.append([*''.join(line.splitlines())])  # unpack


# part 1 - naive implementation
def solve(data):
    width = len(data[0])
    length = len(data)
    visibleEdges = 2 * width + 2 * length - 4
    flag = [[0]*width for i in range(length)]
    maxHeight = 0

    # check from left
    for i in range(1, width-1, 1):
        maxHeight = 0
        for j in range(1, length-1, 1):
            if (int(data[i][j]) > int(data[i][j-1])) and (int(data[i][j]) > maxHeight):
                flag[i][j] = 1
                maxHeight = max(maxHeight, int(data[i][j]))
            else:
                maxHeight = max(maxHeight, int(data[i][j-1]))

    # check from top
    for j in range(1, width-1, 1):
        maxHeight = 0
        for i in range(1, length-1, 1):
            if (int(data[i][j]) > int(data[i-1][j])) and (int(data[i][j]) > maxHeight):
                flag[i][j] = 1
                maxHeight = max(maxHeight, int(data[i][j]))
            else:
                maxHeight = max(maxHeight, int(data[i-1][j]))

    # check from right
    for i in range(width-2, 0, -1):
        maxHeight = 0
        for j in range(length-2, 0, -1):
            if (int(data[i][j]) > int(data[i][j+1])) and (int(data[i][j]) > maxHeight):
                flag[i][j] = 1
                maxHeight = max(maxHeight, int(data[i][j]))
            else:
                maxHeight = max(maxHeight, int(data[i][j+1]))

    # check from bottom
    for j in range(width-2, 0, -1):
        maxHeight = 0
        for i in range(length-2, 0, -1):
            if (int(data[i][j]) > int(data[i+1][j])) and (int(data[i][j]) > maxHeight):
                flag[i][j] = 1
                maxHeight = max(maxHeight, int(data[i+1][j]))
            else:
                maxHeight = max(maxHeight, int(data[i+1][j]))

    # TODO: understand how sum flattens the list
    return sum(sum(flag, [])) + visibleEdges


# part 2 - highest scenic score
def solve2(data):
    width = len(data[0])
    length = len(data)

    maxScenicScore = 0

    # iterate through all trees
    for i in range(1, width-1, 1):
        for j in range(1, length-1, 1):
            #process tree
            # print("-- ", i,j, " --")
            scenicScore = 1

            #look up
            count = 0
            for ii in range(i-1, -1, -1):
                if int(data[ii][j]) < int(data[i][j]):
                    count += 1
                elif int(data[ii][j]) >= int(data[i][j]):
                    count += 1
                    break
                else:
                    break
            scenicScore = scenicScore * count

            #look down
            count = 0
            for ii in range(i+1, width, 1):
                if int(data[ii][j]) < int(data[i][j]):
                    count += 1
                elif int(data[ii][j]) >= int(data[i][j]):
                    count += 1
                    break
                else:
                    break
            scenicScore = scenicScore * count
            
            #look left
            count = 0
            for jj in range(j-1, -1, -1):
                if int(data[i][jj]) < int(data[i][j]):
                    count += 1
                elif int(data[i][jj]) >= int(data[i][j]):
                    count += 1
                    break
                else:
                    break
            scenicScore = scenicScore * count

            #look right
            count = 0
            for jj in range(j+1, length, 1):
                if int(data[i][jj]) < int(data[i][j]):
                    count += 1
                elif int(data[i][jj]) >= int(data[i][j]):
                    count += 1
                    break
                else:
                    break
            scenicScore = scenicScore * count

            maxScenicScore = max(maxScenicScore, scenicScore)

    return maxScenicScore


print(solve2(data))

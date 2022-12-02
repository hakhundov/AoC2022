# AoC 2022 - Day 2 - Rock Paper Scissors
# 1 Rock     A  X
# 2 Paper    B  Y
# 3 Scissors C  Z
# 0 lost
# 3 draw
# 6 win

file = open("input", "r")
score = 0
points = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

for line in file:
    oponent, me = line.strip().split(' ')
    score += points[me]

    if (oponent == (me.replace('X', 'A').replace('Y', 'B').replace('Z', 'C'))):
        score += 3
    elif ((me == 'X' and oponent == 'C') or (me == 'Y' and oponent == 'A') or (me == 'Z' and oponent == 'B')):
        score += 6

print(score)
if (score == 14163):
    print('PASSED!')
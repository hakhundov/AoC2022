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
    'Z': 3,
    'A': 1,
    'B': 2,
    'C': 3
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


# -----------------------
# Part 2
# X -> lose, Y ->  draw, and Z -> win.

file.seek(0)
score = 0
win_points = {
    'X': 0,
    'Y': 3, 
    'Z': 6
}

win_hand = {
    'A': 2, # if oponent has rock, paper is to win
    'B': 3, # scissors
    'C': 1  # rock
}

lose_hand = {
    'A': 3, #scissor
    'B': 1, #rock
    'C': 2  #paper
}

for line in file:
    oponent, instruction = line.strip().split(' ')
    score += win_points[instruction]

    if instruction == 'Y': # draw
        score += points[oponent]
    elif instruction == 'X': # lose
        score += lose_hand[oponent]
    else: # win
        score += win_hand[oponent]


print(score)

if (score == 12091):
    print('PASSED!')
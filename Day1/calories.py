file = open("input", "r")
max = 0
summa = 0

# for line in file:
#     if line != "\n":
#         summa += int(line.strip())
#     else:
#         if summa > max:
#             max = summa
#         summa = 0
# print(max)

# part 2 - slighly modifyed the top one
calories = []
summa = 0
for line in file:
    if line != "\n":
        summa += int(line.strip())
    else:
        calories.append(summa)
        summa = 0
calories.sort()
print(str( sum(calories[-3:])))
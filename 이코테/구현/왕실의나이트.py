dot = input()

row = int(dot[1])
column = int(ord(dot[0]) - ord("a")) + 1
steps = [
    (-2, 1),
    (-2, -1),
    (-1, 2),
    (-1, -2),
    (1, 2),
    (1, -2),
    (2, 1),
    (2, -1),
]
count = 0

for step in steps:
    nRow = row + step[0]
    nColumn = column + step[1]
    if 1 <= nRow <= 8 and 1 <= nColumn <= 8:
        count += 1

print(count)

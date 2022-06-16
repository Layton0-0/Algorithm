miro = []
MIROSIZE = 10
for i in range(MIROSIZE):
    miro.append(list(map(int, input().split())))

x, y = 1, 1
while True:
    if miro[x][y] == 0:
        miro[x][y] = 9
    elif miro[x][y] == 2:
        miro[x][y] = 9
        break

    right = miro[x][y + 1]
    down = miro[x + 1][y]

    if (right == 1 and down == 1) or (x == 8 and y == 8):
        break

    if right != 1:
        y += 1
    elif down != 1:
        x += 1

for i in range(MIROSIZE):
    for j in range(MIROSIZE):
        print(miro[i][j], end=" ")
    print()

miro = []
MIROSIZE = 10
for i in range(MIROSIZE):
    miro.append(list(map(int, input().split())))
x, y = 1, 1
print()
while True:
    miro[x][y] = 9
    right = miro[x][y + 1]
    down = miro[x + 1][y]
    if right == 0:
        y += 1
    elif right == 1:
        if down == 0:
            x += 1
        elif down == 1:
            break
        else:
            x += 1
            miro[x][y] = 9
            break
    else:
        y += 1
        miro[x][y] = 9
        break
for i in range(MIROSIZE):
    for j in range(MIROSIZE):
        print(miro[i][j], end=" ")
    print()

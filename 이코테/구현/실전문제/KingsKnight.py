point = input()
x, y = int(point[1]), ord(point[0])

dx = [2, 2, 1, -1, -2, -2, -1, 1]
dy = [-1, 1, 2, 2, 1, -1, -2, -2]
count = 0

for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx < 1 or nx > 8 or ny < 97 or ny > 104:
        continue
    count += 1

print(count)

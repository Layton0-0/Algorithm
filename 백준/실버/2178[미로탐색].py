from collections import deque

n, m = map(int, input().split())
miro = []
for i in range(n):
    miro.append(list(map(int, input())))

# 북동남서
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

x = 0
y = 0


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        if x == n - 1 and y == m - 1:
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if miro[nx][ny] == 1:
                queue.append((nx, ny))
                miro[nx][ny] += miro[x][y]
    return miro[n - 1][m - 1]


print(bfs(x, y))

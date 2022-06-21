from collections import deque

n, m = map(int, input().split())
maze = []

for i in range(n):
    maze.append(list(map(int, input())))

# n과 m을 기준으로 x와 y를 설정하므로 순서대로 상하좌우.
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    # 현재 위치를 큐에 삽입.
    queue.append((x, y))

    # 큐가 빌 때까지 반복
    while queue:
        # 시작점 빼면서 현재 위치로 저장
        x, y = queue.popleft()
        # 상하좌우 반복이라 4번/ 상하좌우의 노드들에 각각의 최단거리를 기록한다.
        for i in range(4):
            # 반복할 때마다 상, 하, 좌, 우로 이동.
            new_x = x + dx[i]
            new_y = y + dy[i]

            # 범위 벗어나면 무시
            if new_x < 0 or new_y < 0 or new_x >= n or new_y >= m:
                continue

            # 벽일 경우 무시
            if maze[new_x][new_y] == 0:
                continue

            # 해당 노드 처음 방문하는 경우(1) 최단 거리 기록(추가)
            if maze[new_x][new_y] == 1:
                # 기존 노드에서 1더한 값을 저장.
                maze[new_x][new_y] = maze[x][y] + 1
                # 근접 노드 저장
                queue.append((new_x, new_y))
    # 최종값 리턴
    return maze[n - 1][m - 1]


print(bfs(0, 0))

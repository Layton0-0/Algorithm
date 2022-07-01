from collections import deque


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ")
    for i in range(1, n + 1):
        if not visited[i] and graph[v][i] == 1:
            dfs(graph, i, visited)


def bfs(graph, start, visited):
    visited[start] = True
    queue = deque([start])
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in range(1, n + 1):
            if not visited[i] and graph[v][i] == 1:
                queue.append(i)
                visited[i] = True


n, m, v = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(m):
    x, y = map(int, input().split())
    graph[x][y] = graph[y][x] = 1

visited = [False] * (n + 1)
dfs(graph, v, visited)
print()
visited = [False] * (n + 1)
bfs(graph, v, visited)

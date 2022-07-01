from collections import deque

n, m, v = map(int, input().split())
node = [[] for _ in range(n + 1)]
for i in range(m):
    x, y = map(int, input().split())
    node[x].append(y)
    node[y].append(x)
for i in range(1, n + 1):
    node[i].sort()


def dfs(node, v, visited):
    visited[v] = True
    print(v, end=" ")

    for i in node[v]:
        if visited[i] == False:
            dfs(node, i, visited)


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        now = queue.popleft()
        print(now, end=" ")

        for i in graph[now]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True


visited = [False] * (n + 1)

dfs(node, v, visited)
print()
visited = [False] * (n + 1)
bfs(node, v, visited)

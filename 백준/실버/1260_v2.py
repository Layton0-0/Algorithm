import sys
from collections import deque

input = sys.stdin.readline

n, m, v = map(int, input().split())
nodes = [[] for _ in range(n + 1)]
for i in range(m):
    x, y = map(int, input().split())
    nodes[x].append(y)
    nodes[y].append(x)
for i in range(n + 1):
    nodes[i].sort()


def dfs(visited, v, nodes):
    visited[v] = 1
    print(v, end=" ")
    for i in nodes[v]:
        if visited[i] == 0:
            dfs(visited, i, nodes)


def bfs(nodes, start, visited):
    queue = deque([start])
    visited[start] = 1
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in nodes[v]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = 1


visited = [0] * (n + 1)
dfs(visited, v, nodes)
print()
visited = [0] * (n + 1)
bfs(nodes, v, visited)

import sys
from collections import deque

input = sys.stdin.readline


def bfs(nodes, start, visited):
    queue = deque([start])
    visited[start] = 0
    while queue:
        v = queue.popleft()
        if visited[v] == k:
            answer.append(v)
        for node in nodes[v]:
            if visited[node] < 0:
                visited[node] = visited[v] + 1
                queue.append(node)


n, m, k, x = map(int, input().split())
roads = [[] for _ in range(n + 1)]
visited = [-1] * (n + 1)
answer = []

for i in range(m):
    a, b = map(int, input().split())
    roads[a].append(b)

bfs(roads, x, visited)
answer.sort()

if len(answer) > 0:
    for i in answer:
        print(i)
else:
    print(-1)

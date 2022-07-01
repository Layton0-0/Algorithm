com_amount = int(input())
ssang = int(input())
graph = [[0] * (com_amount + 1) for _ in range(com_amount + 1)]
for i in range(ssang):
    x, y = map(int, input().split())
    graph[x][y] = graph[y][x] = 1

global count
count = 0


def dfs(graph, v, visited):
    visited[v] = True
    global count
    count += 1
    for i in range(1, com_amount + 1):
        if not visited[i] and graph[v][i] == 1:
            dfs(graph, i, visited)


visited = [False] * (com_amount + 1)
dfs(graph, 1, visited)

# 1은 카운트 안해야 하기 때문
print(count - 1)

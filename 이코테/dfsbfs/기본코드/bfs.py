# popleft사용해서 큐 구현
from collections import deque


def bfs(graph, start, visited):
    # 시작 노드를 큐에 넣어준다.
    queue = deque([start])
    visited[start] = True

    # 큐가 빌 때까지 반복
    while queue:
        # 가장 먼저 들어온 요소 빼고 검사
        v = queue.popleft()
        print(v, end=" ")

        # 요소의 행에서 아직 방문 안 한 원소가 있으면 방문 및 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


# 인접 행렬 방식으로 표현
graph = [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]

# 각 노드의 방문여부를 표현
visited = [False] * 9

bfs(graph, 1, visited)

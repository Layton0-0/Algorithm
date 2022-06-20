# 인접 행렬

INF = 999999999  # 무한의 비용
graph = [
    [0, 2, 3, INF, INF],
    [2, 0, 15, 2, INF],
    [3, 15, 0, INF, 13],
    [INF, 2, INF, 0, 9],
    [INF, INF, 13, 9, 0],
]

print(graph)

# 인접 리스트
graph_list = [[] for _ in range(6)]

# 노드 0에 연결된 노드 정보 저장(노드, 거리)
graph_list[0].append((1, 3))
graph_list[0].append((2, 5))

# 노드 1에 연결된 노드 정보 저장(노드, 거리)
graph_list[1].append((3, 2))

# 노드 2에 연결된 노드 정보 저장(노드, 거리)
graph_list[2].append((3, 1))

# 노드 3에 연결된 노드 정보 저장(노드, 거리)
graph_list[3].append((4, 4))
graph_list[3].append((5, 8))

# 노드 4에 연결된 노드 정보 저장(노드, 거리)
graph_list[4].append((5, 6))

# 노드 5에서 뻗어나가는건 없음.
print(graph_list)

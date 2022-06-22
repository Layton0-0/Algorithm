n, m = map(int, input().split())
a, b, d = map(int, input().split())
game_map = []
# 북, 동, 남, 서
da = [1, 0, -1, 0]
db = [0, 1, 0, -1]
visit_count = 0
# 정답코드에서는 방문한 위치를 따로 저장함(컴프리헨션을 이용해 초기화)
visited = [[0] * m for _ in range(n)]

for i in range(n):
    game_map.append(list(map(int, input().split())))

while True:
    # 방문 기록
    game_map[a][b] = 1
    visit_count += 1
    # 방향 방문 카운트
    dir_count = 0
    # 4방향 탐색
    for i in range(4):
        # 왼쪽 방향 탐색
        nd = d - 1
        if d < 0:
            nd = 3
        # 향하는 방향으로 위치 저장
        na = a + da[nd]
        nb = b + db[nd]
        # 왼쪽으로 돈 그 곳이 육지라면(안 가본 곳이라면)
        if game_map[na][nb] == 0:
            # 왼쪽 방향으로 회전
            d = nd
            # 한 칸 이동
            a, b = na, nb
            break
        # 왼쪽으로 돈 그 곳이 육지가 아니라면
        else:
            # 왼쪽으로 회전
            d = nd
            dir_count += 1
    # 4방향 모두 확인하고도 이동하지 않은 경우
    if dir_count == 4:
        # 방향 유지하고 한 칸 뒤로
        na = a - da[d]
        nb = b - db[d]
        # 뒤가 이동 불가지역이면 탐색 중지
        if game_map[na][nb] == 1:
            break
        # 이동 가능 지역이면 이동 후 탐색 진행
        a, b = na, nb


print(visit_count)

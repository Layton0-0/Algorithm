n = int(input())
plans = input().split()
direction = ["L", "R", "U", "D"]
# L, R, U, D(direction과 인덱스를 맞춤)
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
x, y = 1, 1

for plan in plans:
    # 방향의 인덱스 값을 저장
    i = direction.index(plan)
    # 방향 벡터를 이용해 해당 좌표 저장
    nx = x + dx[i]
    ny = y + dy[i]
    # 이동한 좌표가 범위를 벗어나면 해당 경로 패스
    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue
    x, y = nx, ny

print(x, y)

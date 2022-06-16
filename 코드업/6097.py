# h = 세로, w = 가로
h, w = map(int, input().split())
# 판
pan = [[0 for _ in range(w)] for _ in range(h)]
# n = 막대의 개수
n = int(input())
# 막대의 길이(l), 방향(d) 가로0 세로1, 좌표(x, y)
stick_info = []
for i in range(n):
    l, d, x, y = map(int, input().split())
    # 인덱스 값으로 바로 사용 위함
    x -= 1
    y -= 1
    if d == 0:
        for j in range(l):
            pan[x][y] = 1
            y += 1
    else:
        for j in range(l):
            pan[x][y] = 1
            x += 1

for i in range(h):
    for j in range(w):
        print(pan[i][j], end=" ")
    print()

# 판 모양
pan = []
# 뒤집기 기준 좌표
turning_point = []
# 판 사이즈
PANSIZE = 19
for i in range(PANSIZE):
    pan.append(list(map(int, input().split())))
n = int(input())
for i in range(n):
    turning_point.append(list(map(int, input().split())))
    for j in range(PANSIZE):
        # 자기 자신은 바뀌지 않는다 = 2번 바꿔버린다
        row_point = turning_point[i][0] - 1
        col_point = turning_point[i][1] - 1
        pan[row_point][j] = int(not pan[row_point][j])
        pan[j][col_point] = int(not pan[j][col_point])

for i in range(PANSIZE):
    for j in range(PANSIZE):
        print(pan[i][j], end=" ")
    print()

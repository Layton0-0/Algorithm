n = int(input())
lst = []
PANSIZE = 19
# 2차원 배열 0으로 초기화
pan = [[0 for _ in range(PANSIZE)] for _ in range(PANSIZE)]

for i in range(n):
    # 배열 안에 배열을 넣어 입력과 동시에 저장
    lst.append(list(map(int, input().split())))
    # index는 입력된 값에서 1을 뺀 값
    pan[lst[i][0] - 1][lst[i][1] - 1] = 1

for i in range(PANSIZE):
    for j in range(PANSIZE):
        print(pan[i][j], end=" ")
    print()

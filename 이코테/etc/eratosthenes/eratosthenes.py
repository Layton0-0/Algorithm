import math

n = 1000
array = [True for i in range(n + 1)]

for i in range(2, int(math.sqrt(n)) + 1):
    # 아직 검사하지 않은 칸이라면
    if array[i] == True:
        j = 2
        # 해당 구구단 전부 방문 처리
        while i * j <= n:
            array[i * j] = False
            j += 1

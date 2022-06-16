n = int(input())
lst = list(map(int, input().split()))
# 총 학생 수
STUDENT = 23
# 0으로 채워진 길이가 23(학생수)인 배열 형성
count = [0 for _ in range(STUDENT)]

for i in range(n):
    # 배열은 0부터 시작하니 부른 숫자에서 1뺀 index의 value를 count.
    count[lst[i] - 1] += 1

for i in range(STUDENT):
    print(count[i], end=" ")

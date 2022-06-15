a, m, d, n = map(int, input().split())
# a는 첫번째 값이라 식을 안 거쳐도 되니 n-1회 반복 필요
for _ in range(n - 1):
    # ma + d를 다시 a값으로 만들어 재귀형태로 구현(점화식 형태)
    a = m * a + d
print(a)

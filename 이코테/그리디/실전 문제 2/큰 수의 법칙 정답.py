n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()  # 정렬 먼저 하기
first = data[n - 1]
second = data[n - 2]

count = int(m / (k + 1)) * k  # 묶음으로 몇 번 인지 카운트
count += m % (k + 1)  # 남은 떨이 카운트

result = 0
result += (count) * first  # 가장 큰 수 더하기
result += (m - count) * second  # 두 번째로 큰 수 더하기

print(result)

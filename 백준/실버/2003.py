# 투포인터 기본 문제
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))

i_sum = 0
end = 0
count = 0

for start in range(n):
    while i_sum < m and end < n:
        i_sum += a[end]
        end += 1
    if i_sum == m:
        count += 1
    i_sum -= a[start]

print(count)

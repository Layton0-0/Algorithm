# 에라토스테네스의 체
import sys
import math

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
m = max(arr)

num = [True for _ in range(m + 1)]
num[0] = False
num[1] = False
count = 0

for i in range(2, int(math.sqrt(m)) + 1):
    if num[i]:
        j = 2
        while i * j <= m:
            num[i * j] = False
            j += 1

for a in arr:
    if num[a]:
        count += 1

print(count)

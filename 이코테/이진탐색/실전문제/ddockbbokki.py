# 내 풀이는 순차 탐색 풀이. 입력값이 많아지면 시간 초과 판정을 받을 수 있음.
import sys


def binary_search(array, target, start, end):
    mid = (start + end) // 2
    while start <= end:
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


n, m = map(int, input().split())
rice_cakes = list(map(int, sys.stdin.readline().rstrip().split()))

# index = binary_search()
for h in range(max(rice_cakes), -1, -1):
    minus = 0
    for j in range(n):
        if rice_cakes[j] - h > 0:
            minus += rice_cakes[j] - h
    if minus >= m:
        print(h)
        break

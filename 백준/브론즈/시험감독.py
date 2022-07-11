import sys

input = sys.stdin.readline

n = int(input())
s_num = list(map(int, input().rstrip().split()))
b, c = map(int, input().split())

count = 0
for num in s_num:
    # 총감독관 먼저 빼줌(무조건 있어야 하니까)
    if num > b:
        num -= b
        count += 1
        # 나누어 떨어질 경우 한 명이 누락됨(제외 시켜줌)
        if num % c == 0:
            count += num // c
        else:
            count += num // c + 1
    else:
        count += 1

print(count)

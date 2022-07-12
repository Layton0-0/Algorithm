# 백트래킹
import sys

input = sys.stdin.readline
n = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split()))

maxinum = -1e9
minimum = 1e9


def dfs(depth, total, plus, minus, multi, div):
    global maxinum, minimum
    if depth == n:
        maxinum = max(total, maxinum)
        minimum = min(total, minimum)
        return

    if plus:
        # 돌아와서 다음꺼 검사
        dfs(depth + 1, total + num[depth], plus - 1, minus, multi, div)
    if minus:
        dfs(depth + 1, total - num[depth], plus, minus - 1, multi, div)
    if multi:
        dfs(depth + 1, total * num[depth], plus, minus, multi - 1, div)
    if div:
        # int(total / num[depth])로 나누기 하면 c++의 방식으로 음수 나누기까지 할 수 있다
        dfs(depth + 1, int(total / num[depth]), plus, minus, multi, div - 1)


dfs(1, num[0], op[0], op[1], op[2], op[3])
print(maxinum)
print(minimum)

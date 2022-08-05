import sys

input = sys.stdin.readline

n, m = map(int, input().split())
num = []


def bt():
    if len(num) == m:
        print(*num)
        return
    for i in range(1, n + 1):
        if i in num:
            continue
        num.append(i)
        if max(num) > i:
            num.pop()
            continue
        bt()
        num.pop()


bt()

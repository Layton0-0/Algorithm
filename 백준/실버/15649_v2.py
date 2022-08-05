import sys

input = sys.stdin.readline


def bt():
    if len(num) == m:
        print("".join(map(str, num)))
        return
    for i in range(1, n + 1):
        if i in num:
            continue
        num.append(i)
        bt()
        num.pop()


n, m = map(int, input().split())
num = []

bt()

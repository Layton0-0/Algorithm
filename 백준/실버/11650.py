import sys

input = sys.stdin.readline

n = int(input().rstrip())
pos = [list(map(int, input().rstrip().split())) for _ in range(n)]
pos.sort(key=lambda x: (x[0], x[1]))

for p in pos:
    x, y = p
    print(x, y)

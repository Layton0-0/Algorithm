import sys
import itertools

input = sys.stdin.readline

n, m = map(int, input().split())
for arr in itertools.permutations([i for i in range(1, n + 1)], m):
    for x in arr:
        print(x, end=" ")
    print()

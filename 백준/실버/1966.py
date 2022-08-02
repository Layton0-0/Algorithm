from collections import deque
import sys

input = sys.stdin.readline

t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    q = deque(map(int, input().split()))
    count = 0
    while q:
        if max(q) == q[0]:
            q.popleft()

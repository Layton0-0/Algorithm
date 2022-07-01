from collections import deque

n, k = map(int, input().split())
MAX = 10 ** 5
count = [0] * (MAX + 1)


def bfs(n, k):
    queue = deque([n])
    while True:
        x = queue.popleft()
        if x == k:
            print(count[x])
            break
        for i in (x - 1, x + 1, 2 * x):
            if 0 <= i <= MAX and not count[i]:
                queue.append(i)
                count[i] = count[x] + 1


bfs(n, k)

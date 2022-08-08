import sys

input = sys.stdin.readline

n = int(input())
chess = [-1] * n
visited = [False] * n
answer = 0


def check(x):
    for i in range(x):
        if chess[x] == chess[i] or abs(chess[x] - chess[i]) == (x - i):
            return False
    return True


def queen(x):
    global answer
    if x == n:
        answer += 1
        return
    # 열
    for i in range(n):
        if visited[i]:
            continue
        chess[x] = i
        if check(x):
            visited[i] = True
            queen(x + 1)
            visited[i] = False


queen(0)
print(answer)

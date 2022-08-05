import sys

input = sys.stdin.readline

n = int(input())
arr = [0] * n
visited = [False] * n
answer = 0


def check(a):
    for i in range(a):
        # 대각선인 좌표는 차의 절댓값이 같다.
        if arr[a] == arr[i] or abs(arr[a] - arr[i]) == a - i:
            return False
    return True


# x는 현재 탐색하고 있는 위치를 뜻함
def bt(x):
    global answer
    if x == n:
        answer += 1
        return
    for i in range(n):
        if visited[i]:
            continue
        arr[x] = i
        if check(x):
            # 자원 낭비 방지를 위해 방문 처리 해줌 -> 시간이 반으로 줄었음
            # 백트래킹을 위해 다시 False로 값 변경해줌
            visited[i] = True
            bt(x + 1)
            visited[i] = False


bt(0)
print(answer)

import sys

input = sys.stdin.readline

sdoku = list(list(map(int, input().split())) for _ in range(9))
n = 9
visited = [[False] * n for _ in range(n)]


def sdo():
    if visited[n - 1][n - 1]:
        return
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                continue
            visited[i][j] = True
            if sdoku[i][j] == 0:
                check_pos(i, j)
                sdo()
                visited[i][j] = False


def check_pos(row, col):
    for x in range(1, n + 1):
        if check_row(row, x) and check_col(col, x) and check_box(row, col, x):
            sdoku[row][col] = x


def check_row(row, x):
    if sdoku[row].count(x) == 0:
        return True
    return False


def check_col(col, x):
    for i in range(n):
        if sdoku[i][col] == x:
            return False
    return True


def check_box(row, col, x):
    for i in range((row // 3) * 3, (row // 3) * 3 + 3):
        for j in range((col // 3) * 3, (col // 3) * 3 + 3):
            if sdoku[i][j] == x:
                return False
    return True


print()
sdo()
for s in sdoku:
    print(*s)

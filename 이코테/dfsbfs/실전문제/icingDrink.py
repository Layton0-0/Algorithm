n, m = map(int, input().split())
icy_box = []
count = 0

for i in range(n):
    icy_box.append(list(map(int, input())))

# 방문 처리는 1로
def dfs(x, y):
    # 판 밖으로 벗어나는 경우 함수 종료
    if x < 0 or x >= n or y < 0 or y >= m:
        return False

    # 처음 만난 덩어리일 경우
    if icy_box[x][y] == 0:
        icy_box[x][y] = 1
        # 상하좌우 방문처리(하위목록까지)해서 한번 검사한 덩어리는 다시 카운트 못하게 함. 촤라락
        dfs(x, y + 1)
        dfs(x, y - 1)
        dfs(x - 1, y)
        dfs(x + 1, y)
        # 재귀가 끝난 후 True를 반환해 함수를 사용하는 곳에서 카운트할 수 있도록 함.
        return True

    # 처음 만난 덩어리 아닐 경우
    return False


# 각 좌표를 처음부터 검사해 덩어리만 카운트해줌.
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            count += 1

print(count)

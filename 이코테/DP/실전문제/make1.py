x = int(input())

d = [0] * 30001

# 점화 트리에서 (최소 + 1)을 구하는 것.
# 내 밑에 일어날 수 있는 횟수 중에 가장 작은 횟수를 찾아 1을 더하면 내 횟수가 됨.
for i in range(2, x + 1):
    d[i] = d[i - 1] + 1
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)

print(d[x])

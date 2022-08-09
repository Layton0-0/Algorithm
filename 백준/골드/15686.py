import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
cities = []
for i in range(n):
    cities.append(list(map(int, input().split())))
home = []
chicken = []
result = 1e9

for i in range(n):
    for j in range(n):
        if cities[i][j] == 1:
            home.append([i, j])
        elif cities[i][j] == 2:
            chicken.append([i, j])

for chick in combinations(chicken, m):
    temp = 0
    for h in home:
        h_r, h_c = h
        c_len = 999999
        for c in chick:
            c_r, c_c = c
            c_len = min(c_len, abs(c_r - h_r) + abs(c_c - h_c))
        temp += c_len
    result = min(temp, result)

print(result)

n, k = map(int, input().split())
a = []
result = 0

for i in range(n):
    a.append(int(input()))

# for i in a[::-1]:
#     print(i)

for i in range(n - 1, -1, -1):
    result += k // a[i]
    k %= a[i]
print(result)

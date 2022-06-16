n = int(input())
k = list(map(int, input().split()))

# k.reverse()
# for i in range(n):
#     print(k[i], end=" ")

# 다른 방법 -> 이게 시간은 더 짧긴 함
for i in range(n - 1, -1, -1):
    print(k[i], end=" ")

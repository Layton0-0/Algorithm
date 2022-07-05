# 대실패. 풀이보다가 파스칼 나오면서 포기
n, k = map(int, input().split())
n_val = 1
store_value = []

for i in range(1, n + 1):
    n_val *= i
    store_value.append(n_val)

answer = (n_val / (store_value[k - 1] * store_value[n - k - 1])) % 1000000007
print(int(answer))

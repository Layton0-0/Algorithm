n, m, k = map(int, input().split())
all_numbers = list(map(int, input().split()))

result = 0
all_numbers.sort(reverse=True)

while m > 0:
    for _ in range(k):
        result += all_numbers[0]
        m -= 1
    result += all_numbers[1]
    m -= 1

print(result)

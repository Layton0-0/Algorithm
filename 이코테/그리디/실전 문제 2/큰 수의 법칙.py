n, m, k = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()
first = nums[n - 1]
second = nums[n - 2]

result = 0

while m != 0:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)

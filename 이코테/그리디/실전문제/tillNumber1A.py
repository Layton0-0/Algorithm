n, k = map(int, input().split())
count = 0

while True:
    # 몫 * 나누는 수 = 나누어 떨어지는 가장 큰 수(목표로 해야하는 수)
    target = (n // k) * k
    # 빼기 횟수 카운트
    count += n - target
    # 빼기 횟수를 카운트 해줬으니 바로 target으로 이동
    n = target

    if n < k:
        break

    n //= k
    count += 1

# n이 0이 돼버려서 1이 될 때까지의 count가 아님. count에 1이 추가돼있으니까 하나 빼주기
count += n - 1
print(count)

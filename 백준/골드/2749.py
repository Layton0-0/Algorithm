# 피사노 주기를 사용해야 함.
# 피보나치 수를 K로 나눈 나머지는 항상 주기를 갖게된다.

n = int(input())
# 나눌 수(K)
mod = 1000000
# 주기 계산
period = 15 * (10 ** 5)  # mod//10*15
# 저장할 피보나치 수열
fibo = [0, 1]

for i in range(2, period):
    # 주기 내의 배열을 저장하기 위함
    fibo.append((fibo[i - 1] + fibo[i - 2]) % mod)

# 주기로 나눈 나머지는 해당 값의 주기 속 위치가 됨.
print(fibo[n % period])

coins = [500, 100, 50, 10]
n = int(input())

count = 0
for coin in coins:
    count += n // coin
    n %= coin

print(count)

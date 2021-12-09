n = int(input())
count = 0

coin_types = [500, 100, 50, 10]

for coin in coin_types:
  count += n // coin # n을 500 등의 화폐단위로 나눠서 몫을 카운트 함.
  n %= coin # 나머지를 저장해 다음 화폐단위가 확인할 수 있도록 함. 

print(count)
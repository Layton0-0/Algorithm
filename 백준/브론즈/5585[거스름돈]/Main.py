pay = int(input())  # 지불할 돈 입력받기

pay = 1000 - pay  # 내야 할 거스름돈 계산
charges = [500, 100, 50, 10, 5, 1]  # 잔돈 단위 리스트로 작성
count = 0  # 잔돈의 개수

for charge in charges:
    count += pay // charge  # 거스름돈을 잔돈으로 나눈 몫 = 그 잔돈 단위가 사용되어야 하는 갯수
    pay = pay % charge  # 나머지 = 앞으로 더 줘야 하는 거스름돈

print(count)

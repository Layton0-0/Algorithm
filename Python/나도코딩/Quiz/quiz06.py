# 당신은 Cocoa 서비스를 이용하는 택시 기사님입니다.
# 50명의 승객과 매칭 기회가 있을 대, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

# 조건 1: 승객 별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
# 조건 2: 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.

# (출력문 예제)
# [0] 1번째 손님 (소요시간: 15분)
# [ ] 2번째 손님 (소요시간: 50분)
# [0] 3번째 손님 (소요시간: 5분)
# ...
# [ ] 50번째 손님 (소요시간: 16분)

# 총 탑승 승객: 2명

from random import *

count = 0
allCustomer = []
selCustomer = []

for i in range(50):
    runtime = randint(5, 50)
    allCustomer.append(runtime)
    if 5 <= runtime <= 15:
        count += 1
        selCustomer.append(runtime)
        print(f"[0] {i+1}번째 손님 (소요시간: {runtime}분)")
        continue
    print(f"[ ] {i+1}번째 손님 (소요시간: {runtime}분)")

print(allCustomer)
print(selCustomer)
print("총 탑승 승객: {0}분".format(len(selCustomer)))
print(f"총 탑승 승객: {count}분")

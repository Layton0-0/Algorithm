from random import *

print(random())  # 0.0 ~ 1.0미만
print(random() * 10)  # 0.0 ~ 10.0미만

print(int(random() * 10))
print(int(random() * 10) + 1)  # 1 ~ 10

print(randrange(1, 46))  # 1 ~ 45 임의 숫자(미만)

print(randint(1, 45))  # 1 ~ 45(이하)

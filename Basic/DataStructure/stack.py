# 추상적 자료구조(ADT)
# 추상 자료형(ADT, Abstract Data Type)이란?

# : 자료구조의 방법이 코드로 정의된 것이 아니라 구조의 행동 양식만 정의된 것

# : 순수하게 기능이 무엇인지 나열한 것(과정은 불포함)

# : 클래스의 함수를 정의하는 것 = 클래스의 추상 자료형을 정의하는 것
# LiFo (Last in First out)

stack = []

stack.append(3)  # [3]
stack.append(6)  # [3, 6]
stack.append(4)  # [3, 6, 4]
stack.pop()  # [3, 6]
stack.append(7)  # [3, 6, 7]
stack.pop()  # [3, 6]

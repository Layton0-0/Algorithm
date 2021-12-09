t = int(input())  # 숫자 입력받음.


buttons = [300, 60, 10]  # 단위가 초이기 때문에 통일
count = []  # 여러 개를 세어야 하기 때문에 리스트 형태로 만듦.


for button in buttons:
    count.append(t // button)  # 숫자를 나누고 몫을 저장.
    t = t % button  # 나머지를 저장


if t != 0:
    print(-1)
else:
    for i in range(3):  # 버튼이 3개라 3번 반복
        print(count[i], end=" ")  # 옆으로 출력하라고 했기 때문​

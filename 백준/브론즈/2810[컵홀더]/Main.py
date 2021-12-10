n = int(input())
seats = str(input())

count = 1  # 맨 왼쪽의 컵홀더를 미리 세어준다.
s = 0  # 좌석 갯수 세는 용도의 변수
l = 0
# 각 좌석 갯수 세기
for i in range(len(seats)):
    if seats[i] == "S":
        s += 1
    else:
        l += 1

count += s + l // 2  # S좌석 갯수 + l좌석의 컵홀더 갯수

if count <= n:
    print(count)
else:  # 사람 수를 구하라고 했기 때문에 최대 인원은 초과할 수 없다.
    print(n)

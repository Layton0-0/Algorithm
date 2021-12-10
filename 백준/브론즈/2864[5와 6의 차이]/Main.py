a, b = map(str, input().split())  # 각각의 값에 접근해야하기 때문에 문자열로 입력받음.

a = a.replace("5", "6")  # 최댓값을 구하기 위해 5를 6으로 전부 변경.
b = b.replace("5", "6")

maxNum = int(a) + int(b)

a = a.replace("6", "5")  # 최솟값을 구하기 위해 6을 5로 전부 변경.
b = b.replace("6", "5")

minNum = int(a) + int(b)

print(minNum, maxNum, end=" ")  # 둘을 나란히 출력

# 삽입 정렬
numbers = [3, 5, 7, 6, 4, 19, 2, 10, 8]

# 0 위치에 있는 항목은 정렬이 되어있다고 가정.
for i in range(1, len(numbers)):
    # i번째 숫자와 그 앞의 숫자들과 비교
    for j in range(i, 0, -1):
        # 뒤의 숫자가 더 작으면 앞과 바꿈.
        if numbers[j - 1] > numbers[j]:
            numbers[j - 1], numbers[j] = numbers[j], numbers[j - 1]
        else:
            break

print(numbers)

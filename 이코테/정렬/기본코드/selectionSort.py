# 선택 정렬
numbers = [3, 7, 1, 9, 11, 10, 5, 4, 2]

for i in range(len(numbers)):
    # 현재 위치(i)와 바꿀 가장 작은 숫자의 인덱스
    min_index = i
    # i까지는 이미 정렬 됐으므로 그 다음부터 검사
    for j in range(i + 1, len(numbers)):
        if numbers[min_index] > numbers[j]:
            min_index = j
    # 위치 바꿔주기
    numbers[min_index], numbers[i] = numbers[i], numbers[min_index]

print(numbers)

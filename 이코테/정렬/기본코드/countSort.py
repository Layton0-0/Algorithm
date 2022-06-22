# 계수 정렬
# 모든 원소의 값이 0보다 크거나 같다고 가정
numbers = [3, 7, 1, 9, 11, 10, 5, 4, 2, 4, 5, 2, 8, 1, 5, 3]
# 모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
count = [0] * (max(numbers) + 1)

# 각 숫자가 나올 때마다 카운트해줌.
for number in numbers:
    count[number] += 1

# 각 인덱스를 카운트된 횟수만큼 출력
for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=" ")

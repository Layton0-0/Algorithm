arr = [1, 2, 3, 4, 5]

# index 접근(0부터 카운트)
print(arr[2])  # 3
# 배열의 길이 출력
print(len(arr))  # 5

# 삽입(맨 끝)
arr.append(6)  # [1, 2, 3, 4, 5, 6]
print(arr)
# 삽입(인덱스, 값)
arr.insert(1, 9)  # [1, 9, 2, 3, 4, 5, 6]
print(arr)

# 삭제(해당 값)
arr.remove(9)  # [1, 2, 3, 4, 5, 6]
print(arr)
# 삭제(인덱스)
del arr[1]  # [1, 3, 4, 5, 6]
print(arr)
arr.pop(0)  # [3, 4, 5, 6]
print(arr)

# 정렬
arr.reverse()  # [6, 5, 4, 3]
print(arr)
arr.sort()  # [3, 4, 5, 6]
print(arr)

# 해당 값이 몇개인지 찾아줌
print(arr.count(4))  # 1

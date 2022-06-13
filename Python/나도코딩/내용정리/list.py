subway = [10, 20, 30]
print(subway)

print(subway.index(20))

# 맨 뒤에 추가
subway.append(90)
print(subway)

# 인덱스 자리에 뒤의 값을 넣음
subway.insert(1, 70)
print(subway)

# 맨 뒤에 하나를 뺌 + 누가 빠졌는지 바로 알 수 있음
print(subway.pop())

# 같은 이름의 사람이 몇 명 있는지 확인
subway.append(30)
print(subway.count(30))

# 정렬도 가능
subway.sort()
print(subway)

# 뒤집기도 가능
subway.reverse()
print(subway)

# 모두 지우기
subway.clear()
print(subway)

# 다양한 자료형 함께 사용 가능
mixedList = ["최윤정", 24, True]
print(mixedList)

# 리스트 확장
subway = [10, 20, 30]
subway.extend(mixedList)
print(subway)

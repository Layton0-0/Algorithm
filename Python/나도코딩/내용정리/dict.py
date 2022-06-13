cabinet = {3: "최윤정", 100: "신대은"}
print(cabinet[100])

# 오류 발생
# print(cabinet[5])
# None 반환
print(cabinet.get(5))
# 값이 없으면 뒤의 값을 반환
print(cabinet.get(5, "사용가능"))
print(cabinet)

print(3 in cabinet)  # True
print(10 in cabinet)  # False

# 값 업데이트 가능
cabinet[100] = "최윤서"
# 값 추가 가능
cabinet[50] = "최오용"
print(cabinet)

# 값 삭제 가능
del cabinet[100]
print(cabinet)

# key들만 출력
print(cabinet.keys())

# values만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# 전부 삭제
cabinet.clear()
print(cabinet)

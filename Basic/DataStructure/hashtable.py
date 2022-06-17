supermarket = {"bread": 1, "juice": 5, "snack": 18}

# key 있는지 검사
if "snack" in supermarket:
    print("snack!")
# value 있는지 검사
if 5 in supermarket.values():
    print("juice!")

# key 출력
print(supermarket.keys())

# values 출력
print(supermarket.values())

# key, value 모두 출력
print(supermarket.items())

# key값으로 value얻기(없으면 None반환)
print(supermarket.get("bread"))

# 키를 통해 값 삭제
del supermarket["bread"]

# 딕셔너리 안의 값 비우기
supermarket.clear()

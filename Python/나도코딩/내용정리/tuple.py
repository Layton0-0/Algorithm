# 값을 변경할 수 없음

menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

# menu.add() -> 불가능

# 그냥 이런게 가능하다~
(name, age, hobby) = ("이름", 0, "취미")
print(name, age, hobby)
(name, age, hobby) = ("이름변경", 0, "취미")

print(name)

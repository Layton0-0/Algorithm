python = "Python is Amazing"

print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))  # 문자열의 길이
print(python.replace("Python", "Java"))  # 문자열에서 앞 단어를 찾아서 뒤로 바꿔줌.

index = python.index("n")  # n이 몇번째에 있는가
print(index)
index = python.index("n", index + 1)
print(index)

print(python.find("Java"))  # 원하는 값이 없으면 -1을 반환
# print(python.index("Java")) # 원하는 값이 없으면 오류를 발생

print(python.count("n"))  # 몇번 발생하는 지

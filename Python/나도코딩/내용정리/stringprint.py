print("a" + "b")  # ab
print("a", "b")  # a b

print("나는 %d살입니다." % 20)  # 정수
print("나는 %s을 좋아해요" % "파이썬")  # 문자열
print("Apple은 %c로 시작해요." % "A")  # 문자

# s 로 전부 가능(자연수도)
print("나는 %s살입니다." % 20)

print("나는 %s색과 %s색을 좋아합니다." % ("파란", "하늘"))

print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란", "하늘"))
print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "하늘"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "하늘"))

print("나는 {age}살이며, {color}색을 좋아합니다".format(age=20, color="하늘"))

# v3.6~
age = 20
color = "하늘"
print(f"나는 {age}살이며, {color}색을 좋아합니다")

# 밑에 애들 지금은 안되는 듯

# \r: 커서를 맨 앞으로 이동
print("Red Apple\rPine")  # PineApple -> 덮어씀

# \b: 백스페이스(한 글자 삭제)
print("Redd\bApple")

# 얘는 됨
print("a\tb")

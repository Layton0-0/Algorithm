# 기본값
def profile1(name, age=17, main_lang="파이썬"):
    print(f"이름: {name}\t나이: {age}\t주 사용 언어: {main_lang}")  # \이렇게 하면 줄바꿈 가능


profile1("유재석")

# 키워드값
def profile2(name, age, main_lang):
    print(f"이름: {name}\t나이: {age}\t주 사용 언어: {main_lang}")  # \이렇게 하면 줄바꿈 가능


profile2(name="유재석", main_lang="파이썬", age=20)


def profile3(name, age, lang1, lang2, lang3, lang4, lang5):
    print(f"이름: {name}\t나이: {age}", end=" ")  # end는 줄바꿈 없이 저 문자를 기준으로 쭉 출력함
    print(lang1, lang2, lang3, lang4, lang5)


profile3("유재석", 20, "Python", "Java", "C", "C++", "C#")

# 가변인자
def profile4(name, age, *language):
    print(f"이름: {name}\t나이: {age}", end=" ")  # end는 줄바꿈 없이 저 문자를 기준으로 쭉 출력함
    for lang in language:
        print(lang, end=" ")
    print()


profile4("유재석", 20, "Python", "Java", "C", "C++", "C#")
profile4("김태호", 25, "Kotlin", "Swift")

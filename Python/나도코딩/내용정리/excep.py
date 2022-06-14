# 기본 에러처리
try:
    print("나누기 할거야")
    num1 = int(input("숫자만 쓰라고 1 : "))
    num2 = int(input("숫자만 쓰라고 2 : "))
    print(num1 / num2)
except ValueError:  # 어떤 에러 처리할건지 자바의 파라미터 느낌
    print("에러에러에러에러에러")
except ZeroDivisionError as err:
    print(err)
except Exception as err:
    print("알 수 없는 에러가 발생함")
    print(err)


class CustomException(Exception):
    def __init__(self, msg):
        self.msg = msg

    # tostring느낌?
    def __str__(self):
        return self.msg


# 에러 발생
try:
    print("한자리 나누기 할거야")
    num1 = int(input("숫자만 쓰라고 1 : "))
    num2 = int(input("숫자만 쓰라고 2 : "))
    if num1 > 10:
        raise CustomException("입력값 틀림 {0} {1}".format(num1, num2))
    print(num1 / num2)
except CustomException as err:
    print("악")
    print(err)
finally:
    print("그럼 이만~~~~")

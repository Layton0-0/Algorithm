gun = 10


def checkpoint(soldiers):
    # 웬만하면 파라미터로 넘겨서 사용할 것! 리턴해서 사용하시오
    global gun  # 전역 공간에 있는 gun을 사용하겠다.
    gun = gun - soldiers
    print(f"함수 내 남은 총: {gun}")


print(f"전체 총: {gun}")
checkpoint(2)
print(f"남은 총: {gun}")

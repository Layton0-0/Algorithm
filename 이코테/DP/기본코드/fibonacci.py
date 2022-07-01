# 피보나치 함수(재귀로 구현 -> 지수 시간 복잡도)
def fibo(x):
    # 첫 번째나 두 번째 일 경우 1을 리턴해버리고(종료 조건)
    if x == 1 or x == 2:
        return 1
    # 그 외의 경우 재귀적으로 그 전 값 더하기
    return fibo(x - 1) + fibo(x - 2)


print(fibo(4))

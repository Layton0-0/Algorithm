n, m = map(int, input().split())
cardNumbers = []
lineNumbers = []
# 2차원 배열 형태로 받기 + 행 별 가장 작은 숫자 저장
for i in range(n):
    cardNumbers.append(list(map(int, input().split())))
    cardNumbers[i].sort()
    lineNumbers.append(cardNumbers[i][0])

# 행 별 가장 작은 숫자 중 가장 큰 수
lineNumbers.sort(reverse=True)

print(lineNumbers[0])

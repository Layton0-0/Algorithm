# 제곱 ㄴㄴ 수

min, max = map(int, input().split())
# 총 숫자 개수에서 빼주는 방식으로 진행
answer = max - min + 1
whole = [True] * answer

# 에라토스테네스의 체 이용 -> max까지 중에서 절반(제곱근까지)만 탐색해도 됨
# 1, 2, 3은 어차피 해당이므로 4부터 순차적으로 뒤를 지워나감
for i in range(2, int(max ** 0.5) + 1):
    sq = i ** 2
    # min 이상인 수 중 제곱근(sq)의 배수의 최소값
    # min에서 1을 빼고 계산한 이유는 자신이 제곱근의 배수일 경우를 포함시키기 위함
    # 제곱근(sq)의 배수의 최솟값부터 제곱근(sq)씩 증가시키며 범위 내 모든 해당 숫자 방문처리 + 정답 갯수 지워나감
    for j in range(((min - 1) // sq + 1) * sq, max + 1, sq):
        if whole[j - min]:
            whole[j - min] = False
            answer -= 1

print(answer)

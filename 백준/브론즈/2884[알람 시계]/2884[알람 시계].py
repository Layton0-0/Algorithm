h, m = map(int, input().split())

if h == 0 and m < 45:  # h값이 음수가 나오지 않게 조건 설정
    h = 24

result = h * 60 + m - 45  # 분으로 단위를 통일하고, 45분 빠른 시간을 계산
h = result // 60
m = result % 60

print(h, m)

print("python", "java", sep=" vs ", end="?")
print("end는 뒷 문장과 이어짐")

import sys

print("Python", "Java", file=sys.stdout)
print("Python", "Java", file=sys.stderr)

# 출력 정렬 ljust, rjust
scores = {"수학": 0, "영어": 50, "코딩": 100}
for subject, score in scores.items():
    # 8칸 확보한 상태로 왼쪽 정렬 / 4칸 확보한 상태로 오른쪽 정렬
    print(subject.ljust(8), str(score).rjust(4), sep=":")

# 숫자 정형화 zfill()
for num in range(1, 21):
    print("대기번호: " + str(num).zfill(3))

# 빈 자리는 빈 공간으로 두고, 오른쪽 정렬을 하되, 총 10자리를 확보
print("{0: >10}".format(500))
# 양수일 땐 +, 음수일 땐 - 함께 출력
print("{0: >+10}".format(500))
print("{0: >-10}".format(-500))
# 왼쪽 정렬하고 빈칸을 _로 채움
print(("{0:_<10}".format(500)))
# 3자리마다 ,를 찍어주기
print("{0:,}".format(100000000000))
# 3자리마다 ,를 찍어주고 +- 부호도 붙이기
print("{0:+,}".format(+100000000000))
print("{0:-,}".format(-100000000000))
# 3자리마다 ,를 찍어주고 +- 부호도 붙이고 자릿수 확보하기
print("{0:^<+30,}".format(10000000000000000))
# 소수점 출력
print("{0:f}".format(5 / 3))
# 부동 소수점 출력(반올림)
print("{0:.2f}".format(5 / 3))

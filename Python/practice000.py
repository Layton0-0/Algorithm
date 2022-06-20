import sys

# 엔터를 \n으로 받지 않기 위해 공백을 없애는 rstrip함수를 사용한다.
data = list(map(int, sys.stdin.readline().rstrip().split()))
print(data)

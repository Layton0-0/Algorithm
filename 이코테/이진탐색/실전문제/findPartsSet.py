# set을 이용한 검색
n = int(input())
have_parts = set(map(int, input().split()))

m = int(input())
request_parts = list(map(int, input().split()))

for request_part in request_parts:
    if request_part in have_parts:
        print("yes", end=" ")
    else:
        print("no", end=" ")

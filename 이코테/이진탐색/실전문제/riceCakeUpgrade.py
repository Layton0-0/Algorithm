# 입력값의 양이 어마무시할 경우 웬만하면 이진 탐색이라고 보면 됨.
import sys

n, m = map(int, input().split())
rice_cakes = list(map(int, sys.stdin.readline().rstrip().split()))

start = 0
end = max(rice_cakes)

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for rice_cake in rice_cakes:
        # 떡 차이 저장
        if rice_cake > mid:
            total += rice_cake - mid
    # 떡 양이 모자라면 떡을 더해야 하니 끝점을 앞으로 땡김
    if total < m:
        end = mid - 1
    # 떡 양이 충분한 경우 떡을 덜해야 하니 시작점을 뒤로 땡김
    else:
        # 덜 잘랐을 때를 정답으로 제출해야 하므로 기록.
        result = mid
        start = mid + 1

print(result)

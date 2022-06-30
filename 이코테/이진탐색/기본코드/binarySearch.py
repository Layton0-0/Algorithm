# 재귀함수 버전
def binary_search(array, target, start, end):
    # 탐색할 곳이 안 남으면 None반환
    if start > end:
        return None
    mid = (start + end) // 2
    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    # 목표값이 중간점의 값보다 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    # 목표값이 더 크면 오른쪽 확인
    else:
        return binary_search(array, target, mid + 1, end)


n, target = list(map(int, input().split()))

array = list(map(int, input().split()))

result = binary_search(array, target, 0, n - 1)
if result == None:
    print("원소가 없음")
else:
    print(result + 1)

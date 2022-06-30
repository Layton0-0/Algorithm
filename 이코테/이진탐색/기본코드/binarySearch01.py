# 반복문 버전
def binary_search(array, target, start, end):
    while start <= end:
        # 중간점 지정(나머지 버림)
        mid = (start + end) // 2
        # 찾는 숫자가 중간점에 있다면 인덱스 반환
        if array[mid] == target:
            return mid
        # 찾는 숫자가 더 작으면 끝점 이동
        elif array[mid] > target:
            end = mid - 1
        # 찾는 숫자가 더 크면 시작점 이동
        else:
            start = mid + 1
    return None


n, target = list(map(int, input().split()))

array = list(map(int, input().split()))

result = binary_search(array, target, 0, n - 1)
if result == None:
    print("원소가 없음")
else:
    print(result + 1)

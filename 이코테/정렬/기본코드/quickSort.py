# 퀵 정렬
numbers = [3, 7, 1, 9, 11, 10, 5, 4, 2]


def quick_sort(array, start, end):
    # 원소가 1개인 경우 종료
    if start >= end:
        return
    # 피벗은 1번째 원소(인덱스)
    pivot = start

    # 피벗 다음 요소부터라 start + 1(인덱스)
    left = start + 1
    right = end

    # 두 뭉텅이로 나누어질 때까지 반복
    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        # 끝에 도달하기전, 자신의 값이 피벗보다 아직 작을 때까지 이동.
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1
        # 둘이 교차했을 경우, 작은 데이터(right)과 피벗 교체
        if left > right:
            array[pivot], array[right] = array[right], array[pivot]
        # 교차하지 않았으면 서로(left, right)를 교체
        else:
            array[left], array[right] = array[right], array[left]

    # 분할한 후 양 쪽에서 각각 정렬 수행 -> 재귀 활용
    # 마지막에 pivot과 right의 위치가 바껴서 pivot대신 right을 기준으로 사용
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)


quick_sort(numbers, 0, len(numbers) - 1)
print(numbers)

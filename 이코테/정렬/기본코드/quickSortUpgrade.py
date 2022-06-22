# 퀵 정렬 업그레이드
numbers = [3, 7, 1, 9, 11, 10, 5, 4, 2]


def quick_sort(array):
    # 리스트가 하나 이하의 원소를 담고 있다면 종료
    if len(array) <= 1:
        return array
    # 피벗은 첫번째 원소
    pivot = array[0]
    # 피벗을 제외한 리스트
    tail = array[1:]

    # 피벗 제외 리스트에서 피벗보다 작거나 같은 수를 발견하면 저장
    left_side = [x for x in tail if x <= pivot]
    # 피벗 제외 리스트에서 피벗보다 큰 수를 발견하면 저장
    right_side = [x for x in tail if x > pivot]

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행하고, 전체 리스트를 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)


print(quick_sort(numbers))

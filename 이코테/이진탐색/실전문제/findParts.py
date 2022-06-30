import sys


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


n = int(input())
have_parts = sys.stdin.readline().split()
m = int(input())
request_parts = sys.stdin.readline().split()

have_parts.sort()

for request_part in request_parts:
    target_index = binary_search(have_parts, request_part, 0, n - 1)
    if target_index == None:
        print("no", end=" ")
    else:
        print("yes", end=" ")

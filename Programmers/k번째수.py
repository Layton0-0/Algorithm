def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command
        slice_arr = array[i - 1 : j]
        slice_arr.sort()
        answer.append(slice_arr[k - 1])

    return answer

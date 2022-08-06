def solution(tasks):
    answer = 0
    tasks.sort()
    s_task = set(tasks)
    for t in s_task:
        c = tasks.count(t)
        temp = c % 3
        while temp < c:
            if temp >= c:
                return -1
            if temp % 2 == 0:
                answer += ((c - temp) // 3) + (temp // 2)
                break
            else:
                temp += 3

    return answer


arr = [1, 1, 2, 3, 3, 2, 2]
arr_1 = [4, 1, 1, 1, 1, 2, 3]
print(solution(arr_1))

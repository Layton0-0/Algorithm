def solution(numbers, target):
    answer = 0
    result = 0

    def dfs(n):
        nonlocal numbers
        nonlocal result
        nonlocal answer
        if n == len(numbers):
            if result == target:
                answer += 1
            return
        for _ in range(2):
            result += numbers[n]
            dfs(n + 1)
            result -= numbers[n]
            numbers[n] *= -1

    dfs(0)
    return answer

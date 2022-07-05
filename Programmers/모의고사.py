def solution(answers):
    answer = []
    count = [0, 0, 0]
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for i in range(1, len(answers) + 1):
        if answers[i - 1] == one[i % len(one) - 1]:
            count[0] += 1
        if answers[i - 1] == two[i % len(two) - 1]:
            count[1] += 1
        if answers[i - 1] == three[i % len(three) - 1]:
            count[2] += 1
    max_count = max(count)
    answer = [i + 1 for i, v in enumerate(count) if v == max_count]

    return answer

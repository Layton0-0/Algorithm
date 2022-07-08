def solution(a, b):
    answer = ""
    week = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # a-1까지의 날짜를 다 더해주고 b일 만큼 더해서 총 날을 구함
    # 그 값을 7로 나눠 몇 번째 요일인지 week에서 찾음
    # 정답 반환
    answer = week[(sum(days[: a - 1]) + b) % 7]

    return answer

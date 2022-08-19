from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []
    for k in course:
        temp = []
        for menus in orders:
            for m in combinations(menus, k):
                m = "".join(sorted(m))
                temp.append(m)
        temp = Counter(temp).most_common()
        answer += [menu for menu, cnt in temp if cnt > 1 and cnt == temp[0][1]]
    return sorted(answer)


## 풀이

# Counter 라이브러리는 요소의 갯수를 세어 딕셔너리 형태로 반환해주는 라이브러리이다.

# 해당 라이브러리를 모른 상태로 문제를 풀 때 Counter에 해당하는 기능을 직접 구현하다 포기하였다.

# 1. 요청 course의 길이 만큼의 조합을 만든다.
# 2. 각 조합을 정렬하여 문자열로 만든 후 전부 한 배열에 저장한다.
# 3. 각 문자열의 갯수를 세어준다. 이 때 Counter를 사용해 빈도수가 높은 순으로 저장한다.
# 4. 빈도수가 2이상이고 가장 높은 빈도수의 문자열들을 전부 정답 배열에 저장한다.
# 5. 마지막으로 정답 배열을 오름차순으로 정렬해준다.

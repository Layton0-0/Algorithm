# 풀이 베껴옴
# Counter는 요소의 갯수를 세어주는 라이브러리(딕셔너리로 반환)
from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []
    # 갯수 별로 체크
    for k in course:
        candidates = []
        # 각 문자열 탐색
        for menu_li in orders:
            # 문자열에서 k개의 조합을 탐색
            for li in combinations(menu_li, k):
                # 모든 조합을 저장해줌
                res = "".join(sorted(li))
                candidates.append(res)
        # 조합을 빈도수로 정렬
        sorted_candidates = Counter(candidates).most_common()
        # 한 번 이상 나왔고, 가장 높은 빈도수의 후보를 전부 정답 처리
        answer += [
            menu
            for menu, cnt in sorted_candidates
            if cnt > 1 and cnt == sorted_candidates[0][1]
        ]
    return sorted(answer)

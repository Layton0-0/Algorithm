def solution(N, stages):
    result = {}
    # 나눌 수
    denominator = len(stages)
    # 스테이지 수는 최대 500개이므로 하나씩 검사해도 된다
    for stage in range(1, N + 1):
        if denominator != 0:
            # 스테이지의 사용자 수 카운트
            count = stages.count(stage)
            # key: stage, value: count/denominator
            # 스테이지 번호를 key로, 실패율을 value로 저장
            result[stage] = count / denominator
            # 해당 스테이지의 사용자 수만큼 빼주면 다음 스테이지까지 도달한 사람 수를 저장 가능
            denominator -= count
        else:
            # 더이상 도달한 사람이 없으면 그 때부터는 다 0처리
            result[stage] = 0
    # sorted에 result를 그냥 넘기면 result의 key가 들어간다.
    # result[key] = value니까 value의 순서대로 정렬이 되는거.
    return sorted(result, key=lambda x: result[x], reverse=True)

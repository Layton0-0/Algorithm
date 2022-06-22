array = [("바나나", 2), ("사과", 5), ("옥수수", 1)]

# 정렬 기준을 세우는 함수
def setting(data):
    # 2번째 원소를 정렬 기준으로 삼음.
    return data[1]


result = sorted(array, key=setting)
print(result)

# 집합(set)
# 중복 안됨, 순서 없음

mySet = {1, 2, 3, 3, 3}
print(mySet)

java = {"유재석", "김태호", "양세형"}
listt = ["유재석", "박명수", "박명수"]
python = set(listt)
print(python)

# 교집합
print(java & python)
print(java.intersection(python))

# 합집합
print(java | python)
print(java.union(python))

# 차집합
print(java - python)
print(java.difference(python))

# set에 값 추가
python.add("김태호")
print(python)

# set에서 값 빼기
java.remove("김태호")
print(java)

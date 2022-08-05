import itertools

data = [1, 2, 3]

# 순서 상관없이(순열)
for x in itertools.permutations(data, 2):
    print(list(x))

print()

# 순서 상관있음(조합) -> 내부 오름차순
for x in itertools.combinations(data, 2):
    print(list(x))
print(list(itertools.combinations(data, 2)))
for x in itertools.combinations_with_replacement("ABCD", 3):
    print(x)

print(len(list(itertools.combinations_with_replacement("ABCD", 3))))

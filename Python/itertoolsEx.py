from itertools import combinations, permutations

arr = ["A", "C", "B", "G", "F"]
s = "ACBDSAFSAI"

for i in combinations(arr, 3):
    print(i)

print()

for i in permutations(arr, 3):
    print(i)

print()
for i in combinations(s, 3):
    print(i)

# 제곱 ㄴㄴ 수

min, max = map(int, input().split())
whole = [True for _ in range(min, max + 1)]
count = 0

for i in range(min, max + 1):
    if whole[i - min]:
        j = 1
        k = 1
        while (j ** 2) * k <= max:
            for j in range(1, k + 1):
                whole[(j ** 2) * k] = False
            k += 1

for w in whole:
    if w:
        count += 1

print(count)

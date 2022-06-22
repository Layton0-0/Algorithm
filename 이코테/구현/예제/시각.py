n = int(input())
count = 0
# 싹 다 검사하는 방식
for i in range(n + 1):
    for j in range(60):
        for k in range(60):
            # if (
            #     i % 10 == 3
            #     or j % 10 == 3
            #     or k % 10 == 3
            #     or j // 10 == 3
            #     or k // 10 == 3
            # ):
            # 3이 포함되어 있다면 -> 효율적인 버전
            if "3" in str(i) + str(j) + str(k):
                count += 1

print(count)

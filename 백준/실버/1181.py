import sys

input = sys.stdin.readline

n = int(input())
words = [input().rstrip() for _ in range(n)]
words = set(words)

words = sorted(words, key=lambda x: (len(x), x))

for word in words:
    print(word)

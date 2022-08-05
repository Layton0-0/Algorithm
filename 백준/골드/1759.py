import sys
import itertools

input = sys.stdin.readline

l, c = map(int, input().split())
s = input().split()
s.sort()

for i in itertools.combinations(s, l):
    a_count = i.count("a") + i.count("e") + i.count("i") + i.count("o") + i.count("u")

    if a_count >= 1 and a_count <= l - 2:
        print("".join(i))

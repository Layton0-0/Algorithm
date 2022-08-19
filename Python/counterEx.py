from collections import Counter

arr = ["hi", "hello", "hi", "hey", "hello", "hi"]
c = Counter(arr)
print(c.most_common())
print(c.values())
print(c.items())
print(c.setdefault(0))
print()

s = "acadbca"
c = Counter(s)
print(c.most_common())
print(c.values())
print(c.items())
print(c.setdefault(0))
print()

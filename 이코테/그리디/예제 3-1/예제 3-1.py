n = int(input())
i = 0

while 1:
    if n >= 500:
        n -= 500
        i += 1
    elif n >= 100:
        n -= 100
        i += 1
    elif n >= 50:
        n -= 50
        i += 1
    elif n >= 10:
        n -= 10
        i += 1
    else:
        break

print(i)

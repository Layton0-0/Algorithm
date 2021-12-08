maxNum = int(input())
num = 0
sumNum = num

while 1:
  num += 1
  sumNum += num
  if maxNum <= sumNum:
    print(num)
    break
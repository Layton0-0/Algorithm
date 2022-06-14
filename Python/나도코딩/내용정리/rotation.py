for waiting_no in [0, 1, 2, 3, 4]:
    print(waiting_no)

for waiting_no in range(5):  # 0, 1, 2, 3, 4
    print(waiting_no)

for waiting_no in range(1, 6):  # 1, 2, 3, 4, 5
    print(waiting_no)

starbucks = ["아이언맨", "토르", "그루트"]
for customer in starbucks:
    print(customer)

# 한 줄 for문
students = [1, 2, 3, 4, 5]
students = [i + 100 for i in students]
print(students)

students = ["Iron man", "Thor", "Groot"]
students = [len(man) for man in students]
print(students)

students = ["Iron man", "Thor", "Groot"]
students = [man.upper() for man in students]
print(students)

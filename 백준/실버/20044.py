n = int(input())
people = list(map(int, input().split()))

people.sort()

teams = []
for i in range(n):
    teams.append(people[i] + people[-(i + 1)])

teams.sort()

print(teams[0])

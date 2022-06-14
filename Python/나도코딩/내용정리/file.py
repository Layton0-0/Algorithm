# Create
score_file = open("score.txt", "w", encoding="utf8")
print("수학: 100", file=score_file)
print("영어: 90", file=score_file)
score_file.close()

# Update
score_file = open("score.txt", "a", encoding="utf8")
score_file.write("과학: 80")
# write는 줄바꿈이 따로 없음
score_file.write("\n코딩: 100")
score_file.close()

# Read
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline())  # 줄별로 읽기, 한줄 읽고 커서는 다음줄로 이동
while True:
    line = score_file.readline()
    if not line:
        break
    print(line)
# print(score_file.read())
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines()
for line in lines:
    print(line)
score_file.close()

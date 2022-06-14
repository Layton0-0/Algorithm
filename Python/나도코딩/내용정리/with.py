import pickle

# 따로 close 해주지 않아도 알아서 종료됨.
with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))

with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("write 하는 중")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())

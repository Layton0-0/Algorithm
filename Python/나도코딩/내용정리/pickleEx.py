# 데이터를 파일로 저장하는 것 = pickle
# 저장하려는 파일명과 py 파일명이 같으면 안됨.
import pickle

# Create
profile_file = open("profile.pickle", "wb")  # write binary 형태
profile = {"이름": "박명수", "나이": 30, "취미": ["축구", "야구", "코딩"]}
print(profile)
pickle.dump(profile, profile_file)  # profile에 있는 정보를 file에 저장
profile_file.close()

# Read
profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file)  # file에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close()

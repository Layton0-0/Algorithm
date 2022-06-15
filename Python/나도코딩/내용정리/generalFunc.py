# 내장함수

# input : 사용자 입력을 받는 함수
# dir: 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
print(dir())  # 기본 내장함수만 나옴
import random  # 외장함수

print(dir())  # random 추가돼서 나옴
lst = [1, 2, 3]
print(dir(lst))  # lst에 대해서 쓸 수 있는 함수가 쭉 나옴

name = "윤정"
print(dir(name))

# 외장함수 : 직접 import해서 사용해야함.

# glob: 프로젝트 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir)
import glob

print(glob.glob("*.txt"))  # 프로젝트 경로 내 가장 바깥 쪽에 확장자가 txt인 모든 파일

# os: 운영체제에서 제공하는 기본 기능
import os

print(os.getcwd())  # 현재 디렉토리

folder = "sample_dir"

if os.path.exists(folder):
    print("이미 존재하는 폴더임")
    os.rmdir(folder)
    print(folder, "폴더를 삭제하였습니다")
else:
    os.makedirs(folder)
    print(folder, "폴더를 생성하였습니다")

print(os.listdir())

# time: 시간 관련 함수
import time

print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S"))

import datetime

print(datetime.date.today())
print(datetime.datetime.now())

# timedelta: 두 날짜 사이의 간격
today = datetime.date.today()  # 오늘 날짜 저장
td = datetime.timedelta(days=100)  # 100일이라는 날짜를 저장
print(today + td)

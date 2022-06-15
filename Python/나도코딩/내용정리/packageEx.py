# 모듈들을 모아놓은 것 -> 패키지
import travel.thailand

letsgo = travel.thailand.ThailandPackage

letsgo.start()

from travel.thailand import ThailandPackage as th

th.start()

# __init__.py의 __all__의 배열 안에 쓸 패키지를 정의해줘야함.
from travel import *

trip = thailand.ThailandPackage
trip.start()

import inspect
import random

# 패키지 모듈 위치 출력 방법
print(inspect.getfile(random))
print(inspect.getfile(thailand))

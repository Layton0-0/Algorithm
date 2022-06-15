# 부품만 교체하기 위한 용도 -> 모듈
# 같은 파일 안에 있어야 함

# 기본 불러오기
import moduleEx_module

moduleEx_module.price(90)

# 별칭 지정 가능
import moduleEx_module as mv

mv.price(30)

# 이렇게 불러오면 .적어줄 필요도 없다.
from moduleEx_module import *

price(20)

# 원하는 애들만 불러올 수도 있음 + 별칭 지정 가능
from moduleEx_module import price_morning, price

price_morning(80)

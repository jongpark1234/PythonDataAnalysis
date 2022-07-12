# 시리즈 연산
# 벡터화 연산 가능
# value에 대해서만 연산 가능, index는 연산 대상이 아님
# index 값은 불변

import pandasex01 as ex01
import pandas as pd

div = ex01.city / 1000000
print(div)

# 시리즈 인덱싱
# numpy 인덱싱 사용 가능, 인덱스 라벨을 이용한 인덱싱도 가능
# 배열 인덱싱이나 인덱스 라벨을 이용한 슬라이싱도 가능

print(ex01.city['부산']) # 부산의 인구
print(ex01.city[3]) # 부산의 인구

print(ex01.city[1], ex01.city['대전']) # 대전의 인구
print(ex01.city[0], ex01.city['대구']) # 서울의 인구, 대구의 인구

print(ex01.city[[0, 3, 1]]) # 서울, 부산, 대전의 정보
print(ex01.city[['서울', '부산', '대전']]) # 서울, 부산, 대전의 정보

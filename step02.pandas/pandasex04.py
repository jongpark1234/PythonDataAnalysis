# 데이터 프레임 -> 표
# 시리즈 : 1차원 벡터 데이터에 행방향 인덱스를 붙인 것

import numpy as np
import pandas as pd
from pandas import DataFrame

print('데이터 프레임 생성 1')
# 1. 하나의 열이 되는 데이터를 리스트나 1차원 배열로 준비
# 2. 각각의 열에 대한 이름을 키로 가지는 딕셔너리 만들기
# 3. 이 데이터를 데이터프레임 클래스의 생성에 넣어주기
# 4. 열방향 인덱스는 column 인수
# 5. 행방향 인덱스는 index 인수로 지정하기

df = DataFrame(['뽀로로', '페티', '크롱', '루피', '에디'])
print(df)

df = DataFrame({'name' : ['뽀로로', '페티', '크롱', '루피', '에디']}, index = ['no1', 'no2', 'no3', 'no4', 'no5'])
print(df)

df = DataFrame({'name' : ['뽀로로', '페티', '크롱', '루피', '에디'], 'id' : ['pororo', 'paty', 'cron', 'rupy', 'edi']}, index = ['no1', 'no2', 'no3', 'no4', 'no5'])
print(df)


data = {
    '2015' : [9904312, 3448737, 2890451, 2466052],
    '2010' : [9631482, 3393191, 2632035, 3431774],
    '2005' : [9762546, 3512547, 2517680, 2456016],
    '2000' : [9853972, 3655437, 2466338, 2473990],
    '지역' : ['수도권', '경상권', '수도권', '경상권'],
    '2010-2015증가율' : [0.0238, 0.0163, 0.0982, 0.0141]
}
columns = ['지역', '2015', '2015', '2005', '2000', '2010-2015증가율']
index = ['서울', '부산', '인천', '대구']
df = DataFrame(data, index = index, columns = columns)

print(df)

print(df.values)
print(df.columns)
print(df.index)

df.index.name = '도시'
df.columns.name = '특성'

print(df)

# 데이터프레임 열 인덱싱

print(df['지역'])
print(type(df['지역'])) # <class 'pandas.core.series.Series'>


# 인덱싱에서 [] 을 한 세트로 사용하면 시리즈로
# [][] 두 세트로 인덱싱을 하면 데이터프레임으로 결과 리턴

# 데아터프레임의 열 인덱스가 문자열 라벨을 가지고 있는 경우에는
# 순서를 나타내는 정수 인덱스를 열 인덱싱에 사용 불가
# 정수 인덱싱은 행 인덱싱에 사용

# print(df[0]) # 정수 열 인덱싱은 에러

# 행 인덱싱은 항상 슬라이싱을 해야함. 시리즈 처럼 라벨슬라이싱
print(df[-1:])
print(df[:1])
print(df[1:3])

print(df['부산':'대구']) # 마지막 위치 '대구'는 inclusive

# 데이터프레임 열 데이터 갱신 추가 삭제

df['2010-2015증가율'] *= 100

print(df)

del df['2010-2015증가율'] # 삭제
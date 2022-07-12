# 대부분의 데이터는 시계열 ( Series ) 또는 표 ( Table ) 의 형태로 나타낼 수 있는데 pandas 패키지에서는
# Series 와 DataFrame 을 제공한다.

# 시리즈 클래스 : numpy의 1차원 배열과 비슷하지만 데이터의 의미를 표시하는 index 를 붙일 수 있고 데이터 자체는 value 라고 표현

import pandas as pd

# 시리즈 생성 : 데이터를 리스트나 1차원 배열 형식으로 Series 생성자에 넣어주면 객체 완성

city = pd.Series([9875426, 1502227, 2475231, 3470653], index=['서울', '대전', '대구', '부산'])
print(city)

# '서울', '대전', '대구', '부산' 을 인덱스 라벨
# 인덱스 라벨은 문자열, 정수, 날짜, 시각 등을 사용

# 인덱스 미지정 시리즈는 인덱스가 0부터 시작하는 정수값

print(pd.Series(range(10, 14)))

# 시리즈의 인덱스는 index 속성으로 접근 
# 시리즈 값은 1차원 배열이며 values 속성으로 접근 가능

print(city.index)
print(city.values)

city.name = '도시별 인구수'
city.index.name = '도시'

print(city)
print(type(city)) # <class 'pandas.core.series.Series'>


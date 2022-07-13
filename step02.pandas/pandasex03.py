# 시리즈와 딕셔너리 자료형
# 라벨을 키로 가지는 딕셔너리 구조와 동이
# 딕셔너리 자료형의 in 연산, item 메소드 를 사용하여
# for 루프를 이용하여 키, 밸류에 접근이 가능

import pandas as pd
import pandasex01 as ex01

print('서울' in ex01.city) # True
print('광주' in ex01.city) # False

for k, v in ex01.city.items():
    print(k, v)

city = pd.Series({'서울' : 10022181, '대전' : 1518775, '대구' : 2487892, '부산' : 3513777}, index = ['서울', '대전', '대구', '부산'])

print(city)

dist1 = ex01.city - city # 인덱스 기반 연산
dist2 = ex01.city.values - city.values # 인덱스 기반 연산 ( 값만 가져옴 )

print(f'인구증감수 : \n{dist1}')
print(f'인구증감수 : \n{dist2}') # ndarray


city = pd.Series({'서울' : 10022181, '대전' : 1518775, '대구' : 2487892, '부산' : 3513777}, index = ['대전', '서울', '대구', '부산'])
print(ex01.city.values - city.values)


city = pd.Series({'서울' : 10022181, '대전' : 1518775, '대구' : 2487892, '부산' : 3513777, '인천' : 2925815}, index = ['대전', '서울', '대구', '부산', '인천'])
dist = ex01.city - city
print(dist) # 연산을 수행할 대상이 없는 경우에는 NaN

print(dist.notnull()) # 널이 아닌 대상은 True, 아니라면 False
print(dist[dist.notnull()]) # 널이 아닌 대상은 True, 아니라면 False

# 문제. 인구 증가율을 계산하시오.

city1 = pd.Series({'서울' : 1000, '대구' : 53200, '부산' : 3200}, index = ['서울', '대구', '부산'])
city2 = pd.Series({'서울' : 3754, '대구' : 100132, '부산' : 6614}, index = ['서울', '대구', '부산'])

dist = (city2 - city1) / city1 * 100
print(dist)


dist['부산'] = -1.23
print(dist)

del dist['서울']
print(dist)

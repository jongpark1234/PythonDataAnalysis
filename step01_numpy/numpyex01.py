# numpy : 수치해석용 파이썬 패키지
# 다차원 배열 자료구조인 ndarray 클래스 지원
# 벡터와 행렬을 사용하는 선형 대수 계산에 주로 사용

# numpy 배열 연산은 c 언어로 구현된 내부 반복문 사용
# 벡터화 연산을 이용하여 선형 대수 연산 가능
# 배열 인덱싱을 사용한 질의 기술을 이용하여 복잡한 수식을 계산

import numpy as np

line = lambda: print('-' * 50)

# 1차원 배열
# numpy의 array()에 리스트 자료형의 데이터를 넣으면 numpy 배열로 변환
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(arr)
print(type(arr)) # ndarray 자료형. list 와는 다름

line()

# 벡터화 연산 ( vectorized operation )
data = list(range(10))
# 1. for문을 사용하여 계산 수행
answer = []
for di in data:
    answer.append(di * 2)
print(f'data의 배수 : {answer}')
print(f'연산 : {data * 2}')

line()

# 2. 벡터화 연산
x = np.array(data)
print(f'벡터화 연산 : {x * 2}')
# 벡터화 연산은 비교연산과 논리연산을 포함한 모든 종류의 수학 연산에 사용 가능

line()

# 3. 벡터화 연산 ( 비교, 논리 연산 )
a, b = np.array([1, 2, 3]), np.array([10, 20, 30])
print(a * 2 + b)
print(f'a == 2 ? : {a == 2}') # False True False

# 문제 1. a > 10 인가?
# 문제 2. a는 2 이거나 10보다 큰가?
print(a > 10) # 1
print((a == 2) + (a > 10))

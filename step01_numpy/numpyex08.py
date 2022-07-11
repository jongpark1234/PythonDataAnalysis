# numpy가 제공하는 배열 생성 명령

import numpy as np

# zeros() : 크기가 정해져있는 모든 값이 0인 배열 ( 인수는 배열의 크기 )
# ones() : 크기가 정해져있는 모든 값이 1인 배열 ( 인수는 배열의 크기 )

z_arr = np.zeros(5)
print(z_arr) # [0. 0. 0. 0. 0.]
print(z_arr.dtype) # float64

z_2darr = np.zeros((2, 3)) # 2x3 크기의 0으로 채워진 배열 생성
print(z_2darr)

# dtype 인수를 명시하면 원하는 자료형 원소를 가진 배열 생성
z_2darr = np.zeros((5, 2), dtype='i')
print(z_2darr.dtype) # int32

str_arr = np.zeros(5, dtype='U') # dtype 의 U 는 대문자로 작성하여야 함.
print(str_arr) # ['' '' '' '' '']

str_arr[0] = '가나다'
str_arr[1] = 'abc'
str_arr[2] = 'abcd'
print(str_arr) # ['가' 'a' 'a' '' '']

o_arr = np.ones(5, dtype='i8') # dtype 을 int64 로 초기화
print(o_arr) # [1 1 1 1 1]
print(o_arr.dtype) # float64

# 배열의 크기가 큰 경우 값의 초기화 없이 기억공간 확보만 하는 경우

e_ar = np.empty((4, 3))
print(e_ar) # 쓰레기 값들로 채워짐

# empty() 를 사용할 때 dtype을 사용하면 값을 초기화 하는 것과 동일한 효과

aran1 = np.arange(10)
print(aran1) # [0 1 2 3 4 5 6 7 8 9]

aran2 = np.arange(3, 21, 2) # 마지막 값은 미포함
print(aran2) # [3 5 7 9 11 13 17 19]

lin_sp = np.linspace(0, 100, 5, dtype='i8') # 마지막 값 포함
print(lin_sp) # [0 25 50 75 100]

log_sp = np.logspace(0.1, 1, 5) # 마지막 값 포함
print(log_sp) # [1.25892541, 2.11348904, 3.54813389, 5.95662144 10.]

# 전치연산
# 2차원 배열에 대하여 행과 열을 바꾸는 연산
# 배열의 T 속성으로 구할 수 있음
# method 가 아니고 attr 이다.

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr) # 2x3 [[1, 2, 3], [4, 5, 6]]
print(arr.T) # 3x2 [[1, 4], [2, 5], [3, 6]]

# 배열의 크기 변환 

a = np.arange(12)
print(a) # 1x12 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

b = a.reshape(3, 4)
print(b) # 1x12 [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]]

print(a.reshape(4, -1)) # 4x3 ( 열의 크기는 자동 맞춤 )
print(a.reshape(-1, 6)) # 2x6 ( 행의 크기는 자동 맞춤 )
b = a.reshape(2, 2, -1) # 2x2x3 ( 깊이와 행의 크기는 2, 열의 크기는 자동 맞춤 )

# 다차원 배열을 1차원으로 펼치기
print(b.flatten())
print(b.revel())


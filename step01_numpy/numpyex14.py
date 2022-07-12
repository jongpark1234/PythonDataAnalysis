# 차원 축소 연산
# 행렬에서 하나의 행에 있는 원소를 하나의 데이터 집합으로 보고
# 그 집합의 평균을 구하면 행 병로 하나의 숫자가 나오게 됨
# 10x5 크기의 2차원 배열에 대하여 각 행별로 평균을 구하면 10개의 숫자를 가지는 1차원 벡터가 나옴 -> 차원 축소 연산.

import numpy as np

x = np.array([1, 2, 3, 4])
print(x.sum()) # 10
print(np.sum(x)) # 10

x = np.array([1, 3, 2])
print(x.min()) # 1
print(x.max()) # 3

print(x.argmax()) # 1 ( 최대값의 위치 )
print(x.argmin()) # 0 ( 최소값의 위치 )

x = np.array([1, 2, 3, 1])
print(x.mean()) # 1.75 ( 배열의 평균 )
print(np.median(x)) # 1.5 ( 배열의 중앙값 )

a = np.zeros((100, 100), dtype='i8')
print(a)

a[0][0] = 1
print(np.any(a != 0)) # True
print(np.all(a == 0)) # False

a = np.array([1, 2, 3, 2])
b = np.array([2, 2, 3, 2])
c = np.array([6, 4, 4, 5])

print(((a <= b) & (b <= c)).all()) # True

# 연산의 대상이 2차원인 경우
# 어느 방향으로 계산할지 axis 함수를 이용하여 계산

x = np.array([[1, 2], [3, 4]])
# [[1 2]
#  [3 4]]
#  [4 6]
print(x.sum(axis=0)) # [4 6] ( 열 합계 )
# [[1 2]  -> [3]
#  [3 4]] -> [7]
#            [3 7]
print(x.sum(axis=1)) # [3 7] ( 행 합계 )


# 문제. 3x4 행렬을 만들고 다음을 구하세요.
# 1. 전체의 최대값
# 2. 각 행의 합
# 3. 각 열의 평균

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(arr.max()) # 12
print(arr.sum(axis=1)) # [10 26 42]
print(arr.mean(axis=0)) # [5. 6. 7. 8]

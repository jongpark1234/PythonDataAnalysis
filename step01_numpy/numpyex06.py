# 배열인덱싱 : 펜시 인덱싱 ( facny indexing )
# 인덱싱 결과가 스칼라 값이 아니고 인덱스 배열인 경우

# 인덱스 배열의 방식은 불리언 배열과 정수 배영로 구분

import numpy as np

a = np.array(list(range(10)))
idx = np.array([True, False, True, False, True, False, True, False, True, False])

print(a[a[idx]])

# 조건 연산문
print(a % 2 == 0)
print(a[a % 2 == 0])

# 정수 배열 인덱싱에서는 인덱스 배열의 원소 각각이
# ndarray 객체를 가리키는 인덱스 정수여야함
a = np.array([11, 22, 33, 44, 55, 66, 77, 88, 99])
idx = np.array([0, 2, 4, 6, 8])
print(a[idx])

# 인덱스 배열의 크기는 달라도 상관이 없음
# 인덱스 배열이 원 배열의 개수보다 많아도 괜찮지만
# 인덱스 배열의 값이 원 배열에 엑세스 할 수 없는 경우 에러
a = np.array([11, 22, 33, 44, 55, 66, 77, 88, 99])
idx = np.array([0, 2, 4, 6, 8, 0, 2, 4, 6, 8])
print(a[idx])

# 배열 인덱싱은 다차원 배열에서 사용 가능
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a[:, [True, False, False, True]])

# 문제
x = np.array(list(range(1, 21)))

# 1. 3의 배수를 찾으시오.
# 2. 4로 나눈 나머지가 1인 수를 찾으시오.
# 3. 3으로 나누면 나누어 떨어지고 4로 나누면 1이 남는 수를 찾으시오.

print(x[x % 3 == 0])
print(x[x % 4 == 1])
print(x[(x % 4 == 1) & (x % 3 == 0)])

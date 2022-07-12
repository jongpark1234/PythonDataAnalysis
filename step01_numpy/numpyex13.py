# 스칼라와 벡터 / 행렬의 곱셈
# 벡터화 연산(곱셈)은 선형대수에서 사용하는 식과 numpy 코드와 일치

import numpy as np

x = np.arange(12)
print(x * 100)

x = x.reshape(3, 4)
print(x * 100)

# 브로드캐스팅
# 벡터화 연산은 배열의 크기가 같아야 하는데
# 크기가 다른 배열간의 사칙연산도 가능. -> 브로드캐스팅
# 크기가 작은 배열을 자동으로 반복 확장하여 크기가 큰 배열에 맞춤

x = np.arange(5)
y1 = np.ones_like(x)
print(x, y1) # [0 1 2 3 4] [1 1 1 1 1]
print(x + y1) # [1 2 3 4 5]
print(x + 2) # [2 3 4 5 6]
print(x + 1) # [1 2 3 4 5]

# 브로드캐스팅은 차원이 높은 경우에서도 사용 가능

x = np.vstack([range(7)[i:i + 3] for i in range(5)]) # 5x3 행렬
print(x) # [[0 1 2] [1 2 3] [2 3 4] [3 4 5] [4 5 6]]
y1 = np.arange(5)[:, np.newaxis] # 5x1 행렬
print(y1) # [[0] [1] [2] [3] [4]]
y2 = np.arange(3)
print(y2) # [0, 1, 2]

print(x + y1) # [[0 1 2] [2 3 4] [4 5 6] [6 7 8] [8 9 10]]
print(x + y2) # [[0 2 4] [1 3 5] [2 4 6] [3 5 7] [4 6 8]]

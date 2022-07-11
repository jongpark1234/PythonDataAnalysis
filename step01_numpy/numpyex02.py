# 2차원 배열
# 안쪽 리스트의 길이는 열의 수, 바깥쪽 리스트의 길이는 행의 수

import numpy as np
c = np.array([[0, 1, 2], [3, 4, 5]]) # 2x3 ndarray

print(c)
print(f'행의 개수 : {len(c)}')
print(f'열의 개수 : {len(c[0])}')

# 다음과 같은 행렬을 만드록 출력하세요.
# 10 20 30 40
# 50 60 70 80
# 결과
# 2x4행렬[0] : [10 20 30 40]
# 2x4행렬[1] : [50 60 70 80]

result = np.array([[10, 20, 30, 40], [50, 60, 70, 80]])
row = len(result)
column = len(result[0])
for i in range(row):
    print(f'{row}x{column}행렬[{i}] : {result[i]}')

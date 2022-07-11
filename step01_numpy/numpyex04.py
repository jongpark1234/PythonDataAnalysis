# 배열의 크기와 차원 알아내기
# ndim 속성은 배열의 차원, shape속성은 배열의 크기를 리턴

import numpy as np
import numpyex03 as ex03

# 1차원 배열의 속성
a = np.array([1, 2, 3])
print(a.ndim) # 1
print(a.shape) # (3, )

# 2차원 배열의 속성
b = np.array([[1, 2, 3], [4, 5, 6]])
print(b.ndim) # 2
print(b.shape) # (2, 3)

# 3차원 배열의 속성
print(ex03.d.ndim) # 3
print(ex03.d.shape) # (2, 3, 4)


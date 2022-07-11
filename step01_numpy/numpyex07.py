# ndarray 클래스는 데이터가 같은 자료형이어야 함.
# array() 로 배열을 만들 때 자료형을 명시적으로 적용하면 dtype 인수 사용
# dtype 인수가 없는 경우는 유추해서 생성
# 만들어진 배열의 자료형을 확인할때는 dtype 속성 확인

import numpy as np

x = np.array([1, 2, 3])
print(x.dtype) # int32

x = np.array([1.0, 2., 3.])
print(x.dtype) # float64

x = np.array([1, 2, 3.])
print(x.dtype) # float64

# dtype 사용 방법

x = np.array([1, 2, 3], dtype='f')
print(x.dtype) # float32
print(x[0] + x[1]) # 3.0 ( float )

x = np.array([1, 2, 3], dtype='U')
print(x.dtype) # <U1 ( Unicode )
print(x[0] + x[1]) # 12 ( str )

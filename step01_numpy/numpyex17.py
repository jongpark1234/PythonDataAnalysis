# 난수 발생, 카운팅

import numpy as np

print(np.random.random())

x = np.arange(10)
print(x)

np.random.shuffle(x)
print(x)

# choice() : 데이터 집합에서 일부를 무작위로 선택
# np.random.choice(x, size=None, replace=True, p=None)
# x : 배열, size : 뽑을 개수, replace : 복원 추출, p : 데이터가 선택될 확률

print(np.random.choice(5, 5, replace=True))
print(np.random.choice(np.arange(10), 5, replace = False))
print(np.random.choice(5, 10))
print(np.random.choice(5, 5, p=[0.1, 0, 0.3, 0.6, 0]))

# 난수 생성

# rand()
print(np.random.rand(10)) # 10개의 실수 난수 생성
print(np.random.rand(4, 3)) # 4x3 개의 실수 난수

# randn()
print(np.random.randn(10)) # 10 개의 실수 난수
print(np.random.randn(4, 3)) # 4x3 개의 실수 난수

# randint()
print(np.random.randint(10, size=10)) # 10 개의 0 ~ 9 정수 난수
print(np.random.randint(10, 20, size=10)) # 10 개의 10 ~ 19 정수 난수

# unique()
print(np.unique(np.random.choice(5, 5, replace=True)))

a = np.array(['a', 'b', 'b', 'c', 'a'])
idx, cnt = np.unique(a, return_counts=True)
print(idx, cnt)

import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([4, 2, 2, 4])

print(a == b)
print(a > b)

print(np.all(a == b))

c = np.arange(5)
print(np.exp(c)) # 지수화

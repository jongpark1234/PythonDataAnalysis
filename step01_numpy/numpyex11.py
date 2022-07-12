# 벡터화 연산

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1, 10001)
y = np.arange(10001, 20001)

z = np.zeros_like(x)
for i in range(10000):
    z[i] = x[i] + y[i]
print(z)
z = x + y
print(z)

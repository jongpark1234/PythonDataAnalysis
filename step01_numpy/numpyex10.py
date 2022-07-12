# 2차원 그리드 포인트 생성
# 변수가 2개인 2차원 함수의 그래프를 그리거나 표를 그릴 때
# 2차원 영역에 대한 (x, y) 좌표값 쌍
# 즉, 그리드 포인트를 생성하여 각 좌표에 대한 함수 값을 계산

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(3)
y = np.arange(5)

X, Y = np.meshgrid(x, y)

print(X)
print(Y)

plt.title('Grid Points')
plt.scatter(X, Y, linewidths=20)
plt.show()

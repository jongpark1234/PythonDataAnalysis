import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

ax.set(xlim=[0, 8], ylim=[0, 40])

x = np.array([1, 3, 5, 7]) # x축에 표시할 값
y = np.array([10,20, 15, 33]) # y축에 표시할 값

ax.plot(x, y, color='red')

plt.show()


# 문제. y = 2x+5 의 방정식을 꺾은선 그래프로 나타내시오.

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

ax.set(xlim=[-1, 11], ylim=[0, 30])
ax.set_title('y = 2x + 5', size = 20)
ax.set_xlabel('x', size = 10)
ax.set_ylabel('y', size = 10)

x = np.array(range(11))
y = x * 2 + 5

ax.plot(x, y, color='blue')

plt.show()

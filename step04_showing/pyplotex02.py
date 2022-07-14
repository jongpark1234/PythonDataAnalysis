import matplotlib.pyplot as plt

# 문제. 창을 가로 2, 세로 2로 나누어서 왼쪽 상단과 오른쪽 하단에 axes를 배치하세요.

fig = plt.figure()

ax1 =  fig.add_subplot(2, 2, 1)
ax2 =  fig.add_subplot(2, 2, 4)

plt.show()


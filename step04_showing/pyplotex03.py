import matplotlib.pyplot as plt

fig = plt.figure()

ax = fig.add_subplot(1, 1, 1)

ax.set_xlim([0, 1]) # x축의 값의 범위
ax.set_ylim([0, 2.5]) # y축의 값의 범위
ax.set_xlabel('x-Axis', size = 10) # x축의 라벨
ax.set_ylabel('y-Axis', size = 10) # y축의 라벨
ax.set_title('matplotlib test', size = 20) # plot 의 제목

plt.show()

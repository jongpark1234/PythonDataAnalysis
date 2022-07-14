# matplotlib 파이썬용 plot 라이브러리
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

# 가로 1칸, 세로 1칸으로 분할하고
# 분할된 창에서 1번째 칸에 ax라는 이름의 axes 생성

# axes : figure 내에서 축을 가질 수 있는 좌표평면
plt.show()

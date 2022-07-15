import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 20)

y1 = np.sin(x)
y2 = np.sin(x + 1)

plt.plot(x, y1, 'o', color = 'lime', label = 'plot test')
plt.scatter(x, y2, color = 'lime', cmap='Blues') # cmap : 컬러맵, 색상 패턴

plt.legend(loc = 'lower left') # 범례 표시, 기본위치는 우측 상단
plt.colorbar() # 우측 막대 표시
plt.title = 'plot vs scatter'
plt.xlabel('x axis')
plt.ylabel('y axis')

plt.show()

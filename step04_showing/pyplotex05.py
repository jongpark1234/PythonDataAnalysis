import matplotlib.pyplot as plt
import numpy as np

x1 = np.array([5, 8, 10])
y1 = np.array([12, 16, 6])

x2 = np.array([6, 9, 11])
y2 = np.array([5, 7, 8])

plt.bar(x1, y1, align='center')
plt.bar(x2, y2, align='center', color='lime')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rc('font', family='NanumBarunGothic')

# plt.plot([10, 20, 30, 40])
# plt.show()

# plt.title('빅데이터 분석')
# plt.plot([1, 2, 3, 4], [10, 43, 52, 22]) # x축, y축
# plt.show()

# plt.title('기상현상')
# plt.plot(['3월', '4월', '5월', '6월', '7월'], [10, 16, 19, 21, 28], 'd-', label='온도', color='skyblue')
# plt.plot(['3월', '4월', '5월', '6월', '7월'], [10, 20, 15, 50, 100], 'p-', label='강수량', color='pink')
# plt.legend()
# plt.grid()
# plt.show()

# x = [f'7.2{i}.' for i in range(1, 8)]
# y = [107, 130, 140, 146, 144, 168, 177]
# plt.title('일별 신규입원 현황과 재원 위중증 현황')
# plt.plot(x, y, 'p-', label='재원 위중증 현황', color='blue')
# plt.plot(x, [247, 321, 270, 236, 201, 275, 296], 'p-', label='신규입원 현황', color='skyblue')
# plt.legend()
# plt.grid()
# for i, j in enumerate(x):
#     plt.text(j, y[i], y[i], fontsize=10, color='black', horizontalalignment = 'center', verticalalignment='bottom')
# plt.show()

# milk = ['서울우유', '남양유업', '매일유업', '동원F&B', '빙그레']
# sales = [6152, 2077, 1936, 972, 2020]
# plt.title('2019년 3분기 누적 매출액', size=20)
# plt.bar(milk, sales, color='pink', edgecolor='green')
# plt.xlabel('회사명')
# plt.ylabel('매출액 (단위: 억)')
# plt.ylim(0, 10000)
# plt.grid(axis='y')
# for i, x in enumerate(milk):
#     plt.text(x, sales[i], sales[i], fontsize=9, color='black', horizontalalignment = 'center', verticalalignment = 'bottom')
# plt.show()

# day = [f'07.{i}' for i in range(18, 25)]
# data1 = [81, 91, 94, 107, 130, 140, 146]
# data2 = [142, 223, 277, 247, 321, 270, 236]

# fig, ax1 = plt.subplots()

# ax1.bar(day, data1, label = '일별 입원환자')
# ax1.set_xlabel('날짜')
# ax1.set_ylabel('위중증환자')
# ax1.set_ylim()
# ax1.tick_params(axis = 'both', direction = 'in')
# ax1.grid(axis = 'y')
# ax1.set_ylim(70, 160)
# ax1.legend(loc = 'upper left')

# ax2 = ax1.twinx()
# ax2.plot(day, data2, '*-', color='orange', label='일별 위중증환자')
# ax2.set_ylabel('입원환자')
# ax2.tick_params(axis = 'y', direction='in')
# ax2.set_ylim(130, 350)
# ax2.legend()

# for i, x in enumerate(day):
#     plt.text(x, data1[i], data1[i], fontsize=9, color='black', horizontalalignment='center', verticalalignment = 'bottom')
# for i, x in enumerate(day):
#     plt.text(x, data2[i], data2[i], fontsize=9, color='black', horizontalalignment='center', verticalalignment = 'bottom')
# plt.show()

# lib = pd.read_csv('전국도서관현황.csv', encoding='cp949')
# lib = lib.drop(lib.index[0])
# lib.reset_index(drop=True)
# x = [i for i in map(str, lib['시점'])]
# data = [i for i in map(int, lib['전체(공공도서관)'])]
# plt.title('연도별 공공 도서관 수 추이', size = 15)
# plt.plot(x, data, 'o-', label='개수', color='blue')
# plt.xlabel('연도')
# plt.ylabel('도서관 개수')
# plt.legend(loc = 'upper left')
# plt.grid()
# for i, x in enumerate(x):
#     plt.text(x, data[i], data[i], fontsize=9, color='black', horizontalalignment='center', verticalalignment='bottom')
# plt.show()


# students = [56, 22, 35, 12, 16]
# subject = ['물리', '화학', '생명과학', '지구과학', '빅데이터분석']
# plt.pie(students, labels=subject, autopct='%.1f%%')
# plt.show()


ratio = [34, 32, 15, 18]
labels = ['Apple', 'Banana', 'Melon', 'Grapes']
explode = [0, 0.1, 0, 0]
colors = ['silver', 'gold', 'whitesmoke', 'lightgray']

plt.pie(ratio, labels=labels, autopct='%.1f%%', explode=explode, shadow=True, colors=colors)
plt.show()

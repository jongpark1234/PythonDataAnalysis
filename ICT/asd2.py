import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
def showing(): plt.legend(); plt.show()
plt.rc('font', family='NanumBarunGothic')
df = pd.read_csv('202206_202206_연령별인구현황_월간.csv', encoding='cp949', index_col=0)
try:
    for _ in range(2):
        dong = input('지역 입력 : ')
        population = df.index.str.contains(dong)
        df_area = df[population].apply(pd.to_numeric, errors = 'coerce').transpose()
        df_area.rename(columns = df.iloc[0], inplace = True)
        exec("df_area = df_area.drop(df_area.index[0]);" * 2)
        plt.title(f'연령별 인구분포 비교')
        plt.plot([i for i in range(101)], [i for i in df_area[df_area.keys()[0]]],label = dong)
    showing()
except Exception as e:
    print(f'Error : {e}')

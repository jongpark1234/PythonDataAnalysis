# 기술 통계

import numpy as np
import scipy.stats as sta

x = np.array([5, 14,-25, -5, 8, 34, -21, 12, 35, 14, 9, 13, -24, 7, 27, -6, 18, 15])

print(len(x)) # 18

# 평균의 통계용어는 sample mean, sample average
print(x.mean()) # 7.222...
print(np.mean(x)) # 7.222...

# 분산 : 샘플분산 ( sample variance ) 은 데이터의 샘플 평균 간의
# 거리 제곱의 평균을 나타냄
# 분산이 적으면 데이터가 모여 있고, 크면 흩어져 있음.

print(x.var()) # 297.0617283950617
print(np.var(x, ddof=1)) # 314.5359477124183 ( 비편향 분산 )

print(x.std()) # 17.235478768953932 ( 표준편차 )
print(np.std(x)) # 17.235478768953932

# 중앙값 : 값을 정렬했을 때 중앙에 위치하는 값
print(np.median(x)) # 10.5

# 사분위수
print(np.percentile(x, 0)) # 최소값
print(np.percentile(x, 25)) # 제 1사분위수
print(np.percentile(x, 50)) # 제 2사분위수
print(np.percentile(x, 75)) # 제 3사분위수
print(np.percentile(x, 100)) # 최대값

print(sta.describe(x)) # nobs, minmax, mean, variance, skewness, kurtosis

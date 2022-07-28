import numpy as np
import pandas as pd
import missingno as msno

import matplotlib.pyplot as plt
import seaborn as sns
import folium

plt.rc('font', family='NanumBarunGothic')

shop = pd.read_csv('data.csv', encoding='utf-8')

view_columns = ['상호명', '지점명', '상권업종대분류명', '상권업종중분류명', '상권업종소분류명', '시도명', '시군구명', '행정동명', '법정동명', '지번주소', '도로명주소', '경도', '위도']
shop = shop[view_columns]

msno.matrix(shop)

shop.plot.scatter(x='경도', y='위도', color='blue', figsize=(12, 10), grid=True)

print(shop['시도명'].unique())
print(shop['시군구명'].unique())
print(shop['시군구명'].nunique())

plt.figure(figsize=(16, 12))
plt.title('대구시 구별 상권 분포')
sns.scatterplot(data=shop[:10000], x='경도', y='위도', style='상권업종대분류명', hue='시군구명')

print(shop['상권업종대분류명'].value_counts())
print(shop['상권업종대분류명'].values)
count = pd.value_counts(shop['상권업종대분류명'].values)
print(count)

plt.title('대구시 상권업종대분류 순위', fontsize=14)
plt.xlabel('대분류명')
plt.ylabel('개수')

count.plot.bar(grid=True, figsize=(15, 8), fontsize=13)
plt.legend()
plt.show()
count.sort_values().plot.bar(grid=True, figsize=(15, 8), fontsize=13)
plt.show()

shop_food = shop[shop['상권업종대분류명'] == '음식']
print(shop_food)

print(shop_food['상권업종중분류명'].value_counts())

count = pd.value_counts(shop_food['상권업종중분류명'].values)
plt.title('대구광역시 음식 상권 중분류 순위', fontsize=14)
plt.xlabel('음식상권중분류')
plt.ylabel('개수')
count.sort_values().plot.barh(grid = True, figsize = (15, 8), fontsize = 15)
plt.show()

print(shop_food['시군구명'].value_counts())

count_status = pd.value_counts(shop_food['시군구명'].values)
plt.title('대구광역시 음식 상권 중분류 시군구별 순위', fontsize=14)
plt.xlabel('가게 수')
plt.ylabel('구')
count_status.sort_values().plot.barh(grid = True, figsize = (15, 8), color='green', fontsize = 15)
plt.show()

shop_food_kor = shop[shop['상권업종중분류명'] == '한식']
print(shop_food_kor['시군구명'].value_counts())
count = pd.value_counts(shop_food_kor['시군구명'].values)
plt.title('대구광역시 음식 상권 중분류 시군구별 한식 순위', fontsize=14)
plt.xlabel('가게 수')
plt.ylabel('구')
count.sort_values().plot.barh(grid = True, figsize = (15, 8), color='green', fontsize = 15)
plt.show()

shop_food_kors_soon = shop[shop['상권업종소분류명'] == '순두부전문']
print(shop_food_kors_soon['시군구명'].value_counts())
count = pd.value_counts(shop_food_kors_soon['시군구명'].values)
plt.figure(figsize=(16, 12))
plt.title('대구광역시 순두부 식당 구별 분포')
sns.scatterplot(data=shop_food_kors_soon[:10000], x='경도', y='위도', hue='시군구명')
plt.show()

geo_df = shop_food_kor.copy()

MAP = folium.Map(location = [geo_df['위도'].mean(), geo_df['경도'].mean()], zoom_start=12)

for i in geo_df.index[:100]:
    title = geo_df['상호명'][i] + '-' + geo_df['도로명주소'][i]
    folium.Marker([geo_df['위도'][i], geo_df['경도'][i]], popup=title, icon=folium.Icon(color='pink')).add_to(MAP)

b4 = shop.loc[shop['상호명'].str.contains('배스킨|마라')].copy()
print(b4['상호명'].value_counts())

b4['브랜드명'] = ''
b4.loc[b4['상호명'].str.contains('배스킨'), '브랜드명'] = '배스킨'
b4.loc[b4['상호명'].str.contains('마라'), '브랜드명'] = '마라탕'
print(b4)

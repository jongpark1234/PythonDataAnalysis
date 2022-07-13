import pandas as pd

# csv 파일
# 판다스에서 read_csv()를 사용하면 DataFrame 으로 가져오게됨
# 매개변수는 '파일경로' 로 'sep=","'
# dtype 오류가 발생하는 경우 'dtype="unicode"' 로 지정해주면 됨

csv_data1 = pd.read_csv('sample5-1.csv', sep=',', dtype='unicode')
print(csv_data1)


# 테이블 내의 특정 열을 행 인덱스로 지정하려면 index_col 인수 사용
csv_data1 = pd.read_csv('sample5-1.csv', index_col='c1')
print(csv_data1)


# 열 인덱스가 없는 csv 파일에 열 인덱스 부여 ( name 인수 사용 )
csv_data2 = pd.read_csv('sample5-2.csv', names = ['c1', 'c2', 'c3'])
print(csv_data2)


# 구분자가 다른 csv 파일 처리
csv_data3 = pd.read_csv('sample5-3.csv', sep='\s+')
print(csv_data3)


# 읽을 떄 행 스킵이 필요한 경우
csv_data4 = pd.read_csv('sample5-4.csv', skiprows = [0, 1])
print(csv_data4)

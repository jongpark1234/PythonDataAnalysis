import requests
import xmltodict
import time
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns

url_base = "http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19NatInfStateJson"
url_serviceKey = "vipCwKzbYxiCn7jqRBV5jJc8A7dn2G3IpZyR2K7wZiVjAV5y11SPTqE8nL%2F22aPK%2Fu13yEA9WQM7QB0WmCXOuA%3D%3D"
url_pages = "1000" #페이지당열갯수
url_start_date = "20200101" #시작날짜
url_end_date = datetime.today().strftime('%Y%m%d') #오늘 날짜
url = url_base + "?serviceKey=" + url_serviceKey + "&pageNo=1&numOfRows=" + url_pages +"&startCreateDt="+ url_start_date + "&endCreateDt=" + url_end_date
response = requests.get(url_base)

print(response.status_code)
response = response.content

xmlObject = xmltodict.parse(response)
dict_data = xmlObject['response']['body']['items']['item']
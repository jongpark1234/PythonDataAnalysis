from bs4 import BeautifulSoup
from urllib import request

soup = BeautifulSoup(request.urlopen('https://movie.naver.com/movie/running/current.naver'), 'html.parser')

# 전체 영화 제목 출력
for i in soup.find_all('div', {'class': 'thumb'}):
    for j in i.find_all('img'):
        print(j.get('alt'))

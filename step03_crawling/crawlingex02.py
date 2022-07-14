from bs4 import BeautifulSoup

# 태그와 속성을 이용해서 가져오기

with open('sample1.html', encoding='utf-8') as fp:
    soup = BeautifulSoup(fp, 'html.parser')
    print(soup)

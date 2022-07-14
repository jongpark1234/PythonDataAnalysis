import requests as req
from bs4 import BeautifulSoup

def get_html(url):
    res = req.get(url)
    if res.status_code == 200:
        return res.text
    else:
        return None
url = 'https://comic.naver.com/webtoon/list?titleId=757904'
html = get_html(url)
soup = BeautifulSoup(html, 'html.parser')
print(soup)
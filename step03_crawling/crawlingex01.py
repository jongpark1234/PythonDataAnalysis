import requests as req

def get_html(url):
    res = req.get(url)
    if res.status_code == 200:
        return res.text
    else:
        return None
url = 'https://comic.naver.com/webtoon/list?titleId=757904'
html = get_html(url)
print(html)

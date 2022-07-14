from bs4 import BeautifulSoup

# find() 및 find_all()

# 찾고자 하는 태그를 검색, 속성지정 가능
# 중복일 경우에는 첫 번째만 가져옴
with open('sample1.html', encoding='utf-8') as fp:
    soup = BeautifulSoup(fp, 'html.parser')

    first_div = soup.find('div')
    all_divs = soup.find_all('div')
    print(first_div)
    print(all_divs)

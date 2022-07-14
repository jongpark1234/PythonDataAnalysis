from bs4 import BeautifulSoup

# 태그와 속성을 이용해 가져오기

with open('sample1.html', encoding='utf-8') as fp:
    soup = BeautifulSoup(fp, 'html.parser')
    # id 가 'sample_id' 인 div 태그를 가지고 와서
    sample_id_div = soup.find('div', {'id': 'sample_id'})
    # 그 안의 p태그를 가져오기
    all_ps_in_sample_id_div = sample_id_div.find_all('p')
    print(all_ps_in_sample_id_div)

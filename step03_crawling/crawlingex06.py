import requests as req
source = '''
<li>123</li>
<li>가나다</li>
<li>마바사</li>
<li>abc</li>
<li>kbs</li>
<style>style</style>
'''
text = ''
while True:
    source = source[source.find('<'):] # < 을 찾는다
    if source.find('<!--') == 0:
        source = source[source.find('-->') + 3:] # 주석내용 건너뛰기
    elif source.find('<style>') == 0:
        source = source[source.find('</style>') + 8:] # 스타일 내용 건너뛰기
    elif source.find('<script>') == 0:
        source = source[source.find('</script>') + 9:] # 스크립트 내용 건너뛰기
    else:
        source = source[source.find('>') + 1:] # > 을 찾는다
        for ch in source: # > 이후부터 한 글자씩 가져오기
            if ch == '<': 
                break # 다시 < 등장하면 종료
            elif ch in '\t\n':
                continue
            else:
                text += ch
        if text.endswith(' ') == False:
            text += ' ' # 공백을 기준으로 분리
    
    print(text)
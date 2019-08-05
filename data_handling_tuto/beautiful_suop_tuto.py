from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import requests

#file에서 html 소스 가져오기
with open('data/03. test_first.html') as fp:
    soup = BeautifulSoup(fp, 'html.parser')
    print(soup.prettify())


#url에서 소스 가저오기
web_url = 'https://www.naver.com'

with urllib.request.urlopen(web_url) as response:
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    print(soup.prettify())

#requests를 통해서 웹에 있는 소스 가져오기
r = requests.get(web_url)
print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)
print(r.text)

#HTML 예제
with open('data/03. test_first.html') as fp:
    soup = BeautifulSoup(fp, 'html.parser')
    #find_all() : 해당 조건에 맞는 모든 태그들을 가져온다.
    all_divs = soup.find_all('div')
    print(all_divs)

    #find() : 해당 조건에 맞는 하나의 태그를 가져온다. 중복이면 가장 첫 번째 태그를 가져온다.
    first_div = soup.find('div')
    print(first_div.prettify())

    #태그와 속성을 이용해서 가져오기
    find_first = soup.find_all('p',{'id':'first'})
    print(find_first)
    print(type(find_first))

    #HTML 구조를 이용해 부분부분 가져오기
    all_divs = soup.find('div')
    all_p = all_divs.find_all('p')
    print(all_p,'\n\n')

#soup의 한 단계 아래에 포함된 태그 찾기
with open('data/03. test_first.html') as fp:
    soup = BeautifulSoup(fp, 'html.parser')
    child_soup = soup.children
    list_child_soup = list(child_soup)
    print(soup)
    print(list_child_soup,'\n\n')
    print(list_child_soup[2],'\n\n')
    print(type(list_child_soup[2]))

    #body 찾기
    print(list(soup.body))
    #class가 할당된 태그 찾기
    print(soup.find('p', class_='outer-text first-item'))

    #다음 태그 찾기(next_sibling 시 \n이 나오고 한번 더 실행 시 다음 태그를 찾을 수 있음)
    print(soup.find('p', class_='outer-text first-item').next_sibling.next_sibling)

    #get_text로 텍스트 가저오기
    print('find ,find_all 타입')
    print(type(soup.find('p')), type(soup.find_all('p')))

    for each_tag in soup.find_all('p'):
        print(each_tag.get_text())

    #태그안의 정보 가지고오기
    links = soup.find_all('a')
    for each in links:
        print('each : ',each)
        print(type(each))
        href = each['href']
        text = each.string

        print(text + ' -> ' +href)



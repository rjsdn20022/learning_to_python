from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from urllib.request import urlopen
from urllib.parse import quote
from tqdm import tqdm_notebook
import matplotlib.pyplot as plt

'''
데이터를 가져오기 전 예시 데이터 처리
url_base = 'https://movie.naver.com/'
url_syb = 'movie/sdb/rank/rmovie.nhn?sel=cur&date=20190723'
url = url_base+url_syb

html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')

#print(soup)

div_tit5 = soup.find_all('div', class_='tit5')
td_point = soup.find_all('td', class_='point')
for div, td in zip(div_tit5, td_point):
    print(div.get_text(), td.get_text())  #text문 전체 가져오기
    print(div.a.string, td.string) #target의 string을 찾아 가져오기
'''
data_index = pd.date_range('2019-06-01', '2019-07-22')
url_base = 'https://movie.naver.com/'
url_syb = 'movie/sdb/rank/rmovie.nhn?sel=cur&date={data_index}'
date = []; name = []; point = [];

for today in tqdm_notebook(data_index):
    html = url_base + url_syb
    response = urlopen(html.format(data_index=quote(today.strftime('%Y%m%d'))))
    soup = BeautifulSoup(response, 'html.parser')
    end = len(soup.find_all('td', 'point'))

    date.extend([today for n in range(end)])
    name.extend([soup.find_all('div', class_='tit5')[n].a.string for n in range(end)])
    point.extend([soup.find_all('td', class_='point')[n].string for n in range(end)])

movie = pd.DataFrame({'date': date, 'name': name, 'point': point})
movie.to_csv('data/movie_sco.csv', sep=',', encoding='UTF-8')
print(movie.head())
aladin_point = movie.query('name == ["알라딘"]')

#movie_unique = pd.pivot_table(movie, index=['name'], aggfunc=np.sum)
#movie_best = movie_unique.sort_values(by='point', ascending=False)

plt.figure(figsize=(12, 8))
plt.plot(aladin_point['date'], aladin_point['point'])
plt.legend(loc='best')
plt.grid()
plt.show()

movie_pivot = pd.pivot_table(movie, index=['date'], columns=['name'], values=['point'])
print(movie_pivot.head(20))
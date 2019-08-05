from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd

url_base = 'https://www.chicagomag.com'
url_sub = '/Chicago-Magazine/November-2017/Chicagos-Best-Steakhouses-2017/'
url = url_base + url_sub

html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')

#print(soup.prettify(),'\n\n')

restaurant_link = soup.find_all('a', class_='steak-item black-reverse')
restaurant_link.append(soup.find('a', class_='steak-item black-reverse balance-text'))


#print(steak_tag, len(steak_tag))
steak_link_num = len(restaurant_link)

rank = [0 for x in range(steak_link_num)]
name = [0 for x in range(steak_link_num)]
restaurant_url = [0 for x in range(steak_link_num)]
place = [0 for x in range(steak_link_num)]
tel = [0 for x in range(steak_link_num)]

for i in range(steak_link_num):
    rank[i] = int(restaurant_link[i].get_text().split('.')[0])
    name[i] = restaurant_link[i].get_text().split('.')[1][1:]

    html = urlopen(url_base+restaurant_link[i]['href'])
    soup = BeautifulSoup(html, 'html.parser')
    section = soup.find('section', 'related-content pull-right')
    if not section:
        section = soup.find('aside', 'related-content pull-right')

    place[i] = section.find('li').get_text()
    tel[i] = section.find('li').next_sibling.next_sibling.get_text()
    restaurant_url = section.find('li').next_sibling.next_sibling.next_sibling.next_sibling.find('a')['href']


data = {'Rank': rank, 'name': name, 'restaurant_url': restaurant_url, 'place': place, 'tel': tel}
df = pd.DataFrame(data)

df.set_index('Rank', inplace=True)
df = df.sort_values(by='Rank', ascending=True)

print(df.head(10))
df.to_csv('data/best_steak_cafe_in_chicago.csv', sep=',', encoding='UTF-8')

import pandas as pd
import numpy as np
import platform
from matplotlib import font_manager, rc, pyplot as plt
import sys
import json
import folium

plt.rcParams['axes.unicode_minus'] = False

if platform.system() == 'Darwin':
	rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
	path = 'C:/Windows/Fonts/malgun.ttf'
	font_name = font_manager.FontProperties(fname=path).get_name()
	rc('font', family=font_name)
else:
	print('not system met')
	sys.exit(0)



CCTV_Seoul=pd.read_csv('data/CCTV_in_Seoul.csv', encoding='utf-8')
pop_Seoul=pd.read_excel('data/population_in_Seoul.xls',
			                usecols = 'A, C, D, E, F, G, H',
			                encoding = 'utf-8')

#print(CCTV_Seoul.head())


CCTV_Seoul.rename(columns={CCTV_Seoul.columns[0] : '구별'}, inplace=True)
CCTV_Seoul['최근증가율'] = (CCTV_Seoul['2016년'] + CCTV_Seoul['2015년'] +
                       CCTV_Seoul['2014년']) / CCTV_Seoul['2013년도 이전'] * 100
CCTV_Seoul=CCTV_Seoul.sort_values(by='최근증가율', ascending = False)
print(CCTV_Seoul.head())

#print(pop_Seoul.head())
pop_Seoul.rename(columns={pop_Seoul.columns[1] : '구별'}, inplace=True)
pop_Seoul=pop_Seoul[pop_Seoul['기준일ID'].isin(['20190525'])]
#####isin으로 bool list를 가저와서 pop_Seoul의 대입 후 index를 뽑아 drop
pop_Seoul.drop(pop_Seoul[pop_Seoul['구별'].isin(['서울시'])].index, inplace=True)
pop_Seoul['외국인인구수']=pop_Seoul['장기체류외국인인구수'] + pop_Seoul['단기체류외국인인구수']
pop_Seoul=pop_Seoul[['구별', '총생활인구수', '내국인생활인구수', '외국인인구수']]
pop_Seoul['외국인비율']=pop_Seoul['외국인인구수']/pop_Seoul['총생활인구수']*100
pop_Seoul=pop_Seoul.sort_values(by='외국인비율', ascending=False)
print(pop_Seoul.head())


data_result = pd.merge(CCTV_Seoul, pop_Seoul, on='구별')

del data_result['2013년도 이전']
del data_result['2014년']
del data_result['2015년']
del data_result['2016년']

data_result.set_index('구별', inplace=True)
data_result['CCTV비율'] = data_result['소계']/data_result['총생활인구수']*100
data_result=data_result.sort_values(by='소계', ascending=False)
print(data_result)

data_corrcoef=np.corrcoef(data_result['외국인비율'], data_result['소계']) #약한 음의 상관관계
print(data_corrcoef)

data_result['소계'].sort_values().plot(kind='barh', grid=True, figsize=(10,10))
plt.xlabel('소계')
plt.ylabel('구별')
plt.title('서울 구별 CCTV 현황')
plt.show()
data_result['CCTV비율'].sort_values().plot(kind='barh', grid=True, figsize=(10,10))
#kind=barh(수평바) grid 추가
plt.xlabel('CCTV비율')
plt.ylabel('구별')
plt.title('서울 구별 CCTV 현황')
plt.show()
'''
CCTV 비율은 용산구가 높지만 전체 CCTV는 강남구가 높다
대채적으로 낮은 CCTV 보유 구는 인구대비 CCTV 현황도 낮은 현상을 보임
'''

plt.figure(figsize=(6,6))
plt.scatter(data_result['총생활인구수'], data_result['소계'], s= 50) #s=marker의 size
plt.show()

fp = np.polyfit(data_result['총생활인구수'], data_result['소계'], 1)
print(fp)

fy = np.poly1d(fp)
fx = np.linspace(100000, 700000, 100)
#상관관계에 대한 라인

plt.plot(fx, fy(fx), ls='dashed', lw=3, color='g')
plt.xlabel('인구수')
plt.ylabel('CCTV')
plt.title('인구수 대비 CCTV')
plt.grid()
plt.show()

data_result['오차'] = np.abs(data_result['소계'] - fy(data_result['총생활인구수']))
#데이터의 상관관계에 대한 오차값
data_result = data_result.sort_values(by='오차', ascending=False)
#인구수와 CCTV 현황의 상관관계에 대한 오차데이터 추가

plt.figure(figsize=(14,10))
plt.scatter(data_result['총생활인구수'], data_result['소계'], c=data_result['오차'], s=50)
plt.plot(fx, fy(fx), ls='dashed', lw=3, color='g')

for n in range(25):
	plt.text(data_result['총생활인구수'][n]*1.02, data_result['소계'][n]*0.98,
			 data_result.index[n], fontsize=15)

plt.xlabel('인구수')
plt.ylabel('CCTV')
plt.title('인구수 대비 CCTV')
plt.colorbar()
plt.grid()
plt.show()

data_result.to_csv('data/data_result.csv', sep=',', encoding='utf-8')

geo_path = 'data/02. skorea_municipalities_geo_simple.json'
geo_str = json.load(open(geo_path, encoding='utf-8'))

map_opt = folium.Map(location=[37.5502, 126.982], zoom_start=11, tiles='Stamen Toner')
#Map 지정
folium.Choropleth(geo_data=geo_str, data=data_result['소계'], columns=[data_result.index, data_result['소계']],
				  fill_color='PuRd', key_on='feature.id').add_to(map_opt)
#data를 이용하여 색 나타내기
map_opt.save('data/CCTV_Map.html')
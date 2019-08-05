import folium
import pandas as pd
import json
map_osm = folium.Map(location=[45.5236, -122.6750], tiles='Stamen Toner', zoom_start=13)
folium.Marker([45.5244, -122.6699], popup='The Waterfont').add_to(map_osm)
folium.CircleMarker([45.5215, -122.6261], radius=50, popup='Laurelhurst Park', color='#3186cc',
                    fill_color='#31866cc').add_to(map_osm)

'''
zoom_start : 확대 비율
tiles : 지도 모양시트
folium.Marker : 마커 추가
- popup : 누르면 나오는 간단한 설명

folium.CircleMarker : 원형 마커 추가
- radius : 크기
- fill_color : 내부 색상
'''
map_osm.save('data/folium_ex1.html')

state_data = pd.read_csv('data/02. folium_US_Unemployment_Oct2012.csv')
state_geo = 'data/02. folium_us-states.json'

map_osm = folium.Map(location=[40, -98], zoom_start=4)
folium.Choropleth(geo_data=state_geo, data=state_data, columns=['State', 'Unemployment'],
                   key_on='feature.id', fill_color='YlGn', legend_name='Unemployment Rare (%)').add_to(map_osm)
map_osm.save('data/folium_ex2.html')
print(state_data.head())

geo_path = 'data/02. skorea_municipalities_geo_simple.json'
geo_str = json.load(open(geo_path, encoding='utf-8'))

map_osm = folium.Map(location=[37.5502, 126.982], zoom_start=11)
folium.Choropleth(geo_data=geo_str, fill_color='PuRd', key_on='feature.id').add_to(map_osm)
map_osm.save('data/folium_ex3.html')

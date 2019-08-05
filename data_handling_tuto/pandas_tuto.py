# -*- coding: utf-8 -*-


import pandas as pd
import numpy as np

print('pandas Series 생성')
s = pd.Series([1,3,5,np.nan,6,8])
print(s)

print('data index만들기(배열, 데이터타입)')
dates = pd.date_range('20130101', periods =6)
print(dates)

print('index이용하여 data frame 만들기')
df = pd.DataFrame(np.random.randn(6,4), index = dates, columns = ['A','B','C','D'])
print(df)
print()

print('data frame 정보 확인')
print(df.head(3)) 
print(df.index)
print(df.columns)
print(df.values)
print(df.info())
print()


print('데이타 프레임 표준편차')
print(df.describe())
print()

print('values_sort')
print(df.sort_values(by='B', ascending=False))
print()

print('data 인덱스(슬라이싱)')
print(df['A'])
print(df[0:3])
print(df['20130102':'20130104'])

print('data location 특정한 범위를 정할 때')
print(df.loc[dates[0]])
print(df.loc[:, ['A','B']])

print('행과 열의 번호를 이용하여 데이터에 접근')
print(df.iloc[3])

print('3~4까지의 행과 0~1까지의 열')
print(df.iloc[3:5,0:2])

print('1~2까지 행, 전체 열')
print(df.iloc[1:3,:])

print('df.A의 0보타 큰 행을 얻어온다.')
print(df[df.A > 0])

print('df 데이터 내용 복사')
df2 = df.copy()

print('df 새로운 컬럼 추가')
df2['E'] = ['one','one','two','there','four','there']
print(df2)

print('데이터의 조건문 .isin')
print(df2[df2['E'].isin(['two','four'])])

print('데이터의 누적 합')
print(df.apply(np.cumsum))

print('lambda 함수를 이용하여 최대값과 최소값의 차 구하기')
print(df.apply(lambda x: x.max() - x.min()))
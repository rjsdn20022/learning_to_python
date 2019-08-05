import pandas as pd
import numpy as np

df = pd.read_excel("data/salesfunnel.xlsx")
print(df.head())

#df = pd.pivot_table(df, index=['Name']) df의 인덱스를 Name으로 지정하고 숫자형 데이터들의 평균값이 남는다
#df = pd.pivot_table(df, index=['Name', 'Rep', 'Manager']) 인덱스를 여러개 지정
#df = pd.pivot_table(df, index=['Manager', 'Rep'], values=['Price']) 특정 values 지정
#df = pd.pivot_table(df, index=['Manager', 'Rep'], values=['Price'], aggfunc= np.sum) 평균대신 전체 합 np.mean = 평균
df = pd.pivot_table(df, index=['Manager', 'Rep', 'Product'], values=['Price', 'Quantity'], aggfunc=[np.sum, np.mean],
                    fill_value=0, margins=True)
print(df.head())
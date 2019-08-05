import pandas as pd

CCTV_Seoul = pd.read_csv('data/CCTV_in_Seoul.csv', encoding='utf-8')

print(CCTV_Seoul.head())
C_c = CCTV_Seoul.columns
print(C_c)
print(C_c[0])

CCTV_Seoul.rename(columns = {CCTV_Seoul.columns[0] : '구별'}, inplace= True)
print(CCTV_Seoul.head())

pop_Seoul = pd.read_excel('data/population_in_Seoul.xls',
			header =2,
			usecols = 'B, D, G, J, N',
			encoding = 'utf-8')

pop_Seoul.rename(columns = {pop_Seoul.columns[0]: '구별',
			pop_Seoul.columns[1]: '인구수',
			pop_Seoul.columns[2]: '한국인',
			pop_Seoul.columns[3]: '외국인',
			pop_Seoul.columns[4]: '고령자',}, inplace = True)
print(pop_Seoul.head())
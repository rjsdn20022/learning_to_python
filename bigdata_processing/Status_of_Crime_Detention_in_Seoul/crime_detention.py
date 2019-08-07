import pandas as pd
import numpy as np
import platform
from matplotlib import font_manager, rc, pyplot as plt
import sys
import seaborn as sns

plt.rcParams['axes.unicode_minus'] = False

if platform.system() == 'Darwin' :
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    path = 'C:/Windows/Fonts/malgun.ttf'
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
else:
    print('find not system')
    sys.exit(0)

crime_detention = pd.read_csv('data/2017년.csv', thousands=',', encoding='euc-kr')
print(crime_detention.head(20))

sns.pairplot(crime_detention, vars=['건수'], kind='reg')
plt.show()

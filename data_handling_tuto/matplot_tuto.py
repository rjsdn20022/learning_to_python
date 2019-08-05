import matplotlib.pyplot as plt
import numpy as np

#기본 데이터 그리기
fig_size = (10, 6)
plt.figure()
plt.plot([x for x in range(1, 10)])
plt.plot([x for x in range(10, 0, -1)])
plt.show()

#삼각함수 그래프
t = np.arange(0, 12, 0.01)
t_sin = np.sin(t)
t_cos = np.cos(t)

plt.figure(figsize=fig_size)
plt.plot(t, t_sin, lw=3, label='sin')
plt.plot(t, t_cos, 'r',label='cos')
plt.grid()
plt.legend()
plt.xlabel('time')
plt.ylabel('Amplitude')
plt.title('Example of sin')
plt.show()

t = [x for x in range(0, 7)]
y = [1, 4, 5, 8, 9, 5, 3]

plt.figure(figsize=fig_size)
plt.plot(t, y, color = 'green', linestyle='dashed', marker='o', markerfacecolor='blue', markersize=12)
plt.show()

colormap = t
plt.scatter(t, y, c=colormap, s=50)
plt.colorbar()
plt.show()

s1 = np.random.normal(loc=0, scale=1, size=1000)
s2 = np.random.normal(loc=5, scale=0.5, size=1000)
s3 = np.random.normal(loc=10, scale=2, size=1000)

plt.plot(s1, label='s1')
plt.plot(s2, label='s2')
plt.plot(s3, label='s3')
plt.legend()
plt.show()
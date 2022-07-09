import matplotlib.pyplot as plt
import numpy as np
plt.rc('font', family='simhei', size=12)
plt.rc('axes', unicode_minus=False)
d1 = np.random.randn(1000)
plt.hist(d1, bins=100, facecolor="blue", edgecolor="black", alpha=0.5)
plt.show()


label = ('big', 'mid', 'small', 'other')
color = ('r', 'orange', 'y', 'g')
size = [48, 21, 18, 13]
explode = (0.1, 0, 0, 0)
pie = plt.pie(size, colors=color, explode=explode,
              labels=label, shadow=True, autopct='%1.1f%%')
plt.title('size statistic')
plt.axis('equal')   # 设置x， y刻度相同
plt.legend()
plt.show()

N = 1000
x = np.random.randn(N)
y = np.random.randn(N)
color1 = ['r', 'y', 'k', 'g', 'm']*int(N/5)    # 平均分布颜色
plt.scatter(x, y, c=color1, marker='v', alpha=0.7)
plt.title('scatter chart')
plt.show()

t = np.arange(0, 2*np.pi, 0.02)
ax1 = plt.subplot(111, projection='polar')   # 创建极坐标
ax1.plot(t, t/6, '--', lw=2)
plt.show()

import numpy as np
import matplotlib.pyplot as plt
font = {'family' : 'SimHei',      # 字典方式设置
        'weight' : 'bold',
        'size' : '20'}
plt.rc('font', **font)    # 统一设置subplot中的字体
plt.rc('axes', unicode_minus=False)   # 解决显示©负号问题
plt.xlabel("中文黑体")
x = np.linspace(-np.pi, np.pi, 100)
x2 = np.linspace(-np.pi, np.pi, 10)
yc, ys = np.cos(x), np.sin(x)
plt.plot(x, yc)
plt.plot(x, ys)
plt.show()


yc, ys = np.cos(x2), np.sin(x2)   # 数目离散
plt.plot(x2, yc)
plt.text(1.5, 0.5, r'Blue sin()', fontsize=10, fontweight='heavy')
plt.arrow(2, 0.8, -0.12, 0.2, width=0.05, fc='r')   # y 0.5 -> -0.12    x 0-> 0.2
plt.plot(x2, ys, 'ro--')  # r red o 点  v 下三角 -- 虚线
plt.annotate('Top amx', xy=(3, 1), xytext=(3.2, 0.5),
             arrowprops=dict(facecolor='m', shrink=0.01), fontsize=10)
plt.title('fig1')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

plt.plot(x2, yc)
plt.plot(x2, ys)
ax = plt.gca()    # 获取当前axes类实例
ax.spines['right'].set_color('none')  # 消除四周axis
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')  # 加入x 轴
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')    # 加入y轴
ax.spines['left'].set_position(('data', 0))
plt.show()

x, y = np.indices((100, 100))
sig = np.sin(2*np.pi*x/50.) * np.sin(2*np.pi*y/50.) *(1+x*y/50.**2)**2
plt.axis('off')
plt.title('sig')
plt.imshow(sig)    # 矩阵可视化绘图 二维无边框绘图
plt.show()

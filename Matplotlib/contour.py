import numpy as np
import matplotlib.pyplot as plt
axes = plt.figure(figsize=(10, 4))
axes.add_subplot(131)


def f(x, y):
    return x**2+y**2-1


n = 256
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)
X, Y = np.meshgrid(x, y)    #
plt.contourf(X, Y, f(X, Y), 8, alpha=0.7, cmap='jet')    # cmap 填充颜色 等高图

axes.add_subplot(132)
C = plt.contour(X, Y, f(X, Y), 8, colors='k', linewidth=0.4)   # 绘制等高线不进行填充

axes.add_subplot(133)
C = plt.contour(X, Y, f(X, Y), 8, colors='k', linewidth=0.2)
plt.clabel(C, inline=True, fontsize=12)    # 设置等高线数值
plt.show()

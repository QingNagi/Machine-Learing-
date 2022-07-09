import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.colors import LightSource
fig = plt.figure(figsize=(15, 5))
ax = fig.add_subplot(1, 3, 1, projection='3d')
x = np.arange(1, 50, 1)
y = np.arange(1, 50, 1)
x, y = np.meshgrid(x, y)


def Z(x, y):
    return x*0.2 + y*0.3 +20


s1 = ax.plot_surface(x, y, Z(x, y), rstride=10, cstride=10, cmap=cm.jet, linewidth=1,
                     antialiased=True)
fig.colorbar(s1, shrink=1, aspect=4)

ax1 = fig.add_subplot(1, 3, 2, projection='3d')
s2 = ax1.plot_surface(x, y, Z(x, y), rstride=1, cstride=1, cmap=cm.jet, linewidth=1,
                      antialiased=False)   # rstide 指定行列色彩跨度， cmap 设置面的颜色条
fig.colorbar(s2, shrink=0.4, aspect=4)   # 色度条

d = 0.05
x1 = np.arange(-4, 4, d)
y1 = np.arange(-4, 4, d)
x1, y1 = np.meshgrid(x1, y1)


def z1(x, y):
    z3 = np.exp(-x**2-y**2)
    z2 = np.exp(-(x - 1)**2 - (y - 1)**2)
    return (z2 - z3)*2


ax2 = fig.add_subplot(1, 3, 3, projection='3d')
s3 = ax2.plot_surface(x1, y1, z1(x1, y1), rstride=1, cstride=1, cmap=cm.jet, linewidth=1,
                      antialiased=False)
fig.colorbar(s3, shrink=0.4, aspect=4)
plt.show()




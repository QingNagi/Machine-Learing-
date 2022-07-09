import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.colors import LightSource
fig2 = plt.figure(2, figsize=(10, 3))
ax3 = plt.subplot(1, 3, 1, projection='3d')
x1 = np.arange(-4, 4, 0.25)
y1 = np.arange(-4, 4, 0.25)

x2, y2 = np.meshgrid(x1, y1)   # 从坐标向量中返回坐标矩阵（x, y）
R = np.sqrt(x2**2 + y2**2)
z = np.sin(2+R)
ax3.plot_surface(x2, y2, z, rstride=1, cstride=1, facecolor='green')

ax4 = plt.subplot(1, 3, 2, projection='3d')

ls = LightSource(90.45)
rgb = ls.shade(z, cmap=cm.Wistia, vert_exag=0.1, blend_mode='soft')
ax4.plot_surface(x2, y2, z, rstride=1, cstride=1, facecolors=rgb)

ax5 = plt.subplot(133, projection='3d')
ax5.plot_surface(x2, y2, z, rstride=1, cstride=1, lightsource=(180, 35, 0, 0.2, 0.1, 0), facecolor='g', shade=False)


plt.show()
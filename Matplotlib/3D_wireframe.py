import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

font = {
    'family': 'SimHei',
    'weight': 'bold',
    'size': '14'
}
plt.rc('font', **font)
plt.rc('axes', unicode_minus=False)
fig = plt.figure(figsize=(11, 4))
x = np.linspace(-30, 30, 60)
y = np.linspace(-30, 30, 60)
ax = fig.add_subplot(131, projection='3d')
z = np.linspace(0, -1*np.pi, 60)
z = np.sin(z)*40
x, y = np.meshgrid(x, y)
z0 = z[:, np.newaxis]   # 形成列向量 建立二维矩阵，要求和x,y矩阵保持一样的维数，单列矩阵可广播
print(z0)

ax.plot_wireframe(x, y, z0, rstride=5, cstride=5, label='下陷', color='b')
ax.legend(loc='best')

ax1 = fig.add_subplot(132, projection='3d')
z1 = np.linspace(0, np.pi, 60)
z1 = np.sin(z1)*40
z01 = z1[:, np.newaxis]
ax1.plot_wireframe(x, y, z01, rstride=7, cstride=7, label='上凸', color='g')
ax.legend(loc='best')  # 给图加上图例,loc 图例所有figure位置

ax2 = fig.add_subplot(133, projection='3d')
z2 = np.linspace(0, 2*np.pi, 60)
z2 = np.sin(z2)*40
z02 = z2[:, np.newaxis]
ax2.plot_wireframe(x, y, z02, rstride=7, cstride=7, label='下陷上凸', color='r')
ax2.legend(loc='best')
plt.show()


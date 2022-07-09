import numpy as np
from matplotlib import pyplot as plt
import mpl_toolkits.mplot3d as p3d
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure(1)
ax1 = plt.axes(projection='3d')
plt.subplot(111, projection='3d')

fig = plt.figure(2)
ax2 = p3d .Axes3D(fig)  #建立三维坐标
ax2.set_xlim(0, 6)
ax2.set_ylim(7, 0)
ax2.set_zlim(0, 8)

dot1 = [[0, 0, 0], [1, 1, 1], [2, 2, 2], [2, 2, 4]]
plt.figure(3)
ax3 = plt.axes(projection='3d')
ax2.set_xlim(0, 6)
ax2.set_ylim(7, 0)
ax2.set_zlim(0, 8)
color1 = ['r', 'g', 'b', 'k', 'm']
marker1 = ['o', 'v', '1', 's', 'h']
i = 0
for x in dot1:
    ax3.scatter(x[0], x[1], x[2], c=color1[i], marker=marker1[i], linewidths=4)
    i += 1

plt.figure(4)
ax4 = plt.axes(projection='3d')
ax4.set_xlim(0, 20)
ax4.set_ylim(20, 0)
ax4.set_zlim(0, 20)
z = np.linspace(0, 4*np.pi, 500)
x = 10*np.sin(z)
y = 10*np.cos(z)
ax4.plot3D(x, y, z, 'black')

z1 = np.linspace(0, 4*np.pi, 500)
x = 5*np.sin(z)
y = 5*np.cos(z)
ax4.plot3D(x, y, z, 'g--')

ax4.plot3D([0, 18, 0], [5, 18, 10], [0, 5, 0], 'om-')


plt.show()


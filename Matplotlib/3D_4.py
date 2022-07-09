from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure(1, figsize=(10, 8))
ax = plt.subplot(111, projection='3d', elev=30, azim=30)   # 进行旋转  elev z轴仰角值 azim x，y轴的方位角
u = np.linspace(0, 2*np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = 10*np.outer(np.cos(u), np.sin(v))    # 求外积
y = 10*np.outer(np.sin(u), np.sin(v))
z = 10*np.outer(np.ones(np.size(u)), np.cos(v))
ax.plot_surface(x, y, z, color='m', cmap=plt.cm.winter, lightsource=(180, 35, 0, 0.2, 0.1, 0), alpha=0.4)
ax.text(0, 0, 0, 'ball', color='r', fontsize=17, alpha=0.4)
z1 = np.linspace(0, 4*np.pi, 500)
x1 = 10*np.sin(z1)
y1 = 10*np.cos(z1)
ax.plot3D(x1, y1, z1, 'black', label='show me')

ax.legend()
plt.title('ball', fontsize=20)
plt.show()


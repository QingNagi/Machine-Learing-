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
fig = plt.figure(figsize=(16, 5))
ax = fig.add_subplot(121, projection='3d')
x1 = np.arange(20)
y1 = np.random.randn(20)
print(y1)
ax.bar(x1, y1, zs=1, zdir='y', color='y', alpha=0.7)
ax.set_xlabel('x轴')

ax1 = fig.add_subplot(122, projection='3d')
x2, y2 = np.meshgrid(x1, y1)
x2, y2 = x2.ravel(), y2.ravel()
z2 = np.abs(x2 + y2)
ax1.bar3d(x2, y2, 0, dx=1, dy=1, dz=z2, shade=True, color='g')  # dx 深度



plt.show()


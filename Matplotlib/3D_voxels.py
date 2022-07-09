import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(10, 4))
ax = plt.subplot(121, projection='3d')
x = np.linspace(0, 4, 5)
y = np.linspace(0, 4, 5)
z = np.linspace(0, 4, 5)
f_one = np.zeros((4, 4, 4), dtype=bool)
f_one[0, 0, 0] = True
x, y, z = np.meshgrid(x, y, z)
ax.voxels(x, y, z, f_one, facecolors='r', edgecolors='k')
y[:, :, :] += 0.2
f2_one = np.zeros((4, 4, 4), dtype=bool)
f2_one[0, 2, 0] = True
x[:, :, :] += 0.2
ax.voxels(x, y, z, f2_one, facecolors='g', edgecolors='k')
f3_one = np.zeros((4, 4, 4), dtype=bool)
f3_one[0, 1, 2] = True
f3_one[0, 2, 3] = True
ax.voxels(x, y, z, f3_one, facecolors='k', edgecolors='k')

ax1 = plt.subplot(122, projection='3d')
x, y, z = np.indices((5, 5, 5), dtype=float)
n = len(x)
f4_one = np.ones((n-1, n-1, n-1), dtype=bool)     # 返回坐标组数
ax1.voxels(x, y, z, f4_one, edgecolors='k', facecolors='m')
plt.show()


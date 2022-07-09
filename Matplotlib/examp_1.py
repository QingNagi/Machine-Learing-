import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Circle
import numpy as np
img = plt.imread('test.jpg')
img1 = img.copy()
fig = plt.figure()
x = np.linspace(50, np.pi*30, 1000)
y = np.sin(5 + x)*15 + 40
ax = fig.add_subplot(111, aspect='equal')
# ax.plot(x, y, lw=2, color='y')
C1 = Circle(xy=(500, 190), radius=24, alpha=0.9, edgecolor='r', facecolor='r')

ax.add_patch(C1)
plt.imshow(img1)
ax.axis('off')
ax.set_xlim(0, 960)
ax.set_ylim(537, 0)
plt.show()

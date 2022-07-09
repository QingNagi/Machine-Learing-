from IPython import display   # 为正常显示动画效果
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
fig = plt.figure()
ax = fig.add_subplot(111)
x = np.linspace(0, 2*np.pi, 300)
y = np.sin(3*x) + 5
plt.plot(x, y, color='r')
x1 = x[::2]
y1 = y[::2]
print(x1)
i = 0
for pos in x1:
    ax.scatter(pos, y1[i], c='b', marker='.')
    i += 1
    plt.pause(0.01)
plt.show()

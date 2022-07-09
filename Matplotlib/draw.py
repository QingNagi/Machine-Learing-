import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse, Circle  # 画图函数
fig = plt.figure(figsize=(3, 3))
axes = fig.add_subplot(1, 1, 1)
square = plt.Rectangle((0.2, 0.2), 0.2, 0.2, color='g', alpha=0.8)  # alpha=0.8 设置矩形背景色的透明度

square1 = plt.Rectangle((0.5, 0.5), 0.2, 0.4, color='c', alpha=0.7, angle=120)

rectangle = plt.Rectangle((0.5, 0.2), 0.45, 0.2, color='b', alpha=0.6, linestyle='--')

E1 = Ellipse(xy=(0.7, 0.5), width=0.4, height=0.2, angle=30, facecolor='y', alpha=0.4)

C1 = Circle(xy=(0.25, 0.75), radius=0.2, alpha=0.3)

p1 = plt.Polygon([[0.7, 0.5], [0.6, 0.7], [0.9, 0.7], [0.9, 0.5]], color='m', alpha=0.4)


axes.add_patch(square)
axes.add_patch(square1)
axes.add_patch(rectangle)
axes.add_patch(E1)
axes.add_patch(C1)
axes.add_patch(p1)
plt.show()

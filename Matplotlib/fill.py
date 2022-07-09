import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(121)
x0 = np.linspace(0, 2*np.pi, 100)
y11 = np.sin(x0)
y12 = np.sin(2*x0)
plt.fill(x0, y11, facecolor="g", alpha=0.7)
plt.fill(x0, y12, facecolor="b", alpha=0.7)
plt.title('fill')


ax1 = fig.add_subplot(122)
x = [1, 1, 2, 2, 3, 3, 4, 4]
y = [1, 2, 2, 1, 1, 2, 2, 1]
y1 = [1, 1, 1, 1, 1, 1, 1, 1]
plt.plot(x, y)
plt.plot(x, y1)
cmap = plt.cm.get_cmap("winter")   # 设置冬天颜色
plt.fill_between(x, y, y1, alpha=0.6, hatch='/', cmap=cmap)  # 两条曲线的相交内填充
plt.show()
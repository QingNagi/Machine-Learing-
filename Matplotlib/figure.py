import matplotlib.pyplot as plt
import numpy as np
s1 = plt.figure()
print("first figure ID:", s1.number)
s2 = plt.figure('second')
print('second figure ID:', s2.number)
plt.show()

s1 = plt.figure('Ok', figsize=(7, 5), facecolor='g', edgecolor='r')
plt.plot([1, 2, 3, 4])
s2 = plt.figure(figsize=(7, 5), facecolor='g', edgecolor='r', frameon=False)  # 取消背景色
plt.plot([1, 2, 3, 4])
plt.show()

t1 = np.arange(0, 5, 0.1)
t2 = np.arange(0, 5, 0.02)
plt.figure(1)
plt.subplot(221, facecolor='m')   # 背景颜色
plt.plot(t1, t1, 'bo', 'k')
plt.subplot(222, title='cos line')
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.subplot(2, 2, 3, projection='polar')  # 极坐标图
plt.plot(t2, t2, 'g--')
plt.subplot(224, frameon=False)    # 消除边框
plt.plot(t2, np.sin(2*np.pi*t2), 'g--')
plt.show()


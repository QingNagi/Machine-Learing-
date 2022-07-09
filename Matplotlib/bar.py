import matplotlib.pyplot as plt
import numpy as np
import matplotlib
plt.rc('font', family='simhei', size=10)
plt.rc('axes', unicode_minus=False)
c = ['四', '五', '六']
x = np.arange(len(c))*0.8
g = [10, 10, 22]
b = [20, 19, 19]
b1 = plt.bar(x, height=g, width=0.2, alpha=0.7, color='r', label='women')

b2 = plt.bar([x1+0.2 for x1 in x], height=b, width=0.2, alpha=0.7, color='g', label='men')
plt.title('population statistics')
plt.legend()
plt.ylim(0, 30)
plt.ylabel("population")

plt.xticks([index + 0.1 for index in x], c)
plt.xlabel("class")
for i in b1:
    height = i.get_height()   # 获取相应高度b
    plt.text(i.get_x() + i.get_width() / 2, height+1, str(height), ha="center", va="bottom")
for i2 in b2:
    height = i2.get_height()
    plt.text(i2.get_x() + i2.get_width() / 2, height + 1, str(height), ha="center", va="bottom")
plt.show()

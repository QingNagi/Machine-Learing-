import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from perceptron import Perceptron
from convenience_function import plot_decision_regions
df = pd.read_csv('iris.data', header=None)  # 读入数据
df.tail()
# print(df)
# select setosa and versicolor
y = df.iloc[0:100, 4].values   # 提取前100个数据的第4个数据值
y = np.where(y == 'Iris-setosa', -1, 1)  # 将其判定为-1 1

# extract sepal length and petal length
x = df.iloc[0:100, [0, 2]].values  # 只保留两个属性

# plot data
plt.scatter(x[:50, 0], x[:50, 1], color='r', marker='o', label='setosa')
plt.scatter(x[50:100, 0], x[50:100, 1], color='b', marker='x', label='versiolor' )
plt.xlabel('sepal length[cm]')
plt.ylabel('petal length[cm]')
plt.legend(loc='best')   # 标签框的位置
plt.show()

ppn = Perceptron(eta=0.1, n_iter=10)  # 给定学习率和学习次数
ppn.fit(x, y)    # 传入数据
plt.plot(range(1, len(ppn.errors_) + 1), ppn.errors_, marker='o')
plt.xlabel('Epcohs')
plt.ylabel('Number of updates')
plt.show()

plot_decision_regions(x, y, classifier=ppn)
plt.xlabel('sepal length[cm]')
plt.ylabel('petal length[cm')
plt.legend(loc='best')
plt.show()

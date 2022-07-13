import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap


def plot_decision_regions(X, y, classifier, resolution=0.02):
    # setup marker generator and color map
    markers = ('s', 'x', 'o', '^', 'v')
    colors = ('r', 'b', 'l', 'g', 'c')
    cmap = ListedColormap(colors[:len(np.unique(y))])

    # plot the decision surface
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x_2max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution), np.arange(x2_min, x_2max, resolution))
    z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)    # ravel将矩阵拉直为向量 预测整个区域进行赋值
    z = z.reshape(xx1.shape)
    plt.contourf(xx1, xx2, z, alpha=0.4, cmap=cmap)  # 以z为高在二维屏幕上画3D投影图
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())

    # plot class samples
    for idx, cl in enumerate(np.unique(y)):    # unique 除开其中重复的元素 enumerate 给每个y一个索引0 1 2 3 idx为y的类别 -1 1
        plt.scatter(x=X[y == cl, 0],
                    y=X[y == cl, 1],
                    c=colors[idx],   # 获取类别
                    alpha=0.7,
                    marker=markers[idx],
                    label=cl,
                    edgecolors='k')
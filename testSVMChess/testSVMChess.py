import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler

# pandas处理数据集
# sklearn.model_selection实现数据集分割，自动调参
# sklearn.svm线性支持向量分类

# 读取数据
data = pd.read_csv('krkopt.data', header=None)
data.dropna(inplace=True)  # 不创建新的对象，直接对原始对象进行修改


def svm_c(x_train, x_test, y_train, y_test):
    # rbf核函数，设置数据权重
    svc = SVC(kernel='rbf', class_weight='balanced', )
    c_range = np.logspace(-5, 15, 11, base=2)
    gamma_range = np.logspace(-9, 3, 13, base=2)
    # 网格搜索交叉验证的参数范围，cv=3,3折交叉
    param_grid = [{'kernel': ['rbf'], 'C': c_range, 'gamma': gamma_range}]
    grid = GridSearchCV(svc, param_grid, cv=3, n_jobs=-1)
    # 训练模型
    clf = grid.fit(x_train, y_train)
    # 计算测试集精度
    score = grid.score(x_test, y_test)
    print('精度为%s' % score)


# 样本数值化 a,b,c...h 转化为 1,2,3...8
for i in [0, 2, 4]:
    data.loc[data[i] == 'a', i] = 1
    data.loc[data[i] == 'b', i] = 2
    data.loc[data[i] == 'c', i] = 3
    data.loc[data[i] == 'd', i] = 4
    data.loc[data[i] == 'e', i] = 5
    data.loc[data[i] == 'f', i] = 6
    data.loc[data[i] == 'g', i] = 7
    data.loc[data[i] == 'h', i] = 8

# 将标签数值化 -1表示将死，1表示和棋
data.loc[data[6] != 'draw', 6] = -1
data.loc[data[6] == 'draw', 6] = 1

# 归一化处理 Z-score标准化方法 （经过处理的数据符合标准正态分布，即均值为0，标准差为1）
for i in range(6):
    data[i] = (data[i] - data[i].mean()) / data[i].std()

# 拆分训练集和测试集    train_teat_split() https://www.cnblogs.com/bonelee/p/8036024.html 省略random_state=0
X_train, X_test, y_train, y_test = train_test_split(data.iloc[:, :6], data[6].astype(int), test_size=0.82178500142572)

svm_c(X_train, X_test, y_train, y_test)


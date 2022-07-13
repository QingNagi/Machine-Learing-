import pandas as pd
import numpy as np
Goods = {'apple': [100, 8, 0, 20], 'pear': [0, 21, 8, 15], 'banana': [88, 31, 45, 21], 'origen': [200, 150, 100, 20]}
Records = pd.DataFrame(Goods, index=['one', 'two', 'three', 'four'])
print(Records)
Records.iloc[0, 1] = 5
print(Records.iloc[0, :])
Records.iloc[3, :] = 30         # 批量更改
print(Records.iloc[3, :])
s1 = pd.Series([10, 20, 30, 40], index=['one', 'two', 'three', 'four'])
Records['pear'] = s1
print(Records)
print(Records.where(Records < 100, 160))
b = np.ones((4, 4), dtype=bool)
b[1, 1] = False
Records.where(b, 40, inplace=True)   # 更换第二行第二列元素
print(Records)


def f1(x):
    return x != 100


f = np.array(f1(Records), dtype=bool)
Records.where(f, 110, inplace=True)    # 在为False的地方进行替换
print(Records)

del(Records['pear'])   # 删除列
print(Records)

print(Records.drop('origen', axis=1))
print(Records.drop('three'))
ic = Records.drop(index='two', columns='apple')
print(ic)
print(Records)
d1 = pd.Series([100, 50, 10], name='five', index=['apple',  'banana', 'origen'])
B3 = Records.append(d1)   # 加入行
print(B3)
d2 = np.array([29, 49, 2, 20])
Records['water'] = d2           # 加入列
print(Records)

Records.insert(3, 'lizi', [20, 30, 40, 100])   # 在对应位置插入列
print(Records)
Records.loc[:, 'malen'] = [20, 10, 15, 10]   # 加入新的一列
print(Records)
print(Records.sort_values(by='apple', ascending=False, axis=0))   # ascending默认为True 为升序
print(Records.sort_values(by='two', ascending=False, axis=1))
print(Records.sort_values(by=['two', 'three'], ascending=False, axis=1))
Z = pd.DataFrame(np.arange(1, 10).reshape(3, 3), columns=['one', 'two', 'three'])
print(Z)
print(Z.sort_values(by=1, axis=1))
print(Z.rank())   # 以行排名升序排名默认
print(Z.rank(method='max'))   # 遇到相同排名时候取最大的排名
print(Z.rank(method='min'))
print(Records.rank(method='first'))    # 先出现的排名小（同样排名时）
print(Records.rank(method='dense'))    # 核排名方法
print(Records.rank(axis=1, method='min'))   # 以行为组排名
print(Records.size)
print(Records.shape)
print(Records.info())       # 查看基本信息
D = pd.DataFrame(np.ones(4).reshape(2, 2), dtype=bool)   # 指定为布尔类型
print(Records.all(axis=1))  # 按行检查，返回是否全为T
print(Records.columns)    # 返回列索引
print(Records.index)        # 返回行索引


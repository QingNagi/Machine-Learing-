import np as np
import numpy as np
import pandas as pd
from IPython.display import display
data = {'Tom': [100, 88, 98], 'John': [89, 97, 100], 'Alice': [88, 99, 100]}
a = pd.DataFrame(data)        # 加入display才能看到
display(a)

data1 = np.array([[18, 19, 20], [2, 3, 4], [21, 22, 23]])
A = pd.DataFrame(data1)
print(A)

s1 = pd.Series(np.array(['Tom', 'John', 'Alice', 'Jack']))
s2 = pd.Series(np.array([1, 10, 101, 1001]))
dic = {'name': s1, 'room': s2}
B = pd.DataFrame(dic)
print(B)

C = pd.DataFrame(np.arange(9).reshape(3, 3))
print(C)

Score = np.array([[95, 100, 99], [90, 80, 100], [85, 100, 100]])
E = pd.DataFrame(Score, columns=['语文', '数学', '英语'], index=['Tom', 'John', 'Alice'])
print(E)

e1 = E['语文']
print(e1)
print(E[:2])  # 行索引
print(B.values)
print(B.values[:, 0])       # 列索引 第一列
print(B.values[0, :])       # 行索引 第一行
print(E.iloc[1])             # 获取第二行内容
print(E.iloc[[1, 2]])       # 列表形式索引第二 三行元素
print(E.iloc[[True, False, False]])   # bool型索引
print(E.iloc[0, 2])    # 获取一个值
print(E.head(2))     # 读取前n行
print(E.tail(2))       # 取后n行



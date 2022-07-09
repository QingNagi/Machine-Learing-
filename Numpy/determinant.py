import numpy as np
d = np.arange(4).reshape(2, 2)
print(d)
v1 = np.linalg.det(d)       # 计算行列式
print('%.2f' %(v1))
vm = np.vander([1, 2, 3])  # 范德蒙德行列式
print(vm)
a = np.arange(1, 10).reshape(3, 3)
print(np.tril(a))   # 生成下三角矩阵
print(np.tril(a, -1))  # k = -1 对角线为0
print(np.tril(a, 1))   # k = 1
print(np.tril([1, 2, 3]))   # 提供对角线元素
print(np.triu(a))  # 上三角

z = np.tri(2, 2, 0, dtype=int)
print(z)
z1 = np.tri(2, 3, -1, dtype=int)
print(z1)
print(np.diag(a))    # 获取对角线元素   K可调节
a2 = np.diagflat([[1, 2], [3, 4]])  # k可调节生成对角线元素
print(a2)




import numpy as np
v1 = np.arange(3)   # 列向量
v2 = np.linspace(1, 3, 3).reshape(3, 1)
print(v1)
print(v2)
print(np.outer(v1, v2))
print(np.kron(v2, v1))   # 前列乘后列
print(np.inner([1, 2, 3], [1, 1, 1]))   # 向量内积
print(np.vdot(np.array([1 + 5j, 2 + 2j]), np.array([0 - 2j, 1 + 1j])))   # 支持复数
print(np.cross(v1, v1))    # 交叉积

A = np.matrix([[3, -1], [-1, 3]])
w, v = np.linalg.eigh(A)      # w特征值，v特征向量
print(w, v)
A2 = np.eye(3, 3)
print(np.linalg.eigvals(A2))     # 求方阵特征值
A1 = np.array([[1, 1], [1, 1]])
print(np.linalg.eigvals(A1))

A = np.array([[1, -2j], [2j, 5]])
L = np.linalg.cholesky(A)    # 平方根分解法  A为正定方阵 返回L （下三角）
print(L)
print(np.linalg.qr(A))  # 将矩阵分解为一个正交矩阵和一个上三角矩阵


a = np.random.randn(9, 6) + 1j*np.random.randn(9, 6)
u, s, vh = np.linalg.svd(a, full_matrices=True)      # 奇异值分解
print(u, s, vh)







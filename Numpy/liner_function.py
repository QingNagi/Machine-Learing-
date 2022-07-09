import numpy as np
A = np.matrix([[1, -1, -1], [2, -1, -3], [3, 2, -5]])
b = [2, 0, 1]
x = np.linalg.solve(A, b)  # 解线性方程 要有解
print(x)

a = np.array([[3, 1], [2, 1], [1, 1], [0, 1]])
c = np.array([-1, 0.5, 2, 0.3])
x1, x2 = np.linalg.lstsq(a, c, rcond=None)[0]    # 最小二乘解
print("%.2f, %.2f"%(x1, x2))


a = np.eye(6)
a.shape = (2, 3, 1, 2, 3)
b = np.random.randn(2, 3)
x = np.linalg.tensorsolve(a, b)
print(x.shape)
print(x)


a = np.arange(12).reshape(3, 4)
b = np.arange(12).reshape(4, 3)
c = np.tensordot(a, b, axes=([1, 0], [0, 1]))
print(c)

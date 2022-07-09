import numpy as np
a = np.arange(1, 10).reshape(3, 3)
A = np.matrix(a)     # 建立矩阵
print(A)
B = np.matrix([[1, 2, 3], [3, 4, 3], [5, 6, 3]])
print(B)
C = np.bmat(([[A], [B]]))   # 嵌套A B矩阵
print(C)
x = np.arange(3)
y = np.arange(4)
X, Y = np.meshgrid(x, y)    # 构建网格矩阵 x 3 y 4 网格坐标在X Y中
print(X)
print(Y)
x1, y1 = np.indices((3, 3))  # 返回网格索引
print(x1, '\n', "y", y1)
print(A.T)      # 转置矩阵

m1 = np.arange(24).reshape(2, 3, 4)   # 3维为2 （段），二维为 3（列）， 一维为4（行）
print(np.moveaxis(m1, 0, -1))   # 移动轴位置 0 为开始移动位置 -1 为移动方向 -1 为向大的维数循环移动 1->2->3->1
print(np.moveaxis(m1, -1, 0))

print(np.swapaxes(m1, 0, 2))   # 交换1 3维
print(np.transpose(A))
print(np.transpose(m1, (0, 2, 1),).shape)     # .shape显示维度 只转置2 3维

D = np.matrix([[1, 2], [3, 4]])
mv = np.linalg.inv(D)    # 必须要可逆才行  方阵 matrix
print(mv)
print(D*mv)
print((np.linalg.pinv(A))*A)    # 伪逆矩阵
print(A)
print(B)
print(np.dot(A, B))  # 内积
print(np.inner(A, B))  # 同一维度的元素乘积 前行乘前行
print(np.matmul(A, B))  # 矩阵积



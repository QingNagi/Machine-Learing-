import numpy as np
from activation_function import *
# A = XW + B
# 2 3 2 2 每层的神经元数目
X = np.array([1.0, 0.5])
W1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
B1 = np.array([0.1, 0.2, 0.3])

print(W1.shape)
print(X.shape)
print(B1.shape)

A1 = np.dot(X, W1)    # 内积
print(A1)
z1 = sigmoid(A1)     # 隐层的输出函数为sigmoid
print(z1)

W2 = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
B2 = np.array([0.1, 0.2])

A2 = np.dot(z1, W2) + B2
z2 = sigmoid(A2)
print(z2)

W3 = np.array([[0.1, 0.3], [0.2, 0.4]])
B3 = np.array([0.1, 0.2])

A3 = np.dot(z2,W3) + B3
Y = A3   # 未定义输出层的激活函数 直接输出
print(Y)

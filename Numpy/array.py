import numpy as np

a1 = np.array([1, 2, 3, 4])
type(a1)
a2 = np.array((1, 2, 3, 4))    # 可用元组
print(a1, "\n", a2)

b1 = np.array([[1, 2, 3], [4, 5, 6]])

b2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(b1, "\n", b2)
# 3D
c1 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(c1)

r1 = np.array(['a', '凪', 1])   # 输入类型不一 输出为字符串
print(np.alltrue(c1))     # 是否都为非0值

print(r1.dtype)    # 数组的类型

h1 = np.arange(5)
h2 = np.arange(0, 5)
h3 = np.arange(0, 5, 0.1)
h4 = np.arange(5, 0, -1)   # 逆序
print(h1, "\n", h2, "\n", h3, "\n", h4)

# 等分数列
i1 = np.linspace(0, 1, 2)
i2 = np.linspace(0, 4, 4)
print(i1, "\n", i2,)

z1 = np.zeros(5)
z2 = np.zeros((3, 3))
print(z1, "\n", z2)

o1 = np.ones((2, 3))
print(o1)

# 全0矩阵
e1 = np.empty((5, 5))
print(e1)

# y=lg2--log3
print(np.logspace(2.0, 3.0, num=4))

f1 = np.full(5, 10)
f2 = np.full((3, 3), 8)
f3 = np.full((5, 5), np.inf)
print(f1, "\n", f2, "\n", f3)

print(np.eye(4))
# 重复5次每个元素
print(np.repeat([0, 1, 0], 5))

ar1 = np.array([['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']])
print("维数,形状,元素个数，类型，元素字节大小", ar1.ndim, ar1.shape, ar1.size, ar1.dtype, ar1.itemsize)

t1 = np.arange(9)
t2 = t1.reshape(3, 3)
m1 = np.ones(9).all()
m2 = t2.all(axis=1)     # axis=1 以行为单位 0:以元素为单位 （数字为维数）
m3 = t2.any(axis=1)     # 是否存在T
print(t1, "\n", t2, "\n", m1, "\n", m2, "\n", m3)

ar2 = ar1
print(id(ar1))
print(id(ar2))     # id相同为映射关系
ar3 = ar1.copy()        # ID不同
print(id(ar3))

print(np.ones(9, dtype=int).astype(float))   # 转换元素类型

<<<<<<< HEAD
z1 = np.vstack((a1, a2))
print(z1)   # 垂直对接 列数要一样
z = np.hstack((a1, a2))
print(z)   # 水平对接 行数要一样
print(np.hsplit(z, 2))  # 水平平分
print(np.vsplit(z1 ,2))  # 垂直切分



=======
>>>>>>> 9581f5bdf70009e6f13abc057161653c57d02f91


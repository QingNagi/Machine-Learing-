import numpy as np
n1 = np.arange(10)
print(n1[9], n1[-2])
n1[1] = 9
print(n1)

n2 = n1.reshape(2, 5)
print(n2[1, 0])
n2[1, 1] = 8
print(n2)

n3 = np.arange(12).reshape(2, 2, 3)
print(n3[1, 0, 0])
n3[0, 0, 0] = 7
print(n3)
print(n3[1, ...])
print(n3[..., 2])
print(n3[1, ..., 2])   # ...表示某维度全部内容
print(n2[1][1])

print(n1)
print(n1[1:4])
print(n1[:5])    # 切到下标为5之前
print(n1[:-1])
print(n1[::2])   # step = 2

n4 = np.arange(9).reshape((3, 3))

print(n4)
print(n4[1:3])   # 切去2 3row
print(n4[:, 2])    # row 切片 column 指定 （每一row的第3个元素切取出来）
print(n4[:, :2])    # 切取每一行前两列元素
print(n4[1, 2:])    # 切取2row 3column

# 3 维 （段，行，列）
print(n3)
print(n3[1, 1, :])

# Fancy Indexing
fi1 = np.array(['tom cat', 'jiafei cat', 'boshi cat', 'black cat', 'duanlian cat', 'tianyuan cat'])
f1 = np.array([1, 2, 4, 5])
print(fi1[f1])    # 用matrix来进行index
# 2维时matrix索引row

x = np.array([[0, 1, 2]])
y = np.array([0, 1, 2])
print(n4)
print(n4[x, y])    # 索引 x row  y column的元素
b1 = np.array([[True, False, False], [False, True, False], [False, False, True]])   # 布尔索引 要求与原来matrix形状一样
print(n4[b1])

for g in n1:
    print(g)

studs = np.array([[1, 'jiafei', 'male'], [2, 'kitty', 'female'], [3, 'boshi', 'male']])
for g1 in studs:
    print(g1)        # 2 维每次读出的是row


import numpy as np
a = np.random.rand(2, 6)   # 产生随机数 每次不一样
print(a)
b = np.random.randn(6)   # 标准正态
print(b.max(), b.min())
print(np.sum(b))
c = np.random.randint(0, 4, size=8)  # 固定范围的随机数目 (0 - 3) int型
print(c)

r1 = np.random.normal(0, 7, 10)   # (期望， 偏差， 个数)
print(r1)

r2 = np.random.uniform(0, 4, size=(4, 4))   # 均匀分布的随机数（0-3）
print(r2)

s1 = np.random.permutation(10)   # 乱序排列 （0-10）
print(s1)
s2 = np.random.permutation(s1)  # 将s1中进行乱序排列
print(s2)

np.random.shuffle(s2)      # 进行打乱打不反回任何值
print(s2)
print(np.random.choice(s2, 3, replace=False))    # 随机抽取3个数 不可重


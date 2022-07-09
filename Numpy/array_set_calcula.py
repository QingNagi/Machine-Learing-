import numpy as np
cx = np.array(['tom', 'jack', 'tom', 'alice', 'jack'])
print(np.unique(cx))   # 显示不重复的内容
y1 = np.array(['tom', 'jack', 'tim', 'mike'])
print(np.intersect1d(cx, y1))   # 显示交集
print(np.union1d(cx, y1))    # 显示并集 不重复
print(np.setdiff1d(cx, y1))   # 显示差集 cx中出现 y1中未出现的值
print(np.setxor1d(cx, y1))     # 异或集 各自中单独出现的元素
print(np.in1d(cx, y1))      # 判断cx中的元素是否在y1中出现

a1 = np.arange(12).reshape(3, 4)
print(a1)
a2 = np.array([[np.nan, 10, 9], [np.nan, 10, 9], [np.nan, 10, 9]])
print(a2)

print(np.sum(a1))
print(np.sum(a1, axis=0))   # axis=0按列和 1 按行求和  ,后面算法也都可以用这个方法
print(np.sum(a2))      # 无法进行nan计算
print(np.nansum(a2))  # 进行含有nan的计算
print(np.prod(a1))      # 对所有的函数进行求乘积
print(np.nanprod(a1))    # 包含nan
print(np.max(a1))
print(np.nanmax(a2))
print(np.min(a1))
print(np.nanmin(a2))
print(np.cumsum(a1))     # 累积和统计
print(np.cumprod(a1))
print(np.mean(a1, axis=0))
print(np.average(a1, axis=0, weights=[0.6, 0.2, 0.2]))  # 权重均值
print(np.median(a1, axis=0))
print(np.var(a1, axis=0))
print(np.std(a1, axis=0))
print(np.ptp(a1, axis=0))  # 极值


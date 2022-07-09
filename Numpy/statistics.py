import numpy as np
a1 = np.arange(12).reshape(3, 4)
print(np.percentile(a1, 50, axis=0))   # 百分位数
a2 = np.arange(10)
print(np.diff(a2, n=1))
print(np.diff(a2, n=2))  # 在n=1基础上再进行以此后项减前项
print(np.ediff1d(a2))
print(np.ediff1d(a2, to_begin=[0, 0], to_end=[10]))  # 在结果中插入开始 和结束插入元素
print(np.gradient(a2))
print(np.gradient(a1))   # 梯度计算

print(np.trapz([[1, 2, 3], [4, 5, 6]], axis=1))    # 以行为点位进行定轴积分 梯形求积分面积 （（4+6）*2）/2 = 10

a3 = np.random.randint(1, 20, (3, 3))
print(a3)
print(np.sort(a3))   # 每行排序 不改变原数列
print(np.sort(a3, axis=0))    # 按列排


ar = np.arange(6).reshape(2, 3)
np.place(ar, ar > 3, [44, 55])    # 替换大于3的元素
print(ar)
np.put(ar, [3, 4, 5], [0, 0])    # 将3，4，5位置替换为0
print(ar)
np.put_along_axis(a3, np.array([[1], [1], [2]]), 0, axis=1)  # 将一行中的第二个元素替换为0
print(a3)
np.put_along_axis(a3, np.array([[0, 1]]), 1, axis=1)  # 将所以一二列中元素都替换
print(a3)
np.fill_diagonal(a3, 5)   # 替换主对角线上元素
print(a3)
print(np.delete(a3, np.s_[:2], axis=1))  # 删除1，2列
print(np.delete(a3, 1, axis=1))  # 删除第二列
print(np.delete(a3, np.arange(2), axis=0))  # 删除1 2 行
print(np.insert(a3, 3, [2, 2, 2], axis=1))   # 插入 新列
print(np.append(a3, [[1, 1, 1], [2, 2, 2], [3, 3, 3]], axis=1))   # 在后面添加列
a5 = np.random.randn(16).reshape(4, 4)
print(a5)
print(np.around(a5))   # 四舍五入为int
print(np.rint(a5))    # 去最接近整数
print(np.fix(a5))    # 向下取整
print(np.floor(a5))  # 舍去小数部分
print(np.ceil(a5))      # 向上取整
print(np.where(a3 <= 2, a3, 10))  # 将小于2的元素保留 其他的替换为10
print(np.abs(a5))






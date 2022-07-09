import numpy as np
data = np.array([['成分', '100k牛奶', '100k面粉', '100k乳清', '营养要求'],
                ['碳水化物', '52', '34', '74', '45'],
                ['蛋白质', '36', '51', '13', '33'],
                ['脂肪', '0', '7', '1.1', '3']])
np.savetxt(r'food.csv', data, delimiter=',', fmt='%s')
data1 = np.loadtxt(r'food.csv', delimiter=',', dtype=np.str)
print(data1)
data2 = data1[1:, 1:]  # 舍去头行头列
data2 = data2.astype(np.float)
print(data2)
r = np.linalg.solve(data2[0:3, 0:3], data2[:, 3])   # 进行求解
print(r)
print(sum(r*data2[0, 0:3]))   # 验证求解

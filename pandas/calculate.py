import pandas as pd
import numpy as np
C = pd.DataFrame(np.array([[1, 2, 3, 4], [100, 9, 25, 16], [-3, 0, 15, 55]]))
print(C)
print(C+5)  # 全加5
print(C + [-5, 10, 0, 8])
print(C+pd.Series([1, 2, 3, 4]))     # 给行加
print(C+np.array([[1], [2], [3]]))   # 给列加
print(C-np.arange(4))
print(C*2)
print(C/[1, 2, 3, 4])
print(C//2)    # 取整运算
print(C%2)
print(np.log2(C))
print(C**2)
print(C >= 1)
print(C.all(skipna=False))   # 对none 和 nan进行判定
print(C.any())      # 或计算 只有有非0值就True
print(C.empty)          # 有空值就True

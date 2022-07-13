import pandas as pd
import numpy as np
import io
F = pd.DataFrame(np.array([[100, 200, 300], [20, 10, 15]]))
F.to_csv(r't1.csv')
F.to_csv(r't2.csv', sep=' ')

print(pd.read_csv(r't1.csv'))

str1 = '1, 2, 3\n4, 5, 6\n'
out_s = io.StringIO()       # 在内存建立字符对象
out_s.write('x, y, z\n')    # 建立列索引值
out_s.write(str1)           # 建立数据
out_s.seek(0)                   # 设置字符串的开始位置
print(pd.read_csv(out_s))    # 从内存中读取

import numpy as np
r1 = np.array(['a', '凪', '1'])   # 输入类型不一 输出为字符串
np.alltrue(r1)     # 是否都为非0值

r1.dtype     # 数组的类型

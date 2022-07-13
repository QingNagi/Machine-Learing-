import pandas as pd
import numpy as np
from pandas import RangeIndex

s1 = pd.Series(np.array([1, 10, 101, 10001]))
print(s1)
print(s1.index)
print(s1.values)
s2 = pd.Series(np.arange(3), index=['one', 'two', 'three'])  # 添加索引
print(s2)
s3 = pd.Series({'tom':16, 'john':18, 'alice':12})
print(s3)
s4 = pd.Series(np.ones(3), dtype=bool, name='No')
print(s4)
s5 = pd.Series(np.arange(10, 20))
print(s5)
print(s5[:3])
s6 = pd.Series([10, 38, 100, 12], index=['Tom', 'John', 'Alice', 'Mike'])
print(s6)
animal = pd.Series(['lion', 'wolf', 'bear'], index=[2, 0, 1])
print(animal[0])
print(animal[np.array([0, 1])])
s5[1] = 0
print(s5)
print(s5.replace(15, 90))   # 换的最后的数
del(s5[7])
one = s5.pop(0)
print(one)
print(s5)
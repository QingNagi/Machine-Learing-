import pandas as pd
import numpy as np
G = pd.DataFrame(np.arange(10, 19).reshape(3, 3), columns=['one', 'two', 'three'], index=['tom', 'john', 'alice'])
G1 = G.reindex(index=['alice', 'john', 'tom'])
G3 = G.reindex(labels=['alice', 'john', 'tom'], axis=0)  # 更改索引顺序
print(G)
print(G1)
print(G3)
G.index = ['china', 'japan', 'usa']  # 改行索引
print(G)
G.columns = ['apple', 'pear', 'orange']         # 改列索引
print(G)

i_m = [['6.1', '6.1', '6.2', '6.2'], ['max', 'min', 'max', 'min']]
c_m = [['2019', '2019', '2020', '2020'], ['man', 'woman', 'man', 'woman']]
Data = np.array([[290, 295, 294, 295], [200, 201, 220, 219], [293, 294, 295, 294], [199, 205, 201, 208]])
M = pd.DataFrame(Data, index=i_m, columns=c_m)
print(M)

Mi = pd.MultiIndex.from_arrays(i_m, names=['class', 'score'])
Mc = pd.MultiIndex.from_arrays(c_m, names=['year', 'sex'])
MM = pd.DataFrame(Data, index=Mi, columns=Mc)
print(MM)
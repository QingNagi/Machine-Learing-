import numpy as np
A = np.array([1, 1, 1])
B = np.array([3, 1.5, 1.5])
C = np.array([4, 2, 2])
Dab = np.sqrt(np.sum(np.square(A-B)))
Dac = np.sqrt(np.sum(np.square(A-C)))
Dbc = np.sqrt(np.sum(np.square(B-C)))
print(Dab, Dac, Dbc)
s = (Dab + Dac + Dbc) / 2
area = np.sqrt(s*(s-Dac)*(s-Dab)*(s-Dbc))    # 海伦公式
print(area)
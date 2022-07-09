import numpy as np
import matplotlib.pyplot as plt
t = np.arange(8)
y = np.array([27.0, 26.8, 26.5, 26.3, 26.1, 25.7, 25.3, 24.8])
A = np.c_[t, np.ones_like(t)]    # y = at1 + bt2  [t1, t2]
print('A', A)
print(np.ones_like(t))
ab = np.linalg.lstsq(A, y, rcond=None)[0]    # [a, b]
print(ab)
plt.rc('font', size=16)
plt.plot(t, y, 'o', label='Original data', markersize=5)
plt.plot(t, np.dot(A, ab), 'r', label="Fitted line")   # y = at1 + bt2  # A.dot(ab)一样
plt.legend()
plt.show()
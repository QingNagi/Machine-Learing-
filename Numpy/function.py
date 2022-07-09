import numpy as np
import matplotlib.pyplot as plt
print(np.exp([1, 2, 3]))
a = np.arange(3)
print(np.exp(a))
c1 = np.array([np.e, np.e])
print(np.log(c1))
print(np.log10(10))
print(np.log2(5))
print(np.log1p(0.00000000000001))  # 更高精度
print(np.log(0.000000000001+1))

x1 = np.linspace(0, 2*np.pi, 10)
y1 = np.sin(x1)
plt.plot(x1, y1)
print(np.sin(np.pi/2))  # sin(pi/2) = 1
y2 = np.cos(x1)
plt.plot(x1, y2)
plt.show()

y3 = np.tan(x1)
plt.plot(x1, y3)
plt.show()

x2 = np.linspace(-1, 1)
y4 = np.arcsin(x2)
plt.plot(x2, y4)

y5 = np.arccos(x2)
plt.plot(x2, y5)
plt.show()

x3 = np.linspace(-10, 10)
y6 = np.arctan(x3)
plt.plot(x3, y6)
plt.show()

y7 = np.sinh(x3)
y8 = np.cosh(x3)
y9 = np.tanh(x3)
plt.plot(x3, y7)
plt.plot(x3, y8)
plt.show()
plt.plot(x3, y9)
plt.show()

print(np.degrees(x1))  # 转化为角度
print(np.rad2deg(x1))
a = np.degrees((x1))
print(np.radians(a)/np.pi)   # 转化为弧度
print(np.hypot([3, 3], [4, 4]))   # 勾股定理求出斜边长

import numpy as np
import matplotlib.pylab as plt

def step_function(x):
    if x > 0:
        return 1
    else:
        return 0


def step_function1(x):
    y = x > 0           # 布尔类型 > 0为Ture
    return y.astype(np.int)         # 转换为整型 T=1 F=0


x = np.arange(-5.0, 5.0, 0.1)
y = step_function1(x)
plt.plot(x,y)
plt.ylim(-0.1, 1.1)



def sigmoid(x):
    return 1 / (1 + np.exp(-x))


x = np.array([-1.0, 1.0, 2.0])
z = sigmoid(x)
print(z)

x = np.arange(-5.0, 5.0, 0.1)
y = sigmoid(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)


def Relu(x):
    return np.maximum(0, x)


y = Relu(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()


import numpy as np
import matplotlib.pyplot as plt


def numerical_diff(f, x):   # 求导
    h = 1e-4
    return (f(x + h) - f(x-h)) / (2*h)


def function_1(x):
    return 0.01*x**2 + 0.1*x


x = np.arange(0.0, 20.0, 0.1)
y = function_1(x)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.plot(x, y)
plt.show()
print(numerical_diff(function_1, 10))


def function_2(x):
    return np.sum(x**2)   # x1**2 + x2**2


def function_tmp1(x0):
    return x0*x0 + 4.0**2.0


def function_tmp2(x1):
    return 3.0**2.0 + x1*x1


# 求偏导分别一个个求
print(numerical_diff(function_tmp1, 3.0))
print(numerical_diff(function_tmp2, 4.0))


def numerical_gradient(f, x):
    h = 1e-4    # 0.0001
    grad = np.zeros_like(x)    # 与x形状相同的grad

    for idx in range(x.size):
        tmp_val = x[idx]
        x[idx] = tmp_val + h
        fxh1 = f(x)

        x[idx] = tmp_val - h
        fxh2 = f(x)

        grad[idx] = (fxh1 - fxh2) / (2*h)
    return grad


print(numerical_gradient(function_2, np.array([3.0, 4.0])))
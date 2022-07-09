from diff_function import numerical_gradient
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm


def gradient_descent(f, init_x, lr=0.01, step_num=100):
    x = init_x

    for i in range(step_num):
        grad = numerical_gradient(f, x)
        x -= lr * grad

    return x


def function_2(x):
    return np.sum(x**2)


init_x = np.array([-3.0, 4.0])
print(gradient_descent(function_2, init_x, lr=0.01, step_num=10000))

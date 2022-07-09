import numpy as np

def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = x1*w1 +x2*w2
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1


x = np.array([0, 1])
w = np.array([0.5, 0.5])
b = -0.7
print(np.sum(w*x) + b)

a1 = AND(0, 0)
print(a1)
a2 = AND(0, 1)
print(a2)
a3 = AND(1, 0)
print(a3)
a4 = AND(1, 1)
print(a4)


def AND1(x1, x2):
    x1 = np.array([x1, x2])
    w1 = np.array([0.5, 0.5])
    b1 = -0.7
    tmp = np.sum(w1*x1) + b1
    if tmp <= 0:
        return 0
    else:
        return 1


a1 = AND1(0, 0)
print(a1)
a2 = AND1(0, 1)
print(a2)
a3 = AND1(1, 0)
print(a3)
a4 = AND1(1, 1)
print(a4)


def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1


def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1


a1 = OR(0, 0)
print(a1)
a2 = OR(0, 1)
print(a2)
a3 = OR(1, 0)
print(a3)
a4 = OR(1, 1)
print(a4)


a1 = NAND(0, 0)
print(a1)
a2 = NAND(0, 1)
print(a2)
a3 = NAND(1, 0)
print(a3)
a4 = NAND(1, 1)
print(a4)


def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y


a1 = XOR(0, 0)
print(a1)
a2 = XOR(0, 1)
print(a2)
a3 = XOR(1, 0)
print(a3)
a4 = XOR(1, 1)
print(a4)
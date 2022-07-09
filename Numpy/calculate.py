import numpy as np

one = np.ones(4).reshape(2, 2)
print(one)

two = np.arange(4).reshape(2, 2)
print(two)

print(one + two)
print(one + 1)   # 广播
one += 4
print(one)

one1 = np.arange(1, 10).reshape(3, 3)
print(one1)
print(one1 - np.full((3, 3), 5))

print(one * 2)    # 广播
print(one * two)   # 点乘
print(two / one)    # 点除
print(one / 2)
print(two % one)   # 求余
print(one ** two)   # 点幂
print(one ** 2)
print(one//2)  # 取整

one2 = np.array([[10+2j, 1-1j], [2j, 3+3j]])
f1 = np.array([1j, 2j])
print(one2 + f1)     # 广播

print(one == two)  # 对应元素比较
print(one != two)
print(one > two)
print(two > 2)

b = np.array([[True, False], [False, True]])
print(b)
print(two)
print(two & b)
print(two | b)   # 转化为二进制相与 000 ｜ 001 = 001 -> 1
print(~two)      # 转化为二进制取反 2 -> 0010 -> 1101 -> -3   0 -> 00 -> 11 -> -1
print(two << 2)  # 0001  <<2 -> 0100 ->4
print(two >> 2)
print(two & 2)   # 每一位与0010相与



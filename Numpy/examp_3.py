import numpy as np
trees = np.linspace(0, 100, 21)   # 平均间隔种21棵树 100m
print(trees)
price = np.full((21), 10)     # 单价10元
print(price)
i = 0
while i < 21:
    if i % 2 == 0:
        price[i] = 5
    else:
        price[i] = 10
    i += 1

print(price)
price2 = price * 2
print(price2)
price2[price2 == 20] = 1
price2[price2 == 10] = 0
print(price2)
trees1 = np.vstack((price, trees))
trees1.astype(int)
print(trees1)
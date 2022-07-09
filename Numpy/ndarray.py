import numpy as np
a = np.arange(9).reshape(3, 3)
print(a.data)  # 显示a的内存位置
a.shape = 9  # 改变a的形状
print(a)
b = a
print(b.data)
print(a.data)

b[0] = 1    # a b会被同时改变
print(a)

d = np.copy(a)
d[0] = 9  # 不会同时改变
print(a)

str1 = 'ABCabc'
print(str1.upper())
print(str1.lower())
print(str1.swapcase())  # 大小写转换
print(str1.replace('A', 'Z'))
print(str1.center(11, "-"))   # 居中处理
str2 = " Tom is a chinese "
print(str2.split())         # 以空格为分割点
print(str2.split(sep='a'))   # 以a为分割点
print(str2.strip())   # 去掉头尾的空格

print(str1.count('a'))    # 出现次数
print(str2.find('M'))  # 未找到返回-1
print(str1.isalpha())   # 是否全为字母
print(str1.isdigit())   # 是否全为数字
print(str2.islower())    # 是否为全小写  isupper 全大写
print(str2.isnumeric())   # 是否全为汉字数字








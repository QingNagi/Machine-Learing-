import numpy as np
from io import BytesIO
from io import StringIO
from tempfile import mkdtemp
import os.path as path

data = np.arange(16).reshape(4, 4)
np.savetxt(r'data.txt', data, delimiter=',')      # 分隔符为 ,
data1 = np.loadtxt(r'data.txt', delimiter=',')
print(data1)

data = "N/A, 20, A\n4,  , ???"       # 缺失数据数组
fill = dict(delimiter=',', dtype=int, names="f0, f3, f4",
            missing_values={0:"N/A", 'b':" ", 2:"???"},    # 缺失数据类型
            filling_values={0:0, 'b':0, 2:100})             # 缺失数据的补充
print(np.genfromtxt(BytesIO(data.encode()), **fill))     # 缺失数据补充后结果 BytesIO把字符转化为字节流


s = StringIO(u"1, 1.3,abcde")
data = np.genfromtxt(s, dtype=[('myint', 'i8'), ('myfloat', 'f8'), ('mystring', 'S5')], delimiter=',')   # 定义类型
print(data)

with open('data1.txt', 'w') as f:
    f.write("2000 Tom\n3000 Go\n3333 John")
regexp = r"(\d+)\s+(...)"        # 匹配数字(\d) 空白 \s 任何东西（。。。）
output = np.fromregex('data1.txt', regexp, [('Number', np.int64), ('Key', 'S3')])   # 定义类型
print(output)

np.save(r'data4', data)  # 存储为二进制文件.npy
B1 = np.load(r'data4.npy')
print(B1)    # 未加载出数据

X1 = np.linspace(1, 10, 10)
Y1 = np.sin(X1)
np.savez(r'Z1', X1, Y1)
Z1 = np.load(r"Z1.npz")
for get in Z1.items():
    print(get)
    print(type(get))

Z2 = np.fromfile(r'test.jpg')   # 以数组形式显示图片
print(Z2)
filename = path.join(mkdtemp(), 'newfile.dat')       # 临时文件夹
fp = np.memmap(filename, dtype='float32', mode='w+', shape=(4, 4))   # 内存映射
print(fp)
data4 = np.arange(16).reshape(4, 4)
fp[:] = data4[:]
print(fp)
del fp   # 删去fp

ds = np.DataSource(path.abspath(path.curdir))   # 支持本地和远程URL的操作
if ds.exists(r"https://numpy.org/doc/1.23/numpy-user.pdf"):
    ds.open(r"https://numpy.org/doc/1.23/numpy-user.pdf")
else:
    print('none')
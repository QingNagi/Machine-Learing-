# 此函数是在预定训练过的权重下来进行测试的 权重在mnist.pkl中
import numpy as np
import pickle
from mnist import load_mnist
from functions import sigmoid, softmax


def get_data():  # 获取数据
    (x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, flatten=True, one_hot_label=False)
    return x_test, t_test


def init_network():   # 从文件中读取初始化权重
    with open("sample_weight.pkl", 'rb') as f:
        network = pickle.load(f)
    return network


def predict(network, x):  # 3层网络
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = softmax(a3)

    return y

# 评价其识别精度
x, t = get_data()
network = init_network()

accuracy_cnt = 0
for i in range(len(x)):
    y = predict(network, x[i])
    p = np.argmax(y)          # 获取概率最高的元素的索引 argmax函数在NN中得到的取最大概率的结果为P
    if p == t[i]:
        accuracy_cnt += 1     # 识别正确

print("Accuracy:" + str(float(accuracy_cnt) / len(x)))


# 批量处理
batch_size = 100
accuracy_cnt = 0

for i in range(0, len(x), batch_size):
    x_batch = x[i:i+batch_size]
    y_batch = predict(network, x_batch)
    p = np.argmax(y_batch, axis=1)
    accuracy_cnt += np.sum(p == t[i:i+batch_size])
print("Accuracy:" + str(float(accuracy_cnt)/ len(x)))
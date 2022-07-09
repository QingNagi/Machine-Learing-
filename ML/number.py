import sys, os
sys.path.append(os.pardir)
from mnist import load_mnist


(x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False)  # 调用mnist (训练图像， 训练标签)


print(x_train.shape)
print(t_train.shape)
print(x_test.shape)
print(t_test.shape)



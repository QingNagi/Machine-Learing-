import numpy as np


class Perceptron(object):
    '''Perceptron classifier

    parameters
    eta : float
    learning rate (between 0 and 1)
    n_iter : int     传递数据
     Passes over the training dataset.
     initialization.

    Attributes
    w_ : ld-array
     Weights after fitting
    errors_ : list
     Number of misclassifications (update) in each epoch.
    '''

    def __init__(self, eta=0.01, n_iter=50, random_state=1):
        self.eta = eta
        self.n_iter = n_iter
        self.random_state = random_state

    def fit(self, X, y):
        '''Fit training data

        :param X: {array-like}, shape = [n_samples, n_features]
                Training vectors, where n_samples is the number of samples and n_feature is the number of feature
        :param y: array-like, shape = [n_samples] target values
        :return: self : object
        '''
        rgen = np.random.RandomState(self.random_state)    # 固定随机数
        self.w_ = rgen.normal(loc=0.0, scale=0.01, size=1 +X.shape[1])    # mean=0，val=0.01 b w[0]
        self.errors_ = []

        for _ in range(self.n_iter):
            errors = 0
            for xi, target in zip(X, y):
                update = self.eta * (target - self.predict(xi))     # eta * (Y - y)
                self.w_[1:] += update * xi                   # w := w + eta * (Y - y)* x
                self.w_[0] += update                        # b := w + eta * (Y - y)
                errors += int(update != 0.0)                 # 每次epochs的Loss
            self.errors_.append(errors)

    def net_input(self, X):
        '''Calculate net input'''
        return np.dot(X, self.w_[1:]) + self.w_[0]     # f = wx+b

    def predict(self, X):
        '''Return class label after unit step'''
        return np.where(self.net_input(X) >= 0.0, 1, -1)    # 阶越函数为输出激活层


'''v1 = np.array([1, 2, 3])
v2 = 0.5 * v1
np.arccos(v1.dot(v2) / (np.linspace.norm(v1) * np.linalg.norm(v2)))
= 0.0
'''

import numpy as np
from activation_function import *
from out_put import *

def init_network():

    network = {}

    network['W1'] = np.array(np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]]))
    network['B1'] = np.array([0.1, 0.2, 0.3])
    network['W2'] = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
    network['B2'] = np.array([0.1, 0.2])
    network['W3'] = np.array([[0.1, 0.3], [0.2, 0.4]])
    network['B3'] = np.array([0.1, 0.2])

    return network


def forward(netwrok, x):
    w1, w2, w3 = netwrok['W1'], netwrok['W2'], netwrok['W3']
    b1, b2, b3 = netwrok['B1'], netwrok['B2'], netwrok['B3']

    a1 = np.dot(x, w1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, w2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, w3) + b3
    y = softmax(a3)

    return y

network = init_network()
x = np.array([1.0, 0.5])
y = forward(network, x)
print(y)

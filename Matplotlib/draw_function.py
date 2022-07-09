from IPython import display
import numpy as np
import math
import matplotlib.pyplot as plt
from time import sleep
plt.subplots()
xMax = 500
x = np.linspace(0, 2*np.pi, xMax)
y= np.sin(x)
plt.plot(x, y, 'b--')
sleep(0.5)
ax, = plt.plot(x, y, 'ro')
i = 0
while i <= xMax:
    plt.pause(0.002)
    y1 = np.sin(x[:i])
    ax.set_xdata(x[:i])
    ax.set_ydata(y1)
    plt.show()
    i += 2
plt.show()

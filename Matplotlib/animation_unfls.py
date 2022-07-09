from IPython import display
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()


def init():
    ax.set_xlim(0, 2*np.pi)
    ax.set_ylim(-1, 1)




def update1(frame):
    ln = plt.plot(frame, np.sin(frame), 'r^')
    return ln


ani = FuncAnimation(fig, update1, frames=np.linspace(0, 2*np.pi, 100),
                    init_func=init, blit=True, interval=100)
plt.show()

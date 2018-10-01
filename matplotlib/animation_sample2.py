import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# fig, ax = plt.subplots()
# xdata, ydata = [], []
# ln, = ax.plot([], [], 'r-', animated=False)
#
# def init():
#     ax.set_xlim(0, 2*np.pi)
#     ax.set_ylim(-1, 1)
#     return ln,
#
# def update(frame):
#     xdata.append(frame)
#     ydata.append(np.sin(frame))
#     ln.set_data(xdata, ydata)
#     return ln,
#
# ani = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 128),
#                     init_func=init, blit=True)
# plt.show()


# fig, ax = plt.subplots()
# xdata, ydata = [], []
# ln, = ax.plot([], [], 'r-', animated=False)
#
#
# def init():
#     ax.set_xlim(0, 2 * np.pi)
#     ax.set_ylim(-1, 1)
#     return ln
#
#
# def update(frame):
#     x = np.random.rand()
#     y = np.random.rand()
#     xdata.append(x)
#     ydata.append(y)
#     ln.set_data(xdata, ydata)
#     return ln,
#
#
# ani = FuncAnimation(fig, update, frames=100,
#                     init_func=init, blit=True)
# plt.show()

fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = ax.plot([], [], 'r*', animated=False)
ln, = ax.plot([], [], 'r-', animated=False)

def init():
    # 设置坐标系范围
    ax.set_xlim(0, 2*np.pi)
    ax.set_ylim(-1, 1)
    return ln,

def update(frame):
    xdata.append(np.random.random())
    ydata.append(np.random.random())
    ln.set_data(xdata, ydata)
    return ln,

ani = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 128),
                    init_func=init, blit=True)
plt.show()
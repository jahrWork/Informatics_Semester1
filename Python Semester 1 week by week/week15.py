# matplotlib library to plot functions


from matplotlib.patches import Rectangle, Circle
import matplotlib.pyplot as plt
from numpy import array, sin, cos, pi, zeros, linspace
from random import random, uniform

# **********************************************
# 1. plot math graphs
# y = f(x) function to plot
# y_i = f(x_i) forall i in [0, N]
# **********************************************
# N = 100


# t = array([2*pi*i/N for i in range(N+1)])
# print("t[N] =", t[N], 2*pi)


# x = 3 * sin(t)  # x_i = 3 sin ( t_i )
# y = 2 * cos(t)


# plt.plot(y, x, "blue")
# plt.show()

# plt.plot(t, x,  "blue")
# plt.plot(t, y,  "green")
# plt.show()


# fig, ax = plt.subplots(1, 1)
# ax.set_aspect("equal")

# N = 300
# t = linspace(0, 4*pi, N)

# x = zeros(N)
# y = zeros(N)


# for i in range(N):

#     if t[i] < 2*pi:
#         a = 1
#         e = 0.8
#     else:
#         a = 1
#         e = 0.0

#     r = a * (1 - e**2) / (1 + e * cos(t[i]))
#     x[i] = e*a + r * cos(t[i])
#     y[i] = r * sin(t[i])


# ax.plot(x, y)
# plt.show()


# ********************************************
# 2. plot ants, persons as points
# ********************************************
# def plot(x, y):

#     plt.plot(x, y, "r.")
#     plt.xlim(0, 1)
#     plt.ylim(0, 1)
#     plt.show()


# N = 100
# x_a = []
# y_a = []

# for i in range(N):
#     x_a += [random()]
#     y_a += [random()]

# plot(x_a, y_a)


# for i in range(len(x_a)):

#     if x_a[i] < 0.3:
#         x_a[i] += 0.3

#     elif y_a[i] < 0.3:
#         y_a[i] += 0.3

# plot(x_a, y_a)


# ********************************************
# 3. animate points
# ********************************************
# def plot(x, y):

#     plt.plot(x, y, "r.")
#     plt.xlim(0, 1)
#     plt.ylim(0, 1)
#     plt.show()


# def initial_position():
#     N = 100
#     x = []
#     y = []

#     for i in range(N):
#         x += [random()]
#         y += [random()]

#     return x, y


# def move_ants(x, y):

#     N = len(x)
#     dt = 0.01

#     for i in range(N):
#         vx, vy = [uniform(-1, 1.), uniform(-1., 1.)]
#         x[i] += dt * vx
#         y[i] += dt * vy

#     return x, y


# x, y = initial_position()

# for i in range(100):
#     x, y = move_ants(x, y)
#     plot(x, y)
#     plt.pause(0.1)
#     plt.show()


# ********************************************
# 4. draw circles, rectangles, ...
# ********************************************


# fig, ax = plt.subplots()

# plt.xlim(0, 10)
# plt.ylim(0, 10)
# ax.set_aspect("equal")

# # add rectangle to plot
# ax.add_patch(Rectangle((1, 1), 2, 6))
# ax.add_patch(Circle((5, 5),  1))

# ax.add_patch(Rectangle((6, 6), 1, 1,
#                        edgecolor='red',
#                        facecolor='blue',
#                        fill=True,
#                        lw=5))


# plt.show()
# =============================================================================


from numpy  import sin, pi, arange 
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
import matplotlib as mpl
mpl.use('webagg')


fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.25)
t = arange(0.0, 1.0, 0.001)
a0,f0  = 5, 3
s = a0 * sin(2*pi*f0*t)
l, = plt.plot(t, s, lw=2, color='red')
plt.axis([0, 1, -10, 10])

axcolor = 'lightgoldenrodyellow'
axfreq = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
axamp = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)

slider_freq = Slider(axfreq, 'Freq', 0.1, 30.0, valinit=f0)
slider_amp = Slider(axamp, 'Amp', 0.1, 10.0, valinit=a0)


def update(val):
    amp = slider_amp.val
    freq = slider_freq.val
    l.set_ydata(amp*sin(2*pi*freq*t))
    fig.canvas.draw_idle()


slider_freq.on_changed(update)
slider_amp.on_changed(update)

resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')


def reset(event):
    sfreq.reset()
    samp.reset()


button.on_clicked(reset)

rax = plt.axes([0.025, 0.5, 0.15, 0.15], facecolor=axcolor)
radio = RadioButtons(rax, ('red', 'blue', 'green'), active=0)


def colorfunc(label):
    l.set_color(label)
    fig.canvas.draw_idle()


radio.on_clicked(colorfunc)

plt.show()

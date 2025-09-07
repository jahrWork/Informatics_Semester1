

import matplotlib.pyplot as plt
from matplotlib.widgets import Slider



def build_gui(graph): 

  def update_A(val):
    A = val
    t, s = graph(A)
    l.set_ydata( s )
    fig.canvas.draw_idle()

  fig, ax = plt.subplots()
  plt.subplots_adjust(left=0.25, bottom=0.25)
  A0 = 5
   
  t, s = graph(A0)
  l, = plt.plot(t, s, lw=2, color='red')
  plt.axis([0, 1, -10, 10])

  axes_A = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor="yellow")
  S_A = Slider(axes_A, 'Amp', 0.1, 10.0, valinit = A0)
  S_A.on_changed(update_A)

  plt.show()

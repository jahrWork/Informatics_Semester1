

import matplotlib.pyplot as plt
from matplotlib.widgets import Slider



def build_screen(graph): 

  def update_A(val):
    A = val
    x, y = graph(A)
    l.set_ydata( y )
    fig.canvas.draw_idle()

  fig, ax = plt.subplots()
  plt.subplots_adjust(left=0.25, bottom=0.25)
  A0 = 5
   
  x, y = graph(A0)
  
  l, = plt.plot(x, y, lw=2, color='red')
  xmin, xmax, ymin, ymax = min(x), max(x), min(y), max(y)
  plt.axis([xmin, xmax, ymin, ymax])

  axes_A = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor="yellow")
  S_A = Slider(axes_A, 'Amp', 0.1, 10.0, valinit = A0)
  S_A.on_changed(update_A)

  plt.axis("equal")
  plt.show()

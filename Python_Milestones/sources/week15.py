# maplotlib library to plot functions 


# y = f(x) function to plot 
# y_i = f(x_i) forall i in [0, N]

import matplotlib.pyplot as plt
from numpy import  array, sin, cos, pi 

N = 100
t = array( [ 2*pi*i/N for i in range(N+1) ] )
print("t[N] =", t[N], 2*pi)


x = 3 * sin(t)
y = 2 * cos(t) 


plt.plot(x, y, "red")
plt.show()

plt.plot( t,x,  "blue")
plt.plot( t,y,  "green")
plt.show()










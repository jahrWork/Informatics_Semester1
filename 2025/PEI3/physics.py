
from numpy import  sin, pi,  arange
import matplotlib.pyplot as plt

def wave(A): 

    x = arange(0.0, 1.0, 0.001)
    f = 10
    y = A * sin( 2*pi*f*x )
    return x, y 



if __name__ == "__main__":
 x, y = wave(A=5) 
 plt.plot(x,y)
 plt.show()
               
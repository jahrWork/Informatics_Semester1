
from numpy import  sin, pi,  arange

def graph(A): 

    x = arange(0.0, 1.0, 0.001)
    f = 10
    y = A * sin( 2*pi*f*x )
    return x, y 

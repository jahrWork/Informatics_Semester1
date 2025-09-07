# Functions 
from numpy import array, pi, sin, norm  
import matplotlib.pyplot as plt


#***************************************************************
# Partition of segment [a, b] in N intervals.
# Determine interior nodes x_i = a + (b-a)/N i from i=0 to i=N
#***************************************************************
def partition(a, b, N): 
  x = array([a + (b-a)/N * i for i in range(0, N+1)])
  return x 

def f(x): 
    return sin(pi*x)

def derivative(f,  x, h=1e-3): 
    return ( f(x+h) - f(x-h) )/(2*h)

x = partition(a=0., b=1., N=20)
y = f(x)
yp = derivative(f, x) 

print(" x =", x)
print( "y = ", y)
plt.plot(x,y)
plt.plot(x,yp)
plt.show()

 

print( "yp = ", yp)


# Functions


# """
#     It determines the first derivative

#     Inputs:
#           f : function f: R -> R
#           x : point to evaluate the derivative

#     Output
#           approximated derivative at x

# """

# def Derivative(f, x):

#     Dx = 1e-6

#     return ( f(x+Dx) - f(x) ) / Dx  # lim h->0 ( f(x+h) - f(x) )/h


# def Derivative2(f, x):

#     Dx = 1e-6

#     return (f(x+Dx) - f(x-Dx)) / (2*Dx)


# # *********************************************************
# #  Determine derivative of h(x) = sqrt(x) at x=0.1
# #  for a given tolerance
# # *********************************************************
# def g(x):

#     return sqrt(x)


# def g1(y):

#     return sin(y)


# x0 = 0.1
# D = Derivative(g, x0)
# De = 1/2 * x0**(-1/2)
# print("Derivative = ",  D, "Error = ", De - D)

# D = Derivative2(g, x0)
# De = 1/2 * x0**(-1/2)
# print("Derivative = ",  D, "Error = ", De - D)


# D = Derivative2(g1, x0)
# De = cos(x0)
# print("Derivative = ",  D, "Error = ", De - D)


# D = Derivative3(g1, x0)
# De = cos(x0)
# print("Derivative = ",  D, "Error = ", De - D)


# def Integral(f, a, b):

#     M = 10000
#     dx = (b-a)/M

#     F = [f(a+dx*i) for i in range(M)]

#     return dx * sum(F)


# def h(x):

#     return sqrt(x)


# # *********************************************************
# #  Determine integral of h(x) = sqrt(x) from a=0 to b=1
# #  for a given tolerance
# # *********************************************************
# a, b = 0., 1.
# I = Integral(h, a, b)
# Ie = 2/3 * (b**(3/2) - a**(3/2))
# print("Integral = ",  I, "Error = ", Ie - I)


# I = Integral(f=h, a=0., b=1.)
# Ie = 2/3
# print("Integral = ",  I, "Error = ", Ie - I)



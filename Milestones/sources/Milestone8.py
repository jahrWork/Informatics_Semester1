from Calculus.Derivative_Integral import Derivative, Integral 
import matplotlib.pyplot as plt
from numpy import pi, sin, cos, linspace, array 


def Integral_and_derivative_examples(): 

   # plot from x=-2 pi to x = +2 pi 
     x = linspace(  -2*pi, 2*pi, 200)    

   # plot sine function       
     plt.plot( x, sin(x) )                                  
     plt.show() 

    # plot piecewise function     
     plt.plot( x, array([ Piecewise_f(xi) for xi in x]) )  
     plt.show()

   # plot derivative of piecewise function  
     plt.plot( x,  array([ Derivative(Piecewise_f, xi) for xi in x]) )  
     plt.show()

   # plot integral of piecewise function 
     plt.plot( x,  array([ Integral(Piecewise_f, 0, xi) for xi in x]) )     
     plt.show()  #end
     


def Piecewise_f(x): 

       if x < -pi/2 : 
           
            return 0 
            
       elif x < pi/2 : 
           
            return cos(x) 
            
       else: 
            return 0 # x > pi/2
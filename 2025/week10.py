
#******************************************************
#   Solve nonlinear equations. Newton scalar  
#******************************************************

def derivative(f, x):

    h = 1e-5  
    return ( f(x+h) - f(x-h) )/(2*h)

def newton(f,x0):

    x, dx, eps = x0, 1., 1e-10

    while abs(dx) > eps: 
        dx = -f(x) / derivative(f, x)
        x = x + dx 
        print("x =", x, "dx =", dx)
    return x  

def f(x): 

    return x**2 -1 

print( "sol =", newton(f, 0.8))  


#**********************************************************
#   Solve nonlinear equations. Newton vectorial f: RN-> RN 
#**********************************************************
from numpy import array, zeros
from numpy.linalg import norm  
from week6 import Gauss 


def Newton(F, x0):  
  """
 ____________________________________________________________________
  Newton solver 
        Inputs: 
                x0   : initial guess and output value 
                F(X) : vector function  
        return: 
                x : solution (F(x)=0)

  Author: Juan A Hernandez (juanantonio.hernandez@upm.es) Oct 2022 
_____________________________________________________________________
  """
  
  x, Dx, iteration, itmax = x0, x0, 0, 1000  
  print("x0 =", x0)
 
  while  norm(Dx) > 1e-8 and iteration <= itmax : 
    
      iteration = iteration + 1 
      Dx = Gauss( Jacobian( F, x0 ), -F(x0)) 
      x[:] = x[:] + Dx  # WARNING x = x + Dx (does not work)
      
      print("x =", x, "iteration =", iteration, "Newton norm(Dx) = ",  norm(Dx) ) 

  return x 

  
def Jacobian( F, x ):  

   Dx = 1e-3     
   Dxi = zeros( len(x) ) # WARNING Dxi = x does not work 
   J = zeros( (len(x), len(x)) )
       
   for i, _ in enumerate(x):

       Dxi[:] = 0
       Dxi[i] = Dx
       J[:,i] =  ( F(x + Dxi) - F(x - Dxi) )/(2*Dx)  
   
   return J    






def f(x): 

    return array( [ x**2 - 1 ] ) 

x0 = array( [ 0.1 ])
print(" solution =", Newton(f, x0 ) )
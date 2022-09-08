 
from Calculus.Taylor_expansions import Taylor 
from math import pi, factorial, exp 
import matplotlib.pyplot as plt
from numpy import pi, sin, cos, linspace, array 
from cmath import   exp  
 
def dkexp(x, k): 
      
      return exp(x) 
   
def Taylor_expansion_examples(): 
    
   def Taylor_cosine(x):
       return Taylor( df = d_cosine, x0 = 0., x = x, N = M ) 
 
   print(" Taylor exp(1.) x0=0   :", Taylor( df = dkexp, x0 = 0., x = 1., N = 1) )
   print(" Taylor exp(1.) x0=0   :", Taylor( df = dkexp, x0 = 0., x = 1., N = 4) )
   print(" Taylor exp(1.) x0=0   :", Taylor( df = dkexp, x0 = 0., x = 1., eps = 1e-7 ) )
     
 # plot from x=0 to x = 2 pi 
   x = linspace( 0, 2*pi, 200)    
   plt.plot( x, cos(x) )
   M = 10 
   plt.plot( x, array([ Taylor_cosine(xi) for xi in x])  )
   plt.show()                  
    
   x = linspace( -0.9, 0.9, 200)  
   plt.plot( x, array([ fractional(xi) for xi in x])  )
   plt.plot( x, array([ Taylor_fractional(xi) for xi in x])  )
   plt.show() 
     
   x = linspace( 0, 2*pi, 200)    
   plt.plot( x, cos(x) )
   for  M in range(12, 18, 1):  
      plt.plot( x, array([ Taylor_cosine(xi) for xi in x])  )
   plt.show()  #end

           
# ***********************************************************************     
# Z = exp( I * x)             = cos(x) + I sin(x) 
# Zk = (I)**k * exp( I * x )  = dk( cos(x) )/dxk + I dk( sin(x) ) /dxk 
# Z'= I * exp( I * x) 
# Zk = (I)**k * exp( I * x )  
# ***********************************************************************    
def d_cosine(x, k):
  
  I = complex(0, 1)

  return  ( I**k * exp( I * x) ).real # cosine 
        
   
def d_fractional(x, k):
            
     # f(x) = 1/ ( 1 - x) 
     # f' = + 1 / ( 1 - x ) **2 
     # fk = k! (1-x)**(-k-1)  
       return factorial(k) * ( 1 - x ) **(-k-1) 
        

def Taylor_fractional(x):
      
      return Taylor( df = d_fractional, x0 = 0., x = x, N = 5 ) 

def fractional(x):
      
       return 1 / ( 1 - x ) 

#function exponential(x) result(h) 
#      real, intent(in) :: x 
#      real :: h 
      
#        h = exp( x) 
        
#end function
  
 

#function dksinh(x, k) result(dk) 
#      real, intent(in) :: x 
#      integer, intent(in) :: k 
#      real :: dk  
      
#      if ( mod(k, 2) == 0 ) then 
#          dk = sinh(x) 
#      else 
#          dk = cosh(x) 
#      end if  
       

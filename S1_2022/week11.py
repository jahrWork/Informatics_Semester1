from math import sqrt, exp, factorial 
# Functions 


def Derivative( f, x ): 
 
    h = 1e-5 
    
    return ( f(x+h) - f(x) ) / h  # lim h->0 ( f(x+h) - f(x) )/h 
   

def Integral( f, a, b ):
 
    dx = 1e-3 
    M =  int( abs(b-a)/dx ) 
    dx = (b-a)/M 
         
    F = [ f(a+dx*k) for k in range(M) ]
    return   dx * sum(F) 



#*********************************************************
# 1. Determine integral of h(x) = sqrt(x) from a=0 to b=1  
#    for a given tolerance 
#*********************************************************
def h(x): 
     return sqrt(x)
 
a, b = 0., 1.     
I =  Integral(h, a, b) 
Ie = 2/3 * ( b**(3/2) - a**(3/2) )
print( "Integral = ",  I, "Error = ", Ie - I )

#*********************************************************
# 2. Determine derivative of h(x) = sqrt(x) at x=0.1  
#    for a given tolerance 
#*********************************************************

x0 = 0.1     
D =  Derivative(h, x0) 
De = 1/2 *  x0**(-1/2) 
print( "Derivative = ",  D, "Error = ", De - D)








def Taylor( df, x0, x, N): 
   """" 
       Taylor expansion =  sum _{k=0} ^N f_k(x0) (x-x0)**k / k! 
           Inputs:
              df   : function kth derivative of f(x) 
              x0   : origin of Taylor expansion 
               x   : point where Taylor is evaluated 
               N   : last term of Taylor expansion 
                
   """
      
   def a(k): 
     return  df(x0, k) * ( x - x0 )**k / factorial(k)  

   return Sigma( a, 0, N) 



def Sigma(a, i0, N):
    """S = sum form i=1 to N ( a_i ) """
           
    return sum( [ a(i) for i in range(i0, N+1) ]  )


#************************************************************************
# 4. Taylor expansion of exp(x) origen x0=0 at x =1 with tolerance eps
#************************************************************************
def dkexp(x, k): 
      
      return exp(x) 


N = [ 1, 4, 8, 16]
for n in N: 
   T =  Taylor( df = dkexp, x0 = 0., x = 1., N = n) 
   E =  exp(1.) -T 
   print( "Taylor exp(1.) x0=0   :", T, "Error =", E)

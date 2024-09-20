from numpy import sum, array 

def Derivative( f, x ): 
 
    h = 1e-5 
    
    return ( f(x+h) - f(x) ) / h  # lim h->0 ( f(x+h) - f(x) )/h 
   

def Integral( f, a, b ):
 
    dx = 1e-3 
    M =  int( abs(b-a)/dx ) 
    dx = (b-a)/M 
         
    F = array( [ f(a+dx*k) for k in range(M) ] ) 
    return   dx * sum(F) 


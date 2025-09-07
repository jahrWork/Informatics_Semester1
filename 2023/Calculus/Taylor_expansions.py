    
    
from Calculus.Series import  Sigma, Sigma_N
from math import  factorial

 
def Taylor( df, x0, x, eps = None, N = None):  
    
    if N is None: 
        return Taylor_e(df, x0, x, eps)

    elif eps is None: 
        return Taylor_N(df, x0, x, N)

    else: 
        print("Error Taylor")
        exit() 


  
#******************************************************************** 
#   Taylor expansion =  sum _{k=0} ^{infinity} f_k(x0) (x-x0)**k / k! 
#       Inputs:
#          df   : kth derivative of f(x) 
#          x0   : origin of Taylor expansion 
#           x   : point where Taylor is evaluated 
#           eps : error of Taylor approximation
#********************************************************************
def Taylor_e( df, x0, x, eps):   
      
    def a(k): 
      return df(x0, k) * ( x - x0 )**k / factorial(k)  

    return Sigma( a, 0, eps) 
    

#******************************************************************** 
#   Taylor expansion =  sum _{k=0} ^N f_k(x0) (x-x0)**k / k! 
#       Inputs:
#          df   : kth derivative of f(x) 
#          x0   : origin of Taylor expansion 
#           x   : point where Taylor is evaluated 
#           N   : last term of Taylor expansion 
#********************************************************************
def Taylor_N( df, x0, x, N):   
      
   def a(k): 
     return  df(x0, k) * ( x - x0 )**k / factorial(k)  

   return Sigma_N( a, 0, N) 
    
  

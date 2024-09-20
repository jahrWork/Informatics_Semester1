
from numpy import sum, array  
 
#--------------------------------------
# S = sum from i=i0 to infinity ( a_i ) 
# The error should be < eps
#--------------------------------------
def Sigma(a, i0, eps): 
      
     N = Tail(a, eps) 
     
     return Sigma_N(a, i0, N)
  


#--------------------------------------
# S = sum form i=1 to N ( a_i ) 
#--------------------------------------
def Sigma_N(a, i0, N):
           
    return sum( array( [ a(i) for i in range(i0, N+1) ] ) )



#--------------------------------------
# It calculates the number of terms N
# which gives rise to an error < eps
#--------------------------------------
def Tail(a, eps):  
   

    Nmax = 200000000 
    
  # Obtain N such as:
  # integral from i=N+1 to infinity a_i = eps 
    i = 1 
    while ( abs( a(i) + a(i+1) )  > 2*eps  and i < Nmax ): 
        
        i = i + 1
        
   
    return  i 
   


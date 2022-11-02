# Functions 
from numpy import array 




#***********************************************
# 0. ExampleS f: R -> R, f: R2 -> R, f: R2 -> R2  
#***********************************************
def f(x): 
    
    return x**2 

print( " f(2.) =", f(2.) )

def f(x, y): 
    
    return x**2 + y**2 

print( " f(2., 2.) =", f(2, 2.) )

def f(x): 
    
    return array( [ x[1],  -x[0] ] )

print( " f( array( [1, 2]) =", f( array( [1, 2] ) ) )





# #***********************************************
# # 1. Determine a list of the first N primes 
# #***********************************************
# def is_prime(n): 
    
#       for i in range(2,n):
#           if n % i == 0:  
#             return False
         
#       return True and n > 1   
   
    
   
# def First_primes(N): 

#   N_primes = 0 
#   n = 1   
#   primes = []
  
#   while N_primes < N: 
             
#        if is_prime(n): 
#            primes += [ n ]
#            N_primes = N_primes + 1 
            
#        n = n + 1    
   
#   return primes   
   
    
   
# print("First N primes =", First_primes(7) )     


          
      

# #***********************************************
# # 2. Determine a list of the first N perfects 
# #***********************************************   
# def is_perfect(n): 
    
#       S = 0 
#       for i in range(1,n):
#           if n % i == 0:
#             S = S + i   
          
#       return S == n  
   
# def First_perfect_numbers(N): 

#   N_perfects = 0 
#   n = 1 
#   perfects = [ ]   
  
#   while N_perfects < N: 
             
#         if is_perfect(n): 
#             perfects += [ n ]
#             N_perfects = N_perfects + 1 
            
#         n = n + 1 
#         # print("n =", n)
#         # input()
   
#   return perfects      
      

# print("First N perfect numbers =", First_perfect_numbers(4)  )   




 
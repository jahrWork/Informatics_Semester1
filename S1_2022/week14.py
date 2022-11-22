# Additional examples 
from math import cos, factorial, exp, pi, sqrt  



#***********************************************************
# Relative position to any R3 sphere of center and radius R 
#***********************************************************
# def relative_position(x, y, R): 
    
#      d = (x[0]-y[0])**2 + (x[1]-y[1])**2 + (x[2]-y[2])**2
     
#      return  d < R**2


# print("Relative pos =", relative_position( x = (2,1,3), y=(0,0,0), R=1) ) 



# #***************************************************
# # Implement Gaussian function
# #***************************************************
# def gaussian(x,  m = 0, s = 1): 
    
#       return exp( - ((x-m)/s)**2 / 2 ) / sqrt( 2 * pi * s)


# def partition(a, b, N): 
    
#     return [ a+ (b-a)*i/N for i in range(N+1) ]


# m = 0; s = 1 
# x = partition( a = m -5*s, b = m + 5*s, N = 5)

# y = []
# for xi in x: 
#     y += [ gaussian(xi) ]

# print("Gaussian =", y)



# #***************************************************
# # Implement Taylor cosine expansion 
# #***************************************************
# def Taylor_cosine(x, tol): 
    
#     T = 0; n = 0 
    
#     while abs( cos(x)-T) >= tol:
#         T += (-1)**n * x**(2*n) / factorial(2*n)
#         n += 1 
  
#     return T 

# print("Taylor(1, 1e-3) =", Taylor_cosine(x = 1, tol = 1e-3), "cos(1) =", cos(1.))





#***************************************************
# Implement Collatz function of natural number N 
#    a_{i+1} = f((a_i))
#    f(n) = n/2 if n is even or 3n+1 if n is odd
#    stop when a_i is 1. 
#***************************************************
def f(n): 
    
    if n % 2 == 0: 
          return n//2 
     
    else:
          return 3*n + 1
     
def collatz(N): 
    
    a = [ N ]
 
    i = 0 
    while a[i] != 1:  
        a += [ f( a[i] ) ]
        i += 1 
        
    return a 


print("Collatz(7) =", collatz(7) )






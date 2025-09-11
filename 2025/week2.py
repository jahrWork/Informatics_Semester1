#************************************************************
# loops: for and while 
# functions: def, return versus procedures 
#************************************************************

#**************************************************************
# Determine if n is prime.
#  n is prime if i has only two divisors:  1 and itself. 
#**************************************************************

#  for loop is used we perform a spacific number of operations
print("prime numbers")
n = 13
for i in range(2,n): # from i=2 to n-1 
    if n % i == 0:
          break

if i<n-1:
        print(n, "is not prime")
else:
        print(n, "is prime")





# while loop is used when we don't know th number of operations or steps 
N = 10
print("Determine N=", N, "first primes")

S_prime = 0
N_prime = 0
n = 2
while N_prime < N:

    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            # print( n, " is not prime because ", i, "is a factor")
            is_prime = False
            break

    if is_prime:
        print(n, "is prime")
        N_prime = N_prime + 1
        S_prime = S_prime + n

    else:
        print(n, "is not prime")
        pass

    n = n + 1

print("\n \n")
print("The sum of the first N primes is =", S_prime)

#**********************************************************************
# A number is perfect when the sum of its primes is equal to the number 
#**********************************************************************
print("perfect numbers") 
n = 6
S = 0
for i in range(1,n):
    if n % i == 0:
          print( i, "is a factor")
          S = S + i

if S==n:
        print(n, "is perfect")
else:
        print(n, "is not perfect")






#***************************************************
#  Functions 
#***************************************************


#***********************************************
#  function:  Roots of a second order equation 
#    inputs: a, b, c 
#    outputs: roots 
#*********************************************** 
  
from cmath import sqrt

def roots_2nd_order_equation(a, b, c): 

    if a == 0:
       if b == 0:
         return None 
       else:
        x_1 = -c/b
        return [x_1]
       
    else:

     x_1 = (-b + sqrt(b**2 - 4*a*c)) / (2*a)
     x_2 = (-b - sqrt(b**2 - 4*a*c)) / (2*a)
     return [x_1, x_2] 
     
# ****************************************
# procedure to print different roots 
# ****************************************     
def pretty_print(roots): 

    if roots == None: 
        print("There is no solution ")

    elif len(roots) == 1:     
          x_1 = roots[0] 
          print("There is only one solution = ", x_1)
    else: 
          [x_1, x_2] = roots   
          print("There are two solutions")
          print("x_1 = ", x_1)
          print("x_2 = ", x_2)


roots =  roots_2nd_order_equation(a=0, b=0, c=3)
pretty_print( roots )

roots =  roots_2nd_order_equation(a=0, b=1, c=1)
pretty_print( roots ) 

roots =  roots_2nd_order_equation(a=1, b=-4, c=1)
pretty_print( roots ) 







#*************************************************
# Paradigms: imperative versus declarative 
#*************************************************

# Imperative program (sequence of steps, how to )
n = 6
def factorial_imperative(n): 
   f = 1
   for i in range(1, n+1):
       f = f * i
       print("factorial =", f)
   return f 
print( "\nfactorial(6) = ", factorial_imperative(n))
    

# Declarative program (what to do)
def factorial(n): 
   if n==0: 
        return 1 
   else: 
       return n * factorial(n-1)
   
print( "\nfactorial(6) = ", factorial(n))





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
             
#         if is_prime(n): 
#             primes += [ n ]
#             N_primes += 1 
            
#         n += 1    
   
#   return primes   
   
    
   
# print("First N primes =", First_primes(7) )     


          
      

# #***********************************************
# # 2. Determine a list of the first N perfects 
# # is_perfect: N -> (T,F)
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
   
#   return perfects      
      

# print("First N perfect numbers =", First_perfect_numbers(4)  )   



# Functions 
#from numpy import array, pi, sin,  cos  

# import matplotlib.pyplot as plt

#*************************************************
# Never do the following: 
# f(x) is NOT a function 
# because depends on variable a which is an 
# external variable 
#*************************************************

# a = 3 
# def f(x): 
#    return x**2 + a 

# print(" f(2) =", f(2))
# a = 4 
# print( " f(2) =", f(2) )

#***********************************************************
# Type of arguments can be specified to improve readability 
# However, type of actual arguments are not checked 
#***********************************************************
# def f(x: float) -> float:  
#    return x**2 

# print(" f(2) =", f(2))
# print( " f(2.) =", f(2.) )




#***********************************************
#  ExampleS f: R -> R, f: R2 -> R, f: R2 -> R2  
#***********************************************
# def f1(x): 
    
#     return x**2 

# def f2(x, y): 
    
#     return x**2 + y**2 


# def f3(x): 
    
#     return array( [ x[1],  -x[0] ] )


# print( " f(2.) =", f1( 2. ) )
# print( " f(2.) =", f1( x = 2. ) )
# print( " f(2., 2.) =", f2(x  = 2, y = 2.) )
# print( " f( array( [1, 2]) =", f3( x = array([1, 2]) ) )











#***********************************************************************
# Relative position betwen x and a  RN sphere of center c and radius R 
#***********************************************************************
# def relative_position(x, c, R): 
    
#       d = norm(x-c) 
     
#       return  d < R


# print("Relative pos =", relative_position( x = (2,1,3), c=(0,0,0), R=1) ) 



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





#*****************************************
# Functions
#****************************************
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




# #***********************************************
# #  Polynomial evaluation  
# #***********************************************  
# def polynomial(x, a): 

#     P = 0 
#     for i in range(len(a)): 
#         P  += a[i] * x**i 

#     return P 

 
# print(" polynomial = ", polynomial( x=2, a=[1, 2, 3] ) ) 


# def f(x): 
    
#     if x <= 0: 
#         return cos( pi*x) 
#     else: 
#         return 1 + sin( pi*x) 
    

# from math import sqrt, exp, factorial, sin, cos


# # #***************************************************
# # # Implement Taylor cosine expansion 
# # #***************************************************
# def Taylor_cosine(x, tol): 
    
#     T = 0; n = 0 
    
#     while abs( cos(x)-T) >= tol:
#         T += (-1)**n * x**(2*n) / factorial(2*n)
#         n += 1 
  
#     return T 

# print("Taylor(1, 1e-3) =", Taylor_cosine(x = 1, tol = 1e-3), "cos(1) =", cos(1.))




# # #***************************************************
# # # Implement Taylor expansions 
# # #***************************************************
# def Taylor(df, x0, x, N):
#     """"
#         Taylor expansion =  sum _{k=0} ^N f_k(x0) (x-x0)**k / k!
#             Inputs:
#               df   : function kth derivative of f(x)
#               x0   : origin of Taylor expansion
#                 x   : point where Taylor is evaluated
#                 N   : last term of Taylor expansion

#             return:
#                 Taylor expansion evaluated at x
#     """

#     def b(k):

#         return df(x0, k) * (x - x0)**k / factorial(k)

#     return sum([b(k) for k in range(N+1)])


# # ************************************************************************
# # 4. Taylor expansion of exp(x) origen x0=0 at x =1 with tolerance eps
# # ************************************************************************
# def dexp(x, k):

#     return exp(x)


# # T = Taylor(df=dexp, x0=0., x=1., N=12)
# # print(" T = ", T, " E =", exp(1.) - T)

# N = [1, 2, 3, 4, 5, 6, 7, 8, 16]
# for n in N:
#     T = Taylor(df=dexp, x0=0., x=1., N=n)
#     E = exp(1.) - T
#     print("N=", n, "Taylor exp(1.) x0=0   :", T, "Error =", E)

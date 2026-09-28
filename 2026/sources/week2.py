#************************************************************
# loops: for and while 
# functions: def, return versus procedures 
#************************************************************
# Three ways to use for loop 
# S = "Hello"
# for i in range(len(S)):
#     print("character of S =", S[i] )

# for c in S:
#     print("character of S =", c )

# for i,c  in enumerate(S):
#     print("index i in string S =", i, " S[i] = ", S[i], " character in S = ", c )

#******************************************************************
# Output: print 
#******************************************************************
# Every time print is executed a new line is used
# To avoid new line, use the argument end =', ' 
# This allows to print multiples values separeted by comma: ", "
# for i in range(4): 
#     print( "index :", i)

# for i in range(4): 
#     print( "index :", i, end = ', ')

# print("\nindex :", end =" ")   
# for i in range(4): 
#     print(i, end = ", ")    


# # ouput: 0, 1, 1
# # Once the loop is abandoned, the index retains the last value 
# print("\n\nlast value when loop is abandoned")
# for i in range(2):
#     print(i, end=', ')
# print(i)



# **********************************************************************
#   Roots of a second order equation 
#***********************************************************************

# 1. specification:  obtain roots of secnd order equation
# 2. math model : a x**2 + b x + c = 0, if a==0 equation is b x + c = 0
# 3. algorithm: x_1 = ( -b + .... ) if a == 0 x_1 = - c / b
# 4. code:
# 5. run:
# 6. validation:
#               test1: x**2 -x = 0 , x_1 = 0, x_2 = 1
#               test2: 2 x**2 + 2  = 0, x_1 = + i, x_2 = - i
#               test3: x+1 = 0, x_1 = -1

#***************************************************
#  Functions 
#***************************************************


#***********************************************
#  function:  Roots of a second order equation 
#    inputs: a, b, c 
#    outputs: roots 
#*********************************************** 
  
# from cmath import sqrt

# def roots_2nd_order_equation(a, b, c): 

#     if a == 0:
#        if b == 0:
#          return None 
#        else:
#         x_1 = -c/b
#         return [x_1]
       
#     else:

#      x_1 = (-b + sqrt(b**2 - 4*a*c)) / (2*a)
#      x_2 = (-b - sqrt(b**2 - 4*a*c)) / (2*a)
#      return [x_1, x_2] 



#*************************************************
# Paradigms: imperative versus declarative 
#*************************************************

# Imperative program (sequence of steps, how to )

# def factorial_imperative(n: int) -> int: 

#    f = 1
#    for i in range(1, n+1):
#        f = f * i
#        print("factorial =", f)
#    return f 

# print( "\nfactorial(6) = ", factorial_imperative(n = 6))
    

# # Declarative program (what to do)
# def factorial(n: int) -> int: 

#    if n==0: 
#         return 1 
#    else: 
#        return n * factorial(n-1)
   
# print( "\nfactorial(6) = ", factorial(n=6))


# from math import prod 

# def factorial(n: int) -> int:

#     if n == 0: 
#         return 1
    
#     elif n>0: 
#         return prod( [ i for i in range(1, n+1) ] ) 

#     else: 
#         return("Factorial of a negative number is not defined")

# #print(factorial(-5))  # Output: Factorial of a negative number is not defined
# print(factorial(6))   # Output: 120





#***********************************************
# 1. Determine a list of the first N primes 
#***********************************************
def is_prime(n): 
    
      for i in range(2,n):
          if n % i == 0:  
            return False
         
      return True and n > 1

# # imperative version               
# def First_primes(N: int) -> list: 

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


# Step by step implementation of the first N primes using itertools
# from itertools import count, islice
# from typing import Any


# N = 10

# n=0,1,2,3,..... infinite sequence of integers
# for i in count(2):
#    if i < N :
#       print("i =", i)
#    else:
#       break

# L = [1,2,3,4,5]
# print("L =", L)
# L_primes = list( filter(is_prime, L) )
# print("L_primes =", L_primes)

# L_2primes = list( islice( filter(is_prime, L), 2  ) )
# print("L_2primes =", L_2primes)

# # declarative version using itertools
# def First_primes(N: int) -> list: 
 
#  return list( islice( filter(is_prime, count(2)), N) )

   
# print("First N primes =", First_primes(2) )    

# def sum_first_primes(N: int) -> int:
    
#     return sum(  islice( filter(is_prime, count(2)), N) )

# print("Sum of first N primes =", sum_first_primes(2) ) 

# # math iteration a[n+1] = f( a[n] ), n=0,1,2,... 
# # to obtain a sequence of the first N primes

# def next_prime(n: int) -> int:
    
#     for i in count(n+1):
#         if is_prime(i):
#             return i

# def sum_first_primes(N: int) -> int: 
    
#     a = [2] * N

#     for i in range(0, N-1):
#         a[i+1] = next_prime( a[i] )

#     return sum(a)




# #***********************************************
# #  Determine a list of the first N perfects 
# #***********************************************
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






#**********************************************************************
# A number is perfect when the sum of its primes is equal to the number 
#**********************************************************************
# print("perfect numbers") 
# n = 6
# S = 0
# for i in range(1,n):
#     if n % i == 0:
#           print( i, "is a factor")
#           S = S + i

# if S==n:
#         print(n, "is perfect")
# else:
#         print(n, "is not perfect")







     
# ****************************************
# procedure to print different roots 
# ****************************************     
# def pretty_print(roots): 

#     if roots == None: 
#         print("There is no solution ")

#     elif len(roots) == 1:     
#           x_1 = roots[0] 
#           print("There is only one solution = ", x_1)
#     else: 
#           [x_1, x_2] = roots   
#           print("There are two solutions")
#           print("x_1 = ", x_1)
#           print("x_2 = ", x_2)


# roots =  roots_2nd_order_equation(a=0, b=0, c=3)
# pretty_print( roots )

# roots =  roots_2nd_order_equation(a=0, b=1, c=1)
# pretty_print( roots ) 

# roots =  roots_2nd_order_equation(a=1, b=-4, c=1)
# pretty_print( roots ) 








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
# def f(x: int) -> int:  
#    return x**2 

# print(" f(2) =", f(2))
# print( " f(2.) =", f(2.) )




#***********************************************
#  ExampleS f: R -> R, f: R2 -> R, f: R2 -> R2  
#***********************************************
# from numpy import ndarray, array

# def f1(x: float) -> float: 
    
#     return x**2 

# def f2(x: ndarray) -> float: 
    
#     return x[0]**2 + x[1]**2 


# def f3(x: ndarray) -> ndarray: 
    
#     return array( [ x[1],  -x[0] ] )


# print( " f(2.) =", f1( 2. ) )
# print( " f(2.) =", f1( x = 2. ) )
# print( " f([2., 2.]) =", f2(x  = array([2, 2.]) ) )
# print( " f( array( [1, 2]) =", f3( x = array([1, 2]) ) )



# from numpy import pi, cos 

# def Piecewise_function(x:float) -> float: 

#        if x <= -pi/2 : 
           
#             return 1 
            
#        elif x <= pi/2. : 
           
#             return cos(x) 
            
#        else: 
#             return -2 # x > pi/2

# print(Piecewise_function(-pi/2.), Piecewise_function(pi/2.),   Piecewise_function(pi/2.+1e-5) )


# lambda functions or anonymous functions 
# f = lambda x : x**2 
# print( "f(x=2) =", f(2)) 

# # equivalent to 
# def f(x:float) -> float: 
#       return x**2 
# print( "f(x=2) =", f(2)) 



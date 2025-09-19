#***************************************************
#   Assignemts and control flow 
#***************************************************


# two different ways of importing math functions 
from math import exp, sin, log10, cos, sqrt, fabs
import math

# print("Hello world")

# m = 3
# print("The value of m is: ", m)
# print("The type of m is: ", type(m))

# name =  " Juan"
# print("The value of name is: ", name)
# print("The type of name is: ", type(name))

# x = 1.
# print("The value of x is: ", x)
# print("The type of x is: ", type(x))
# print( "Expression at x=1 is:", ( 3 * x**3 + 5 * x - 1 ) / ( math.exp(x) + 3 * math.sin(x) - math.log10(x) ) )

# x = 1.
# print( "Expression at x=3 is:", ( 3 * x**3 + 5 * x - 1 ) /( exp(x) + 3 * sin(x) - log10(x) ) )

# x = -3.5
# print("Expression:", (3 * x**3 + 1) / ( cos(x**2) + 5 * log10(  sqrt(fabs(x) ) ) ) )
# print("Expression:", (3 * x**3 + 1) / (math.cos(x**2) + 5 * math.log10(  math.sqrt(math.fabs(x)  )) )) # verbose expression 




# PEI1 = 2.1
# PEI2 = 9.9
# PEI3 = 10.
# MOODLE = 10.
# print("\n \nCalcula la media con las siguientes notas", PEI1, PEI2, PEI3, MOODLE )

# if PEI1 >=3 and PEI2 >=3 and PEI3 >=3:

#     MEDIA = 0.3 * PEI1 + 0.3 * PEI2 + 0.3 * PEI3  + 0.1 * MOODLE
#     print("MEDIA :", MEDIA)

# else:
#     print("No se calcula la media. \nNo se alcanza el mínimo exigido en cada una de las partes.")
#     print("Nos vemos en el final.")




# from cmath import sqrt

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
# a = 1.
# b = 1.
# c = 1.

# if a == 0:
#     if b == 0:
#         print("There is no solution ")
#     else:
#         print(" There is only one solution = ", -c/b)
# else:

#     x_1 = (-b + sqrt(b**2 - 4*a*c)) / (2*a)
#     x_2 = (-b - sqrt(b**2 - 4*a*c)) / (2*a)
#     print("There are two solutions")
#     print("x_1 = ", x_1)
#     print("x_2 = ", x_2)

# print("max =", max(abs(x_1), abs(x_2)))



#****************************************************
# Strings and functions 
#****************************************************

#S = "my name is John"
# print( S.split(" ") )

# for c in S: 
#     print("c = ", c)
   
# print("\nString referred by index")    
# for i in range(len(S)): 
#     print("c = ", S[i])
    

# print( " S[0] =",  S[0] ) 
# #S[0] = "M"
# S = "M" + S[1:]
# print(S)

# S = S.upper()  
# print(S)


# s = 'abcd'[0:2]
# print(s)

# s = "abc"
# s2 = s[-1:-len(s)-1:-1]
# print(s2)

# s3 = s[-1:0:-1]
# print("s3 =", s3)
# print("abcd"[:2])






#***********************************************************
# types and operators 
#***********************************************************
# print(7/2)
# print(7./2.)

# print( (3+2j)*(-1j))


# print(2**3**2)
# print( 2**(3**2) )
# print( (2**3)**2 )
# print( 8**3.2 )

# print(13.2/4)
# print(13.2%4)

# print( type(divmod(5,2)))


# print(13.2//4.)
# print(divmod(13.2,4))
# z = 1+ 1j 
# print(z.real, z.imag)

# #from math import floor 
# from numpy import floor, round, ceil 
# #from math import floor, ceil


# print(round(7.8), type(round(7.8)))
# print(int(7.8))
# print(round(7.8, 0))
# print( type(floor(7.8)) )

# for i in range(4): 
#     print( "numero :", num)

# print(4*f"num : {num} \n")

# print(4*f'num : {num}', end = '\n')


# print(4*'num', num, end = '\n')

# ouput: 0, 1, 1
# Once the loop is abandoned, the index retains the last value 
# for i in range(2):
#     print(i, end=', ')
# print(i)


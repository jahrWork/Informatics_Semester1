#***************************************************
#   Assignemts and control flow 
#***************************************************


# two different ways of importing math functions 
from math import exp, sin, log10, cos, sqrt, fabs
import math

print("Hello world")

m = 3
print("The value of m is: ", m)
print("The type of m is: ", type(m))

name =  " Juan"
print("The value of name is: ", name)
print("The type of name is: ", type(name))

x = 1.
print("The value of x is: ", x)
print("The type of x is: ", type(x))
print( "Expression at x=1 is:", ( 3 * x**3 + 5 * x - 1 ) / ( math.exp(x) + 3 * math.sin(x) - math.log10(x) ) )

x = 1.
print( "Expression at x=3 is:", ( 3 * x**3 + 5 * x - 1 ) /( exp(x) + 3 * sin(x) - log10(x) ) )

x = -3.5
print("Expression:", (3 * x**3 + 1) / ( cos(x**2) + 5 * log10(  sqrt(fabs(x) ) ) ) )
print("Expression:", (3 * x**3 + 1) / (math.cos(x**2) + 5 * math.log10(  math.sqrt(math.fabs(x)  )) )) # verbose expression 




PEI1 = 2.1
PEI2 = 9.9
PEI3 = 10.
MOODLE = 10.
print("\n \nCalcula la media con las siguientes notas", PEI1, PEI2, PEI3, MOODLE )

if PEI1 >=3 and PEI2 >=3 and PEI3 >=3:

    MEDIA = 0.3 * PEI1 + 0.3 * PEI2 + 0.3 * PEI3  + 0.1 * MOODLE
    print("MEDIA :", MEDIA)

else:
    print("No se calcula la media. \nNo se alcanza el mínimo exigido en cada una de las partes.")
    print("Nos vemos en el final.")




from cmath import sqrt

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
a = 1.
b = 1.
c = 1.

if a == 0:
    if b == 0:
        print("There is no solution ")
    else:
        print(" There is only one solution = ", -c/b)
else:

    x_1 = (-b + sqrt(b**2 - 4*a*c)) / (2*a)
    x_2 = (-b - sqrt(b**2 - 4*a*c)) / (2*a)
    print("There are two solutions")
    print("x_1 = ", x_1)
    print("x_2 = ", x_2)

print("max =", max(abs(x_1), abs(x_2)))


#***********************************************
# Roots   
#***********************************************  
def roots(a, b, c): 
    if a == 0:
     if b == 0:
        print("There is no solution ")
     else:
        print(" There is only one solution = ", -c/b)
    else:

     x_1 = (-b + sqrt(b**2 - 4*a*c)) / (2*a)
     x_2 = (-b - sqrt(b**2 - 4*a*c)) / (2*a)
     print("There are two solutions")
     print("x_1 = ", x_1)
     print("x_2 = ", x_2)


print( "roots =", roots(1,2,3))
print( "roots =", roots(1,-2,1))
print( "roots =", roots(1,-4,1))
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
# print("\n \nCalcula la media con las siguientes notas", PEI1, PEI2)

# if PEI1 >=3 and PEI2 >=3 :

#     MEDIA = 0.5 * PEI1 + 0.5 * PEI2
#     print("MEDIA :", MEDIA)

# else:
#     print("No se calcula la media. \nNo se alcanza el mínimo exigido en cada una de las partes.")
#     print("Nos vemos en el final.")




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




# # format f in print 
# for i in range(4): 
#   print(f"index : {i}")

# # Tables with print 
# # variable:<length (specify the length of the column 
# # string format: 15s fifteen characters
# # float format: 15.2f fifteen digits with two decimals 
# # :< left justified, :>right justified 
# print("\nPretty print table ")
# print(45*"-")
# print(f"{"x":<15s}{"x**2":<15s}{"x**3":<15s}")
# print(45*"-")
# for i in range(1, 5):
#  x = 2*i + 1.
#  print(f'{x:<15.2f}{x**2:<15.2f}{x**3:<15.2f}')

# print(45*"-")
# print(f"{"x":>15s}{"x**2":>15s}{"x**3":>15s}")
# print(45*"-")
# for i in range(1, 5):
#  x = 2*i + 1.
#  print(f'{x:>15.2f}{x**2:>15.2f}{x**3:>15.2f}')

#******************************************************************
# Operators: +, -, *, /, **, //, %, abs, round, divmod
#******************************************************************
print(" 8/3 =", 8/3)
print(" 8//3 =", 8//3) # floor division
print(" 8%3 =", 8%3)   # modulus
print(" divmod(8,3) =", divmod(8,3)) # returns a tuple with the quotient and the remainder

print(" 2*'Juan' =", 2*'Juan') # string repetition
print (" 'Juan' + 'Hernandez' =", 'Juan' + 'Hernandez') # string concatenation
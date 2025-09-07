from cmath import sqrt


# 1. specification:  Obtener las raices de una ecuacion de segundo grado
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


# #***********************************************
# # Roots   
# #***********************************************  
# def roots(a, b, c): 
    # if a == 0:
    #  if b == 0:
    #     print("There is no solution ")
    #  else:
    #     print(" There is only one solution = ", -c/b)
    # else:

    #  x_1 = (-b + sqrt(b**2 - 4*a*c)) / (2*a)
    #  x_2 = (-b - sqrt(b**2 - 4*a*c)) / (2*a)
    #  print("There are two solutions")
    #  print("x_1 = ", x_1)
    #  print("x_2 = ", x_2)


# print( "roots =", roots(1,2,3))
# print( "roots =", roots(1,-2,1))
# print( "roots =", roots(1,-4,1))
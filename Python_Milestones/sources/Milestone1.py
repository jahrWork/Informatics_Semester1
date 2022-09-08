from math import exp, log, sin 

def Hello_world(): 

    print('Hello World')

    # integer numeric type 
    x = 1 
    print( "\n x =", x, " and its type is : ", type(x) )

    # real numeric type 
    x = 1. 
    print( "\n x =", x, " and its type is : ", type(x) )

    # complex numeric type 
    x = 1. + 1.j
    print( "\n x =", x, " and its type is : ", type(x) )

    # boolean type 
    x = True
    print( "\n x =", x, " and its type is : ", type(x) )

    # String type 
    x = "My name is John"
    print( "\n x =", x, " and its type is : ", type(x) )

    # to impose PEIi >= 3 if conditions are needed. 
    # we will see these logical if condtions in next milestones.
    PEI1 = 9.8 
    PEI2 = 7.5 
    PEI3 = 10.
    N = 0.3 * PEI1 + 0.3 * PEI2 + 0.4 * PEI3 
    print("\n My grade is = ", N)

    x = 1 
    expression = ( 3 * x**3 + 5 * x -1 )/( exp(x) + 3 * sin(x) - log(x) ) 
    print( "\n expression with x=1 : ", expression)

    x = 2 
    expression = ( 3 * x**3 + 5 * x -1 )/( exp(x) + 3 * sin(x) - log(x) ) 
    print( " expression with x=1 : ", expression)

    exit()
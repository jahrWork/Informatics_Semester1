# Functions 
#from numpy import array, pi, sin,  cos  

# import matplotlib.pyplot as plt

#*************************************************
# Never do the following 
# f(x) is NOT a function 
# because depends on variable a which is an 
# external variable 
#*************************************************

# a = 3 
# def f(x): 
#    return x**2 +a 

# print(" f(2) =", f(2))
# a = 4 
# print( " f(2) =", f(2) )

#***********************************************************
# Type of arguments can be specified to improve readability 
# However, type of actual arguments are not checked 
#***********************************************************
def f(x: float) -> float:  
   return x**2 

print(" f(2) =", f(2))
print( " f(2.) =", f(2.) )




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






#*****************************************************************
# Solve linear system of equations by means of iterative methods. 
# Jacobi y Gauss-Seidel 
#*****************************************************************
from numpy import array, zeros, diag, diagflat, dot
from numpy.linalg import norm 

from scipy.linalg import solve 
from scipy.optimize import bisect, newton

from week6 import Gauss 



# ************************************************************************
# The Jacobi method is an iterative algorithm based on splitting A into: 
#    A = D + L + U  (digonal+lower+upper)
#    To solve A x = b, iterate with 
# 
#      x(n+1) = D**(-1) ( b- (L + U ) x(n) ) 
#*************************************************************************
def Jacobi(A,b): 

    N = len(b)
    x, D, R = zeros(N), zeros(N), zeros((N,N))
    xn = 1 + x 
    tolerance = 1e-10
    k, max_iter = 0, 100

  # Jacobi iteration
    for i in range(N): 
     for  j in range(N): 
       if i==j: 
          D[i] = A[i,j]
          R[i,j] = 0 
       else:
          R[i,j] = A[i,j]
   
    while norm(xn - x) > tolerance  and  k < max_iter: 
        x = xn
        xn = (b - dot(R, x)) / D
      

    return x 


# ************************************************************************
# The Gauss Seidel method is an iterative algorithm based on the following
# iteration: 
#    A = L + U (lower part includes diagonal) 
#
#    L x^{n+1} = b - U x^{n+1} 
#
#    Since L is diag0nal, the above system is solved to give: 
#        x_ij^{n+1} = ( b_i - sum j=1 to i-1( A_ij x_j^n)  -
#                             sum j=i+1 to N( A_ij x_j^{n+1} ) / A_ii  
#   
#*************************************************************************
def Gauss_Seidel(A, b):

    N = len(b)
    x1, x2 = zeros(N), zeros(N)
    Error, tolerance = 1, 1e-10 
    k, max_iter = 0, 100

  # Gauss Seidel iteration
    while Error > tolerance  and  k < max_iter: 

        x1[:] = x2[:]   # x1=x2 does not work 
        for i in range(N):
            S2 = dot( A[i, :i], x2[:i] )       # new values
            S1 = dot( A[i, i+1:], x1[i+1:] )   # old values
            x2[i] = ( b[i] - S2 - S1 )/ A[i, i]
        Error = norm(x2-x1)
        k += 1

    return x2 
    

def Test_iterative(): 
 
  A = array([[10, -1,  2,  0],
            [-1, 11, -1,  3],
            [ 2, -1, 10, -1],
            [ 0,  3, -1,  8]])

  b = array([6, 25, -11, 15])

  print(" my Jacobi solution: x =", Jacobi(A,b)  )
  print(" my Gauss-Seidel solution: x =", Gauss_Seidel(A,b) )
  print(" scipy Gauss solution: x =", solve(A,b) )



#******************************************************
#   Solve nonlinear scalar equations.
#
#     my newton, secant, bisection versus scipy: 
#******************************************************

#  1. Newton method
def derivative(f, x):

    h = 1e-5  
    return ( f(x+h) - f(x-h) )/(2*h)

def my_newton(f, x0):

    x, dx, eps = x0, 1., 1e-10

    while abs(dx) > eps: 
        dx = -f(x) / derivative(f, x)
        x = x + dx 
        print("  iteration newton x =", x, "dx =", dx)
    return x  


#  2. Secant method
def secant(f, x0, x1):

    x, dx, eps = x1, x1-x0, 1e-10

    while abs(dx) > eps: 
        dx = -f(x) *(x-x0) / (f(x)-f(x0))
        x0 = x 
        x = x + dx 

        print("  iteration secant x =", x, "dx =", dx)
    return x  

#  3. bisection method 
def bisection(f, a, b):

    x1, x2, dx, eps = a, b, b-a, 1e-10

    while abs(dx) > eps: 

        xm = (x1 + x2)/2 
        if f(x1)*f(xm) <= 0: 
            x2 = xm 
        else:
            x1 = xm 
        dx = x2 - x1
        print("  iteration secant x =", xm, "dx =", x2-x1)
    return xm  



def f(x): 

    return x**2 -1 


def Test_roots(): 
  
  print( "sol my newton =", my_newton(f, 0.8))  
  print( "sol my secant =", secant(f, 0.8, 0.9))  
  print( "sol my bisection =", bisection(f, 0., 2.1))  

  print( "sol scipy newton =", newton(f, 0.8))  
  print( "sol scipy secant =", newton(f, x0=0.8, x1=0.9))  
  print( "sol scipy bisection =", bisect(f, 0., 2.1))  


#**********************************************************
#   Solve nonlinear equations. Newton vectorial f: RN-> RN 
#**********************************************************
def Newton(F, x0):  
  """
 ____________________________________________________________________
  Newton solver 
        Inputs: 
                x0   : initial guess and output value 
                F(X) : vector function  
        return: 
                x : solution (F(x)=0)

  Author: Juan A Hernandez (juanantonio.hernandez@upm.es) Oct 2022 
_____________________________________________________________________
  """
  
  x, Dx, iteration, itmax = x0, x0, 0, 1000  
  print("x0 =", x0)
 
  while  norm(Dx) > 1e-8 and iteration <= itmax : 
    
      iteration += 1 
      Dx = Gauss( Jacobian( F, x0 ), -F(x0)) 
      x[:] = x[:] + Dx  # WARNING x = x + Dx (does not work)
      
      print("x =", x, "iteration =", iteration, "Newton norm(Dx) = ",  norm(Dx) ) 

  return x 

  
def Jacobian( F, x ):  

   Dx = 1e-3
   N = len(x)     
   Dxi, J = zeros(N), zeros((N, N))
       
   for i, _ in enumerate(x):

       Dxi[:] = 0
       Dxi[i] = Dx
       J[:,i] =  ( F(x + Dxi) - F(x - Dxi) )/(2*Dx)  
   
   return J    



def f(x): 

    return array( [ x**2 - 1 ] ) 


def Test_Neton_vectorial(): 

 x0 = array( [ 0.1 ])
 print(" My vectorial Newton: x =", Newton(f, x0 ) )

 sol = newton(f, x0 )
 print(" My scipy Newton: x =", sol)


if __name__ == "__main__":


   Test_iterative()
   Test_roots() 
   Test_Neton_vectorial()
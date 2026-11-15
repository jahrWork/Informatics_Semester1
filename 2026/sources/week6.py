
#******************************************************
#   Solve a linear system of equations: Gauss method. 
#******************************************************

from numpy import array, zeros, max, dot 
from scipy.linalg import solve


def  Gauss(A, b):
   """
 _________________________________________________________
 Solutions to a system of linear equations A x  =b
 Method: Gauss elimination (with scaling and pivoting)
 
   Inputs: 
          A : system matrix, 
          b : independent term 
  return:
          x 
          note: matrix A and b term are modified 

 Juan A. Hernandez, juanantonio.hernandez@upm.es (Oct 2022-2025) 
 
________________________________________________________________  
   """
   
   N = len(b);  x = zeros(N) 
  
#  begin forward elimination
#  elimination (after swapping)
#  for all rows below pivot:

   for i in range(0, N): 
     pivoting_row_swapping( A, b, i, N)

     for k in range(i+1, N):  
       c = A[k,i] / A[i,i]  
       A[k,:] = A[k,:] - c * A[i,:] 
       b[k] = b[k] - c * b[i] 
     
#  back substiturion
   for i in range(N-1, -1, -1):
     x[i] = ( b[i] - dot( A[i,i+1:N], x[i+1:N] ) )/ A[i,i]

   return x 




def pivoting_row_swapping( A, b, k, N): 

     s = zeros(N)

#    s[i] is the largest element of row i
     for i in range(k, N):   # loop over rows
       s[i] = max( abs(A[i,k:N]) ) 
      
#    find a row with the largest pivoting element
     pivot = abs( A[k,k] / s[k] )
     l = k
     for j in range(k, N): 
       if abs( A[j,k] / s[j] ) > pivot: 
          pivot = abs( A[j,k] / s[j] )
          l = j

#    Check if the system has a sigular matrix
     if pivot == 0.0 :  print(" The matrix is singular "); exit()
       
#    pivoting: swap rows k and l (if needed)
     if l != k : 
        A[ [k, l] ,k:N] =  A[ [l, k], k:N]  
        ( b[k], b[l] ) =  ( b[l], b[k] )




def Test_Gauss():
     
     

     A =  array( [ [1, 1, 1] , [1, -1, -1] , [1, -1, 1] ] )
     b =  array( [1, 2, 3 ] ) 
     x = Gauss( A, b )
     xsol = array([ 1.5, -1., 0.5])
     print("my Error =", xsol - x )
     print("scipy Error =", xsol - solve(A, b) ) 

     A =  array( [ [1, 2, 3] , [1, -2, -3] , [1, -2, 3] ] )
     b =  array( [1, 2, 3 ] ) 
     x = Gauss( A, b )
     xsol = array([ 1.5, -0.5,  1/6.])
     print("my Error =", xsol - x ) 
     print("scipy Error =", xsol - solve(A, b) ) 

     

#******************************************************
# Solve a linear system of equations by means of scipy 
# LU, determinant, inverse, linalg.solve
#******************************************************

#scipy.linalg is always compiled with support for BLAS and LAPACK
from scipy.linalg import lu_factor, lu_solve
from scipy.linalg import solve, inv, det

from numpy import array, matmul, sin , pi, zeros, dot 
from numpy.linalg import norm, cond
from numpy.random import random


#***********************************************************
# Before LU factoriztion: 
#   1. Look for max abs of column 0. swap between rows 0 and i 
#      this is piv[0] = i 
#   2. Look for max abs of column 1 in submatrix. swap 
#      this is piv[1] = j 
#
#      Matrix A after pivoting is: A = [ 3,4 ], [1,2] ]
#   3. Factorization LU 
#*************************************************************
def Test_LU_factorization(): 
  
  A = array(
        [
          [1, 2],
          [3, 4],
       ]
       )
  b = array([1, 1]) 


  LU, piv = lu_factor(A)
  print("LU=", LU)
  print("pivot=", piv)

  x = lu_solve((LU, piv), b)
  print("x =", x, matmul(A,x)-b )
 
#*************************************************
# Ill-conditioned matrix (almost singular)
#*************************************************
def Test_ill_posed_systems(): 

   eps0 = 1e-3
   eps = 1e-7

   A = array([[1, 1], [1, 1+eps]])
   b = array([1,1])
   print("Condition number (ill-conditioned):", cond(A))

   x = solve(A, b)
   print("Solution (ill-conditioned):", x)
   b_perturbed = b + array([eps0, -eps0])
   
   x = solve(A, b_perturbed)
   print("Ill-conditioned solution with perturbed b:", x)



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
#    L x^{n+1} = b - U x^{n} 
#*************************************************************************
def Gauss_Seidel(A, b):

    N = len(b)
    x1, x2, b1 = zeros(N), zeros(N), zeros(N)
    Error, tolerance = 1, 1e-10 
    k, max_iter = 0, 100

  # Gauss Seidel iteration
    while Error > tolerance  and  k < max_iter: 

        x1[:] = x2[:]   # x1=x2 does not work 
        for i in range(N):
            b1[i] = b[i] - dot( A[i, i+1:], x1[i+1:] )  # old values  

        for i in range(N):
            x2[i]  = ( b1[i] - dot( A[i, :i], x2[:i] ) )/ A[i, i] 
         
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








if __name__ == "__main__":

    Test_Gauss()
    Test_LU_factorization()
    Test_ill_posed_systems()
    Test_iterative()
 



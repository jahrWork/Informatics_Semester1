
#******************************************************
# Solve a linear system of equations by means of scipy 
# LU, determinant, inverse, linalg.solve
#******************************************************

#scipy.linalg is always compiled with support for BLAS and LAPACK
from scipy.linalg import lu_factor, lu_solve
from scipy.linalg import solve, inv, det

from numpy import array, matmul, sin , pi, zeros 
from numpy.linalg import norm, cond
from numpy.random import random
import matplotlib.pyplot as plt


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
def Test_LU_facorization(): 
  
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



#*************************************************
# Interpolation problem. Vandermonde matrix
# Ill-conditioned matrix (almost singular)
#*************************************************
def partition(a, b, N): 
  return array([a + (b-a)/N * i for i in range(0, N+1)])

def Vandermonde(x): 
    N = len(x)
    return array( [ [ x[i]**j for j in range(N)] for i in range(N) ])

def P(x, c): 
    return sum( [ c[k]*x**k for k in range(len(c)) ] )


def Test_Vandermonde_Interpolation():

  N = 20
  x = partition(0, 2*pi, N)
  y1 = sin(x)
  eps = 1e-2
  y2 = y1 + eps * random(N+1)

  A = Vandermonde(x)
  print("Condition number (ill-conditioned):", cond(A))
  c1 = solve(A , y1)
  c2 = solve(A , y2)
  k = array([ i for i in range(N+1)])
  plt.plot(k, c1, ".-")
  plt.plot(k, c2, ".-")
  plt.show()

  M = 13
  xp = partition(0, 2*pi, M)
  yp1, yp2 = zeros(M+1), zeros(M+1)

  for i, xi in enumerate(xp):
     yp1[i] = P(xi,c1)
     yp2[i] = P(xi,c2)

  plt.plot(xp, yp1, ".-")
  plt.plot(xp, yp2, ".-")
  plt.show()


if __name__ == "__main__":
  
 # Test_LU_facorization()
  Test_ill_posed_systems()
 # Test_Vandermonde_Interpolation()


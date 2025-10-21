
#******************************************************
# Solve a linear system of equations by means of scipy 
# LU, determinant, inverse, linalg.solve
#******************************************************

#scipy.linalg is always compiled with support for BLAS and LAPACK

from numpy import array, matmul 
from scipy.linalg import solve, inv, det

A = array(
      [
          [1, 2],
          [3, 4],
      ]
    )

b = array([1, 1]) 

x = solve(A, b)
print("x =", x, matmul(A,x)-b )

from scipy.linalg import lu_factor, lu_solve

# Look for max abs of column 0. swap between rows 0 and i 
# this is piv[0] = i 
# Look for max abs of column 1 in submatrix. swap 
# this is piv[1] = j 
#
# Matrix A after pivoting is: A = [ 3,4 ], [1,2] ]

LU, piv = lu_factor(A)
print("LU=", LU)
print("pivot=", piv)

x = lu_solve((LU, piv), b)
print("x =", x, matmul(A,x)-b )
 
print("A =", A)
print( " A * A^-1 =", matmul(A, inv(A)))
print("det(A)=", det(A))



            
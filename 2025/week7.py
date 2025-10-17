
#******************************************************
# Solve a linear system of equations by means of scipy 
# LU, determinant, inverse, linalg.solve
#******************************************************

#scipy.linalg is always compiled with support for BLAS and LAPACK

from numpy import array, matmul 
from scipy.linalg import solve, inv, det

A = array(
      [
          [3, 2],
          [2, -1],
      ]
    )

b = array([12, 1]) #.reshape((2, 1))

x = solve(A, b)
print("x =", x, matmul(A,x)-b )

from scipy.linalg import lu_factor, lu_solve

LU, piv = lu_factor(A)
x = lu_solve((LU, piv), b)
print("x =", x, matmul(A,x)-b )
 
print("A =", A)
print( " A * A^-1 =", matmul(A, inv(A)))
print("det(A)=", det(A))



            
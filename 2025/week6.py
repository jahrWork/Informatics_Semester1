
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

     
    


if __name__ == "__main__":

    Test_Gauss()



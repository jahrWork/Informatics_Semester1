
#********************************************************************
#  Aproximation of functions by means of polynomials:
#  Linear regression. Least squares method.
#********************************************************************

from numpy import array, polyfit, polyval, linspace,diag, array, matmul, transpose, shape
import matplotlib.pyplot as plt
from numpy.linalg import svd, solve  



def Test_numpy_interpolation_regression(): 
  
  # given data
  x = array([0, 1, 2, 3, 4, 5, 6])
  y = array([1, 2, 0, 5, 4, 3, 0])

  # polynomial
  c_k = polyfit(x, y, deg=len(x)-1)  
  c2  = polyfit(x, y, deg=4)

  xp = linspace(0, 6, 100)
  yp = polyval(c_k, xp)
  y2 = polyval(c2, xp)

  w = regression_vandermonde(x, y, 4)
  y3 = polynomial(w, xp)



  plt.scatter(x, y, label='Data')
  plt.plot(xp, yp, 'r', label='Interpolation')
  plt.plot(xp, y2, 'r', label='Least squares SVD')
  plt.plot(xp, y3, 'b', label='Vandermonde regression')
  plt.legend()
  plt.show()



def Vandermonde(x, N, M): 
   
    return array( [  [ x[j]**i for i in range(N) ] for j in range(M) ] ) 

def regression_vandermonde(x, y, N): 

      M = len(x)
      A = Vandermonde(x, N, M) 
     
      return solve( matmul(transpose(A), A ), matmul(transpose(A), y) ) 

def polynomial(w, x): 

   N = len(w)
   return sum(   w[k] * x**k for k in range(N) )





#**********************************************************************  
# This is equivalent to least squares but much more stable numerically 
#**********************************************************************
def Test_least_squares_by_means_SVD(): 

 Vandermonde = array([[1, 1],
                     [1, 2],
                     [1, 3],
                     [1, 4]])
 y = array([6, 5, 7, 10])

 U, S, VT = svd(Vandermonde, full_matrices=False)

 # pseudo-inverse Moore-Penrose 
 S_inv = diag(1/S)

 # Solve Vandermonde c = y
 c = VT.T @ S_inv @ U.T @ y
 print("Coefficients:", c)


if __name__ == "__main__":
  
    Test_numpy_interpolation_regression()
    Test_least_squares_by_means_SVD()





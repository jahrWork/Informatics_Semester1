
#********************************************************************
#  Aproximation of functions by means of polynomials:
#     1. Interpolation methods. Lagrange interpolation 
#     2. Linear regression Linear regression. Least squares method.
#********************************************************************

from numpy import array, polyfit, polyval, linspace,diag, array
import matplotlib.pyplot as plt
from numpy.linalg import svd



def Test_interpolation_regression(): 
  
  # given data
  x = array([0, 1, 2, 3, 4, 5, 6])
  y = array([1, 2, 0, 5, 4, 3, 0])

  # polynomial
  c_k = polyfit(x, y, deg=len(x)-1)  
  c2  = polyfit(x, y, deg=4)

  xp = linspace(0, 6, 100)
  yp = polyval(c_k, xp)
  y2 = polyval(c2, xp)


  plt.scatter(x, y, label='Data')
  plt.plot(xp, yp, 'r', label='Interpolation')
  plt.plot(xp, y2, 'r', label='Least squares')
  plt.legend()
  plt.show()

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
  
    Test_interpolation_regression()
    Test_least_squares_by_means_SVD()
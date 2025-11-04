from numpy import array, linspace, zeros




def Test_lagrange_scipy(): 

  from numpy import array, polyfit, polyval, linspace, zeros
  from scipy.interpolate import lagrange
  import matplotlib.pyplot as plt


  
  # given points
  x = array([0, 1, 2, 3, 4, 5, 6])
  y = array([1, 2, 0, 5, 4, 3, 0])

  # polynomial
  P = lagrange(x, y)
  dPdx = P.deriv()

  xp = linspace(0, 6, 100)
  yp = P(xp)
  dypdx = dPdx(xp)

  plt.scatter(x, y, label='Data')
  plt.plot(xp, yp, 'r', label='Lagrange polynomial')
  plt.plot(xp, dypdx, 'r', label='Derivative of Lagrange polynomial')
  plt.legend()
  plt.show()

  x = array([0, 1, 2])
  y = array([1, 0, 0])
  P = lagrange(x, y)
  dPdx = P.deriv()
  d2Pdx2 = dPdx.deriv()
  print( d2Pdx2(0) )

  x = array([0, 1, 2])
  y = array([0, 1, 0])
  P = lagrange(x, y)
  dPdx = P.deriv()
  d2Pdx2 = dPdx.deriv()
  print( d2Pdx2(1) ) 

# ******************************************************************************************
#                                 Lagrange polynomials
# 
#   Recurrence relation  to obtain derivatives  values of the Lagrange polynomials 
#   at xp from a set of nodes x(0:N)
#
#       lagrange_j{n} (x) = (x-x0)(x-x1)(x-x2)........(x-xn) / (xj- x0)(xj-x1)(xj-x2).......(xj-xn), j=0...n
#       lagrange_j{n} (x) = (x-xm)/(xj-xm) lagrange_j{n-1} (x) 
# 
#       d^k lagrange_j{n} (x) /dx^k  = 
#        ( d^k lagrange_j{n-1} (x) /dx^k (x-xm) + k d^(k-1) lagrange_j{n-1} (x) /dx^(k-1) ) / (xj -xm ), n=0...N  
#
#        k =  0 means value of lagrange_j{n} (x) at xp 
#        k > 1  means derivative value of lagrange_j{n} (x) at xp 
# 
#  It returns Lagrange_polynomials(k,j) 
# 
#      k: meaning given above 
#      j: corresponding with l_j(x) (this polynomial equals to one in x_j and vanishes at the rest of nodes) 
# 
#  Author : Juan A Hernandez (juanantonio.hernandez@upm.es) November 2025 
# *************************************************************************************************

def Lagrange_polynomials( x, xp ):  
   
 # first index: derivative, second:j polynomial, third: order
   N = len(x)-1
   Lagrange = zeros((N+1, N+1, N+1)) 

   # j means different lagrange polynomials 
   for  j in range(N+1):  
      
      # lagrange j polynomial of order 0 is equal to 1 
      Lagrange[0, j, 0] = 1 
     
      n = 1 
      for i in range(N+1):  
         
         if i!=j:   
          # the order of the polynomial increases only when the nodal point x[i] is taken into account (i!=j)
          for k in range(N, -1, -1): # k is derivative order
            Lagrange[k,j,n] = ( Lagrange[k,j,n-1] *( xp - x[i] ) + k * Lagrange[k-1,j,n-1] )/( x[j] - x[i] ) 
          n = n + 1 

   # it returns lagrange polynomials associated to node x_j 
   # and their derivatives evaluated at x=xp
   return Lagrange[:,:,n-1] 

#************************************************************************
# It determines finite difference formulas of any order
#  I(x) = sum ( f_j Langrange_j(x) )
#  DF =  ( d^k I /dx^k )_{x_i} = sum ( f_j d^k Lagrange_j/dx^k (x_i))
#  Df = sum_j ( f_j D_{ij} ) 
#  
#   Input: 
#          x modes j=0.... N 
#   return:
#          D_{ij}  
# 
# Author:   Juan A Hernandez (juanantonio.hernandez@upm.es) November 2025
#*************************************************************************
def FD_formulas(x): 
     
 

  N = len(x) - 1 
  # derivative, j lagrange polynomial, i point 
  D = zeros((N+1,N+1,N+1)) 

  for i in range(len(x)):
    D[:,:,i] = Lagrange_polynomials(x, x[i])

  return D 



def Test_FD_formulas(N): 
 

  # N order of polynomial to calculate FD formulas 
  x = array( [ i for i in range(N+1) ] )

  D = FD_formulas(x) 
  print("First derivative =", D[1,:,0])
  print("First derivative =", D[1,:,1])
  print("First derivative =", D[1,:,2])

  print("Second derivative =", D[2,:,0])
  print("Second derivative =", D[2,:,1])
  print("Second derivative =", D[2,:,2])



def Test_Lagrange(): 
   
  N = 2 # order of polynomial 
  x = array( [ i for i in range(N+1) ] )
  import matplotlib.pyplot as plt 

  M = 100
  xm = linspace(0, N, M)
  ym = zeros((M,3))
  for i in range(M):
    L = Lagrange_polynomials(x, xm[i])
    ym[i,:] = L[0,:]

  plt.plot(xm, ym)
  plt.show()


def Test_Lagrange2(): 
   
  N = 2 # order of polynomial 
  x = array( [ i for i in range(N+1) ] )

  xp = 0 
  L = Lagrange_polynomials(x, xp)
  print("\nLagrange polynomials associated to node (x0,x1,x2) =(0,1,2) ")
  print("and their derivatives k=2,1,0 evaluated at xp = 0")
  print("k=2  L(2,:) =", L[2,:])
  print("k=1  L(1,:) =", L[1,:])
  print("k=0  L(0,:) =", L[0,:])



if __name__ == "__main__":

     Test_Lagrange2()
     Test_lagrange_scipy()
     Test_Lagrange()  
     Test_FD_formulas(N=2)
     
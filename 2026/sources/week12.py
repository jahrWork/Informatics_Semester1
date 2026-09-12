
#************************************************************************
# Boundary value problem. F(U) = 0 with boundary conditions 
#    
#   My code: Test_my_BVP versus scipy: Test_scipy_BVP
#**************************************************************************


from numpy import zeros, linspace, array  
import matplotlib.pyplot as plt

from scipy.linalg import solve
from scipy.integrate import solve_bvp



#************************************************************************
# Boundary value problem. 
#    Convection-diffusion equation 
#    d2T/dx2 + a dT/dx + b T = 0 with T0 at x=0 and T1 at x=1
#    F(U) = 0 with U = [ T, dTdx ]
#**************************************************************************
def Convection_diffusion_E(x,U): 

     T, dTdx = U  
     a, b = 5, 1 

     return array( [ dTdx, -a *dTdx - b * T  ]) 

def BC_Convection_diffusion_E(Ua, Ub): 

     return array( [ Ua[0] - 0, Ub[0] - 1  ]) 


#************************************************************************
# Convection-diffusion equation 
#   Input: 
#           T discretized with T0, T1, ........ TN with N+1 points 
#   Output:
#           Eq0 ...EqN discretized equation: bounday points +  inner points (1..N)
#**************************************************************************
def Discretized_Convection_diffusion_E(T): 
    
    N = len(T) - 1
    dx = 1/N 
    a, b = 5, 1
    T0, TN = 0, 1 
    
    Equation = zeros(N+1)

#   Boundary conditions 
    Equation[0] = T[0] - T0 
    Equation[N] = T[N] - TN 

#   inner points  
    for j in range(1, N): 
       Equation[j] =   ( T[j+1] - 2*T[j] + T[j-1] )/dx**2 + \
                       a*( T[j+1] - T[j-1] )/(2*dx) + b * T[j] 

    return Equation 

#***************************************************************
#* If F:RN->RN  is linear F = A x + b where A is a matrix NxN 
#***************************************************************
def linear_system(F, N): 

    delta, A = zeros(N+1), zeros( (N+1,N+1) )
    b = F(delta)

    for i in range(0, N+1): 
        delta[:] = 0 
        delta[i] = 1 
        A[:, i] = F(delta) - b   

    return A, b  


def Test_my_BVP(N): 
  
  x = linspace(0, 1, N+2)
  A, b = linear_system(F = Discretized_Convection_diffusion_E, N = N+1)
  T = solve(A, -b)
  plt.plot(x, T, ".-")
 

def Test_scipy_BVP(N): 
  
  x = linspace(0, 1, N)
  U0 = zeros((2, N))  
  U = solve_bvp(Convection_diffusion_E, BC_Convection_diffusion_E, x, U0)
  plt.plot(U.x, U.y[0], ".-",label='Numericals')


if __name__ == "__main__":
   
   Test_my_BVP(N=10)
   Test_scipy_BVP(N=10)  
   plt.show()
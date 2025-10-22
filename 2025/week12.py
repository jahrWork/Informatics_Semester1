
from scipy.linalg import solve
from numpy import zeros, linspace 
import matplotlib.pyplot as plt

#*************************************************************
# Contour value problem. 
# Convection-diffusion equation 
#   d2T/dx2 + a dT/dx + c T = 0 with T0 at x=0 and T1 at x=1
#   T is discretized with T0, T1, ........ TN points or nodes
#**************************************************************

def Convection_diffusion_E(T): 
    
    N = len(T) - 1
    dx = 1/N 
    T[0], T[N] = 0, 1
    a, b = 5, 1

    # discretized equation only for inner points 
    Equation = zeros(N-1)
    for j in range(1, N): 
       Equation[j-1] =   ( T[j+1] - 2*T[j] + T[j-1] )/dx**2 + \
                       a*( T[j+1] - T[j-1] )/(2*dx) + b * T[j] 

    return Equation 

#***************************************************************
#* If F:RN->RN  is linear F = A x + b where A is a matrix NxN 
#***************************************************************
def linear_system(F, N): 

    delta, A = zeros(N+1), zeros( (N-1,N-1) )

    delta[:] = 0 
    b = F(delta)

    for i in range(1,N): 
        delta[:] = 0 
        delta[i] = 1 
        A[i-1, :] = F(delta) - b     

    return A, b  



N = 100 
x = linspace(0, 1, N+1)
A, b = linear_system(F = Convection_diffusion_E, N = N)
T = solve(A, -b)

print(A, b)
plt.plot(x[1:N], T)
plt.show()

    

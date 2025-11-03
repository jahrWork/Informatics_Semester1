

#************************************************************************
# Cauchy problem. 
#    dU/dt  = F(U,t) with U0 at t=0 
#
#    My code : Cauchy_problem versus scipy: solve_ivp 
#**************************************************************************

from numpy import zeros, array  
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp # solve initial value problem 

def first_version(): 
    """ 
    This is a 101 code (our starting point) to integrate an Oscillator with the Euler method.
    The objective of this course is to learn how to write 
    functional programming codes by means of function composition.
    The idea is to mimic mathematical concepts or abstractions.  
    """
    # d2x/dt2 +x = 0 -> U = [ x, xdot ]
    # dU/dt = F(U) = [ xdot, -x ]

    # initial conditions 
    U = array( [ 1, 0 ])

    #time steps 
    N = 100 

    #x,y to plot 
    x,y = array( zeros(N) ), array( zeros(N) )
    x[0] = 0
    y[0] = U[0]
    
    for i in range(1, N): 
    
      F = array( [ U[1], -U[0] ] ) 
      dt = 0.1 
      U = U + dt * F 

      x[i] = x[i-1] + dt
      y[i] = U[0]
    
    plt.plot(x, y, ".-")
    plt.show()



#******************************************************
#  Initial value problem ODES. Euler 
#******************************************************
"""
  Temporal_schemes

    Inputs: 
           U : state vector at t1
           t1: initial time 
           t2: final time
           F(U,t) : Function dU/dt = F(U,t)

    Return: 
           U state vector at t2   
"""
def Euler(U, t1, t2, F): 

    return U + (t2-t1) * F(t1, U)

def RK2(U, t1, t2, F): 

    dt = t2-t1
    k1 = F(t1, U)
    k2 = F(t2, U+dt*k1)
    
    return U + dt/2 * ( k1 + k2 ) 


def Cauchy_problem( F, t, U0, Temporal_scheme ): 
     """
    Inputs:  
           F(U,t) : Function dU/dt = F(U,t) 
           t : time partition t (vector of length N+1)
           U0 : initial condition at t=0
           Temporal_scheme 

    Return: 
           U: matrix[N+1, Nv], Nv state values at N+1 time steps     
     """
     N, Nv =  len(t)-1, U0.size
     U = zeros( (Nv, N+1), dtype=type(U0) )

     U[:,0] = U0
     for n in range(N):
           U[:, n+1] = Temporal_scheme( U[:, n], t[n], t[n+1],  F ) 

     return U

def Oscillator(t, U):
      
     x, xd = U[0:2]
     return array([ xd, -x ])

def Damped_Oscillator(t, U):
      
     x, xd = U[0:2]
     return array([ xd, -x - 0.7*xd ])

#***************************************************************
# Partition of segment [a, b] in N intervals.
# Determine interior nodes x_i = a + (b-a)/N i from i=0 to i=N
#***************************************************************
def partition(a, b, N): 
  
  return array([a + (b-a)/N * i for i in range(0, N+1)])



if __name__ == "__main__":

  first_version()


  (t0, tf) = (0, 10)
  U0 = array([1, 0])
  t_domain = partition(t0, tf, 100)
  U1 = Cauchy_problem( F = Oscillator, t = t_domain, U0 = U0, Temporal_scheme = Euler)
  U2 = Cauchy_problem( F = Damped_Oscillator, t = t_domain, U0 = U0, Temporal_scheme = Euler)
  plt.plot(t_domain,  U1[0,:], ".-")      
  plt.plot(t_domain,  U2[0,:], ".-")     
  plt.show()

  U1 = Cauchy_problem( F = Oscillator, t = t_domain, U0 = U0, Temporal_scheme = Euler)
  U2 = Cauchy_problem( F = Oscillator, t = t_domain, U0 = U0, Temporal_scheme = RK2)
  plt.axis("equal")
  plt.plot(U1[0,:], U1[1,:], ".-"  )  
  plt.plot(U2[0,:], U2[1,:], ".-" )     
  plt.show()

  U3 = solve_ivp(Oscillator, (t0, tf), U0, method='RK45', t_eval = t_domain )
  plt.axis("equal")
  plt.plot(U3.y[0,:], U3.y[1,:,], ".-"  )  
  plt.show()
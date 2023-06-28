# matplotlib library to plot functions 




import matplotlib.pyplot as plt
from numpy import  array, sin, cos, pi, zeros, linspace 
from random import random, uniform

# **********************************************
# 1. plot math graphs 
# y = f(x) function to plot 
# y_i = f(x_i) forall i in [0, N]
# **********************************************
# N = 100




# t = array( [ 2*pi*i/N for i in range(N+1) ] )
# print("t[N] =", t[N], 2*pi)


# x = 3 * sin(t)  # x_i = 3 sin ( t_i )
# y = 2 * cos(t) 


# plt.plot(x, y, "red")
# plt.show()

# plt.plot( t,x,  "blue")
# plt.plot( t,y,  "green")
# plt.show()


# fig, ax = plt.subplots(1,1)
# ax.set_aspect("equal")

# N = 300
# t = linspace(0, 4*pi, N)

# x = zeros(N)
# y = zeros(N)


# for i in range(N): 
 
#     if t[i] < 2*pi: 
#       a = 1 
#       e = 0.8 
#     else: 
#       a = 1 
#       e = 0.0 
    
#     r = a * (1 - e**2) / ( 1 + e * cos( t[i] ) ) 
#     x[i] = e*a + r * cos( t[i] )
#     y[i] = r * sin( t[i] )


# ax.plot(x, y)
# plt.show()




#********************************************
# 2. plot ants, persons as points 
#********************************************
# def plot(x, y): 
    
#   plt.plot( x, y, "r.")
#   plt.xlim(0,1)
#   plt.ylim(0,1)
#   plt.show()
  


# N = 100
# x_a = [ ]
# y_a = [ ]

# for i in range(N):
#     x_a += [ random() ]
#     y_a += [ random() ] 

# plot(x_a, y_a)


# for i in range(len(x_a)): 
    
#     if x_a[i] < 0.3 : 
#         x_a[i] += 0.3 
        
#     elif y_a[i] < 0.3: 
#         y_a[i] += 0.3
   
# plot(x_a, y_a)



#********************************************
# 3. animate points 
#********************************************
# def plot(x, y): 
    
#   plt.plot( x, y, "r.")
#   plt.xlim(0,1)
#   plt.ylim(0,1)
#   plt.show()
  

# def initial_position():
#   N = 100
#   x = [ ]
#   y = [ ]

#   for i in range(N):
#     x += [ random() ]
#     y += [ random() ] 
    
#   return x, y

# def move_ants(x, y):
 
#   N = len(x) 
#   dt = 0.01 
  
#   for i in range(N):
#     vx, vy =  [ uniform(-1, 1.), uniform(-1., 1.) ]  
#     x[i] += dt * vx 
#     y[i] += dt * vy
    
#   return x, y    

# x, y = initial_position() 
  
# for i in range(100): 
#     x, y = move_ants(x, y)
#     plot(x, y)
#     plt.pause(0.1)
#     plt.show()


#********************************************
# 4. draw circles, rectangles, ... 
#********************************************

from matplotlib.patches import Rectangle, Circle

#define Matplotlib figure and axis
fig, ax = plt.subplots()

plt.xlim(0,10)
plt.ylim(0,10)
ax.set_aspect("equal")

#add rectangle to plot
ax.add_patch( Rectangle((1, 1), 2, 6) )
ax.add_patch( Circle( (5, 5),  1) )

ax.add_patch( Rectangle((6, 6), 1, 1, 
              edgecolor = 'red',
              facecolor = 'blue',
              fill=True,
              lw=5)  )
                        


plt.show()
# =============================================================================



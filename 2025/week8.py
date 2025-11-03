
#******************************************************
#   Matplotlib
#******************************************************



import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle
from matplotlib.widgets import Slider, Button, RadioButtons

from numpy import array, sin, cos, pi, zeros, linspace, arange 
from numpy import meshgrid, max, abs, arctan2  
from numpy.linalg import norm 
from random import random, uniform

import pygame 

import soundfile as sf
#import simpleaudio as sa
#from midiutil import MIDIFile


#***************************************************************
# Partition of segment [a, b] in N intervals.
# Determine interior nodes x_i = a + (b-a)/N i from i=0 to i=N
#***************************************************************
def partition(a, b, N): 
  x = array([a + (b-a)/N * i for i in range(0, N+1)])
  return x 

def f(x): 
    return sin(pi*x)

def derivative(f,  x, h=1e-3): 
    return ( f(x+h) - f(x-h) )/(2*h)

def Test_plot(): 
 
 x = partition(a=0., b=1., N=20)
 y = f(x)
 yp = derivative(f, x) 

 print(" x =", x)
 print( "y = ", y)
 plt.plot(x,y)
 plt.plot(x,yp)
 plt.show()






# **********************************************
# 1. Basic plot math graphs
# y = f(x) function to plot
# y_i = f(x_i) forall i in [0, N]
# **********************************************
def Test_plot_xy(): 
  N = 100
  dt = 2*pi/N 
  t = array( [ dt*i for i in range(N+1) ] )
  print("t =", t)
  print("t[N] =", t[N], 2*pi)

  x = zeros(N+1) # it creates a vector of N+1 components equal to zero
  for i in range(0,N+1):
      x[i] = 3 * sin( t[i] )

  x = 3 * sin(t)  # equivalent to x_i = 3 sin ( t_i ) from i=0 to i=N
  y = 2 * cos(t)

  plt.plot(t, x,  "blue")
  plt.plot(t, x,"." )
  plt.plot(t, y,  "green")
  plt.show()

  plt.plot(y, x, "blue")
  plt.show()




#********************************
# Kepler orbits
#********************************
def Test_plot_Kepler_orbits(): 
 
 fig, ax = plt.subplots(1, 1)
 ax.set_aspect("equal")

 N = 300
 t = linspace(0, 4*pi, N)

 x = zeros(N)
 y = zeros(N)


 for i in range(N):

    if t[i] < 2*pi:
        a = 1
        e = 0.8
    else:
        a = 1
        e = 0.0

    r = a * (1 - e**2) / (1 + e * cos(t[i]))
    x[i] = e*a + r * cos(t[i])
    y[i] = r * sin(t[i])


 ax.plot(x, y)
 plt.show()

#**************************************
# Euler integration of orbits 
#**************************************
def Test_plot_Euler(): 
 N = 1000
 r = array( [1, 0] )
 v = array( [0,1] )
 x = zeros(N+1) 
 y = zeros(N+1)

 dt = 8*pi/N 
 t = array( [ dt*i for i in range(N+1) ] )
 for i, ti in enumerate(t): 
    x[i] = r[0]
    y[i] = r[1]
    r = r + dt * v 
    v = v - dt * r / norm(r)**3 

 fig, ax = plt.subplots(1, 1)
 ax.set_aspect("equal")
 plt.plot(x,y)
 plt.show()



#***************************************************
# Contour plots 
#***************************************************
def Test_contour(): 
   
 N = 100
 x = partition(-2*pi, 2*pi, N)
 y = partition(-2*pi, 2*pi, N)
 z = zeros( (len(x), len(y))  )
 for i in range(len(x)): 
    for j  in range(len(y)): 
        z[i,j] = sin( x[i] ) * cos ( y[j] )

# Creating a filled contour plot
 plt.contourf(z, levels = 50)

# Adding labels and title
 plt.xlabel('X-axis')
 plt.ylabel('Y-axis')
 plt.title('Filled Contour Plot')

# Displaying the plot
 plt.show()


    

#*****************************************************
# Koch snow flake 
# **************************************************** 
def Koch_snowflake(xi, xf, n):  

    global L 
    if n == 0: 
        L += [ ( array([ xi[0], xf[0] ]), array([ xi[1], xf[1] ])) ]
        
    else:  
        x1 = xi + (xf - xi) / 3
        x3 = xf - (xf - xi) / 3
       
        R = x3 - x1
        alpha = arctan2( R[1], R[0] ) + pi / 3
        x2 = x1 + norm(R) * array( [ cos(alpha), sin(alpha) ] ) 

        Koch_snowflake(xi, x1, n - 1)
        Koch_snowflake(x1, x2, n - 1)
        Koch_snowflake(x2, x3, n - 1)
        Koch_snowflake(x3, xf, n - 1)
        

def  Test_build_Koch_snowflake():
    
    global L 
    L = [ ]
    Koch_snowflake( xi = array([0,0]), xf = array([1,0]), n=4 )

    for (p1, p2) in L: 
        plt.plot(p1, p2)
    plt.show()
 





# ********************************************
# 2. plot ants, persons as points
# ********************************************
def plot(x, y):

    plt.plot(x, y, "r.")
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.show()

def Test_plot_ants(): 

 N = 100
 x_a = []
 y_a = []

 for i in range(N):
    x_a += [random()]
    y_a += [random()]

 plot(x_a, y_a)


 for i in range(len(x_a)):

    if x_a[i] < 0.3:
        x_a[i] += 0.3

    elif y_a[i] < 0.3:
        y_a[i] += 0.3

 plot(x_a, y_a)


# ********************************************
# 3. animate points
# ********************************************
def plot(x, y):

    plt.plot(x, y, "r.")
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.show()


def initial_position():
    N = 100
    x = []
    y = []

    for i in range(N):
        x += [random()]
        y += [random()]

    return x, y

def move_ants(x, y):

    N = len(x)
    dt = 0.01

    for i in range(N):
        vx, vy = [uniform(-1, 1.), uniform(-1., 1.)]
        x[i] += dt * vx
        y[i] += dt * vy

    return x, y

def Test_animate(): 
 x, y = initial_position()

 for i in range(100):
    x, y = move_ants(x, y)
    plot(x, y)
    plt.pause(0.1)
    plt.show()

 plt.show()


# ********************************************
# 4. draw circles, rectangles, ...
# ********************************************
def Test_circles_rectangles(): 
 fig, ax = plt.subplots()

 plt.xlim(0, 10)
 plt.ylim(0, 10)
 ax.set_aspect("equal")

# add rectangle to plot
 ax.add_patch( Rectangle((1, 1), 2, 6))
 ax.add_patch( Circle((5, 5),  1) )

 ax.add_patch( Rectangle((6, 6), 1, 1,
                       edgecolor='red',
                       facecolor='blue',
                       fill=True,
                       lw=5))


 plt.show()



#********************************************
# Simple pygame program
#********************************************
def Test_pygame_example(): 
  

  pygame.init()
  screen = pygame.display.set_mode([500, 500])

# Fill the background with white
  screen.fill((155, 255, 255))

# Draw a solid blue circle in the center
  pygame.draw.circle(surface = screen, color = (0, 0, 255), 
                     center = (250, 250), radius = 75)

# Update the display
  pygame.display.update()

# Run until the user asks to quit
  running = True
  while running:

    # Did the user click the window close button?
    events =  pygame.event.get()
    for event in events :

        if event.type == pygame.QUIT:          
            running = False

        elif event.type == pygame.MOUSEBUTTONUP:
                draw_circle(screen)
                pygame.display.update()  

def draw_circle(screen):
 
    pos = get_pos()
    pygame.draw.circle(screen, (0,   0, 255), pos, 20)

def get_pos():

    return pygame.mouse.get_pos()








#********************************************************************
# Music from the physical point of view 
#********************************************************************
def basic_piano_note(frequency, duration, sample_rate=44100):
      
    # Generate time axis
      t = linspace(0, duration, int(sample_rate * duration), endpoint=False)

    # Generate the fundamental frequency component (first harmonic)
      waveform = zeros( len(t) )
    
    # Add higher harmonics with decreasing amplitude 
      harmonics = [ (1, 1), (2, 0.5), (3, 0.2), (4, 0.1), (5, 0.05) , (6, 0.02) ]  
     
      for n, A in harmonics:
        waveform += A * sin(2 * pi * n * frequency * t)

    # Normalize waveform to prevent clipping
      waveform /= max(abs(waveform))
    
      return t, waveform



def play_wav(file_path):
    try:
        # Load and play the .wav file directly with simpleaudio
          wave_obj = sa.WaveObject.from_wave_file(file_path)
          play_obj = wave_obj.play()
        
        # Wait for the playback to finish
          play_obj.wait_done()
          print("Playback finished.")

    except FileNotFoundError:
          print("File not found. Please check the file path.")


def Test_wav_music(): 

 # C3 note in Hz
   frequency = 130.8; duration = 2.0; fs = 44100   

 # Generate the note
   t, note = basic_piano_note(frequency, duration)

   N = int( fs / frequency )
   plt.plot(t[0:N], note[0:N])
   plt.show()

 # Save to file
   file_name = 'piano_note.wav' 
   sf.write(file_name, note, 44100)

   play_wav( file_name )

   return file_name  


#*********************************************************
# Creating midi files for musicians 
#*********************************************************
# def Test_midi(): 

#  degrees  = [60, 62, 64, 65, 67, 69, 71, 72]  # MIDI note number
#  track    = 0
#  channel  = 0
#  time     = 0    # In beats
#  duration = 1    # In beats
#  tempo    = 60   # In BPM
#  volume   = 100  # 0-127, as per the MIDI standard

#  MyMIDI = MIDIFile(1)  # One track, defaults to format 1 (tempo track is created
#                       # automatically)
#  MyMIDI.addTempo(track, time, tempo)

#  for i, pitch in enumerate(degrees):
#     MyMIDI.addNote(track, channel, pitch, time + i, duration, volume)

#  with open("major-scale.mid", "wb") as output_file:
#     MyMIDI.writeFile(output_file)

#  import os 
#  os.startfile("major-scale.mid")




if __name__ == "__main__":

    #Test_plot()  
    #Test_plot_xy()
    #Test_plot_Kepler_orbits() 
    #Test_plot_Euler()
 
    #Test_plot_ants()

    #Test_build_Koch_snowflake()
    #Test_circles_rectangles()
    # #Test_animate()
    # Test_contour()
   
    Test_pygame_example()

    # Test_wav_music()
    # Test_midi()
               
                










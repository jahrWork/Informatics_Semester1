

from matplotlib.patches import Rectangle, Circle
import matplotlib.pyplot as plt
from numpy import array, sin, cos, pi, zeros, linspace
from random import random, uniform

# **********************************************
# 1. plot math graphs
# y = f(x) function to plot
# y_i = f(x_i) forall i in [0, N]
# **********************************************
# N = 100

# t = array( [ 2*pi*i/N for i in range(N+1) ] )
# print("t =", t)
# print("t[N] =", t[N], 2*pi)

# x = zeros(N+1)
# for i in range(0,N+1):
#     x[i] = 3 * sin( t[i] )

# x = 3 * sin(t)  # equivalent to x_i = 3 sin ( t_i ) from i=0 to i=N
# y = 2 * cos(t)

# plt.plot(t, x,  "blue")
# plt.plot(t, x, ".", "blue")
# plt.plot(t, y,  "green")
# plt.show()



# plt.plot(y, x, "blue")
# plt.show()


# fig, ax = plt.subplots(1, 1)
# ax.set_aspect("equal")

# N = 300
# t = linspace(0, 4*pi, N)

# x = zeros(N)
# y = zeros(N)


# for i in range(N):

#     if t[i] < 2*pi:
#         a = 1
#         e = 0.8
#     else:
#         a = 1
#         e = 0.0

#     r = a * (1 - e**2) / (1 + e * cos(t[i]))
#     x[i] = e*a + r * cos(t[i])
#     y[i] = r * sin(t[i])


# ax.plot(x, y)
# plt.show()

#***************************************************
# Contour plots 
#***************************************************
# from numpy import array, meshgrid, sin , cos, zeros, pi 
# import matplotlib.pyplot as plt

# def partition(a, b, N): # equivalent to linspace from numpy 
#   x = array([a + (b-a)/N * i for i in range(0, N+1)])
#   return x 

# # Generating data
# N = 10
# x = partition(-2*pi, 2*pi, N)
# y = partition(-2*pi, 2*pi, N)
# z = zeros( (len(x), len(y))  )
# for i in range(len(x)): 
#     for j  in range(len(y)): 
#         z[i,j] = sin( x[i] ) * cos ( y[j] )

# # Creating a filled contour plot
# plt.contourf(z, levels = 50)

# # Adding labels and title
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.title('Filled Contour Plot')

# # Displaying the plot
# plt.show()








# ********************************************
# 2. plot ants, persons as points
# ********************************************
# def plot(x, y):

#     plt.plot(x, y, "r.")
#     plt.xlim(0, 1)
#     plt.ylim(0, 1)
#     plt.show()


# N = 100
# x_a = []
# y_a = []

# for i in range(N):
#     x_a += [random()]
#     y_a += [random()]

# plot(x_a, y_a)


# for i in range(len(x_a)):

#     if x_a[i] < 0.3:
#         x_a[i] += 0.3

#     elif y_a[i] < 0.3:
#         y_a[i] += 0.3

# plot(x_a, y_a)


# ********************************************
# 3. animate points
# ********************************************
# def plot(x, y):

#     plt.plot(x, y, "r.")
#     plt.xlim(0, 1)
#     plt.ylim(0, 1)
#     plt.show()


# def initial_position():
#     N = 100
#     x = []
#     y = []

#     for i in range(N):
#         x += [random()]
#         y += [random()]

#     return x, y


# def move_ants(x, y):

#     N = len(x)
#     dt = 0.01

#     for i in range(N):
#         vx, vy = [uniform(-1, 1.), uniform(-1., 1.)]
#         x[i] += dt * vx
#         y[i] += dt * vy

#     return x, y


# x, y = initial_position()

# for i in range(100):
#     x, y = move_ants(x, y)
#     plot(x, y)
#     plt.pause(0.1)
#     plt.show()


# ********************************************
# 4. draw circles, rectangles, ...
# ********************************************

# fig, ax = plt.subplots()

# plt.xlim(0, 10)
# plt.ylim(0, 10)
# ax.set_aspect("equal")

# # add rectangle to plot
# ax.add_patch( Rectangle((1, 1), 2, 6))
# ax.add_patch( Circle((5, 5),  1) )

# ax.add_patch( Rectangle((6, 6), 1, 1,
#                        edgecolor='red',
#                        facecolor='blue',
#                        fill=True,
#                        lw=5))


# plt.show()

# ============================================================
# from numpy import arange, sin, pi
# import matplotlib.pyplot as plt
# from matplotlib.widgets import Slider, Button, RadioButtons

# def build_gui(): 

#   def update_A(val):
#     A = val
#     f = S_f.val
#     t, s = graph(A, f)
#     l.set_ydata( s )
#     fig.canvas.draw_idle()

#   def update_f(val):
#     f = val
#     A = S_A.val
#     t, s = graph(A, f)
#     l.set_ydata( s )
#     fig.canvas.draw_idle()

#   def reset(event):
#     S_f.reset()
#     S_A.reset()

#   def color(label):
#     l.set_color(label)
#     fig.canvas.draw_idle()

#   def graph(A, f): 

#     t = arange(0.0, 1.0, 0.001)
#     s = A * sin( 2*pi*f*t )
#     return t, s 

#   fig, ax = plt.subplots()
#   plt.subplots_adjust(left=0.25, bottom=0.25)
#   A0 = 5;  f0 = 3
   
#   t, s = graph(A0, f0)
#   l, = plt.plot(t, s, lw=2, color='red')
#   plt.axis([0, 1, -10, 10])

#   axcolor = "yellow"
#   axes_f = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
#   axes_A = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)

#   S_f = Slider(axes_f, 'Freq', 0.1, 30.0, valinit = f0) 
#   S_f.on_changed(update_f)

#   S_A = Slider(axes_A, 'Amp', 0.1, 10.0, valinit = A0)
#   S_A.on_changed(update_A)

#   axes_reset = plt.axes([0.8, 0.025, 0.1, 0.04])
#   B_reset = Button(axes_reset, 'Reset', color=axcolor, hovercolor='0.975')
#   B_reset.on_clicked(reset)

#   axes_color = plt.axes([0.025, 0.5, 0.15, 0.15], facecolor=axcolor)
#   R_color = RadioButtons(axes_color, ('red', 'blue', 'green'), active=0)
#   R_color.on_clicked(color)

#   plt.show()

# build_gui()

# #********************************************
# # Simple pygame program
# #********************************************
# import pygame 
# def pygame_example(): 
  

#   pygame.init()
#   screen = pygame.display.set_mode([500, 500])

# # Fill the background with white
#   screen.fill((255, 255, 255))

# # Draw a solid blue circle in the center
#   pygame.draw.circle(surface = screen, color = (0, 0, 255), 
#                      center = (250, 250), radius = 75)

# # Update the display
#   pygame.display.update()

# # Run until the user asks to quit
#   running = True
#   while running:

#     # Did the user click the window close button?
#     events =  pygame.event.get()
#     for event in events :

#         if event.type == pygame.QUIT:          
#             running = False

#         elif event.type == pygame.MOUSEBUTTONUP:
#                 draw_circle(screen)
#                 pygame.display.update()  

# def draw_circle(screen):

#     pos = get_pos()
#     pygame.draw.circle(screen, (0,   0, 255), pos, 20)

# def get_pos():

#     return pygame.mouse.get_pos()


# pygame_example()


import numpy as np
from numpy import sin, pi, linspace, zeros, max, abs 
import soundfile as sf
import simpleaudio as sa
import matplotlib.pyplot as plt 

#import pretty_midi
# import mido
# from mido import MidiFile
# import mido.backends.rtmidi
# import rtmidi
# import music21

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


def basic_example(): 

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

   return file_name  


# Wav file with different harmonics 
wav_file = basic_example()
play_wav( wav_file )



# def create_piano_midi(note_name='C3', velocity=100, duration=2.0, file_name='piano_note.mid'):
      
#     # Crear un objeto PrettyMIDI
#       midi = pretty_midi.PrettyMIDI()
    
#     # Crear un instrumento de tipo piano (ID 0 en General MIDI)
#       piano_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
#       piano = pretty_midi.Instrument(program=piano_program)
    
#     # Convertir el nombre de la nota a número MIDI
#       note_number = pretty_midi.note_name_to_number(note_name)
    
#     # Crear una nota de piano
#       note = pretty_midi.Note(velocity=velocity, pitch=note_number, start=0, end=duration)
    
#     # Añadir la nota al instrumento
#       piano.notes.append(note)
    
#     # Añadir el instrumento al objeto PrettyMIDI
#       midi.instruments.append(piano)
    
#     # Guardar como archivo MIDI
#       midi.write(file_name)



# def play_midi(file_name):

# # open midi with musescore   
#   stream = music21.converter.parse(file_name)
#   stream.show("midi")






# # Grand piano note 
# create_piano_midi(note_name='C3', velocity=100, duration=2.0, file_name='piano_note.mid')

# # Nombre del archivo MIDI a reproducir
# play_midi('piano_note.mid')
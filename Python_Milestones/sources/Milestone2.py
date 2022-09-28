
from cmath import sqrt #complex math library 

def Roots_2th(): 

   print("Roots of a x**2 + b* x + c = 0 ")

   coef = input(" Enter coefficients a b c = ").split(" ")
   a, b, c = float (coef[0]), float (coef[1]), float (coef[2])
  
   if a==0 :
      if b==0 : 
             print("There is no solution " )
      else:
             print("There is only one solution x1 =", -c/b  )
   else: 

      x1 = ( - b + sqrt( b**2 - 4* a*c ) )/(2*a)
      x2 = ( - b - sqrt( b**2 - 4* a*c ) )/(2*a)

   print( " x1=", x1, "x2 =", x2) # output
   print( " x1=",  -2*c/( b + sqrt( b**2 - 4* a*c ) ) )

   print("\n")

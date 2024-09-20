

from Calculus import Series
from math import factorial

 
def a1(n): 
     
     return n

def a2(n): 
     
     return 2*n-1

def a4(n): 
     
     return 1 / 2**n

def a5(n): 
     
     return 1 / n**2

def a6(n): 
     
     return (-1)**(n+1) / 2**n


def a7(n): 
     
     return 1 / factorial(n)




def series_examples(): 

 while(1): 
          
       print( " ____________________________ ")   
       print( " 0:  exit        "                              )
       print( " 1:  sum n    N terms   "                       )
       print( " 2:  sum 2n-1 N terms "                         )
       print( " 3:  factorial N "                              )
       print( " 4:  sum 1/2**n infinite terms "                )
       print( " 5:  sum 1/n**2 infinite terms "                )
       print( " 6:  sum (-1)**(n+1)/2**n infinite terms "      )
       print( " 7:  sum 1 / n! infinite terms "                )
       k = int( input(" Enter series number: ") )
       
       if k==0:
           break 

       elif k==1: 
           N = int( input(" Enter number of terms N = ")) 
           SN = Series.Sigma_N(a1, 1, N) 

       elif k==2: 
           N = int( input(" Enter number of terms N = ")) 
           SN = Series.Sigma_N(a2, 1, N) 

       elif k==3: 
           N = int( input(" Enter number of terms N = ")) 
           SN = factorial(N)    

       elif k==4: 
           tolerance = float( input( " Enter tolerance = ") ) 
           SN = Series.Sigma( a4, 1, tolerance )

       elif k==5: 
           tolerance = float( input( " Enter tolerance = ") ) 
           SN = Series.Sigma( a5, 1, tolerance )

       elif k==6: 
           tolerance = float( input( " Enter tolerance = ") ) 
           SN = Series.Sigma( a6, 1, tolerance )

       elif k==7: 
           tolerance = float( input( " Enter tolerance = ") ) 
           SN = Series.Sigma( a7, 1, tolerance )

       else:  
          print( "  series is not implemented k=", k )
       
       print(" Sn = ", SN ) 

 

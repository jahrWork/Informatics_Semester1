

import pandas as pd
from numpy import shape, product, sum 
    
#******************************************************    
#   it reads a filename and save its data in matrix A 
#******************************************************
def load_matrix( filename ): 
     
    data = pd.read_csv(filename)

  # header 
    columns = data.columns.tolist()
    print(" header =", columns)

    return data.values 




A = load_matrix("./week by week/data.csv") 
print(" type of A: ", type(A))
         
# print row ith 
(N,M) = shape(A)
for i in range(0,N): 
  print( A[i,:] )

print( product(A) )  
print( sum( A, axis=0 ))                 
print( sum( A, axis=1 ))  
    
    





#***************************************************
# Implement Collatz function of natural number N 
#    a_{i+1} = f((a_i))
#    f(n) = n/2 if n is even or 3n+1 if n is odd
#    stop when a_i is 1. 
#***************************************************
# def f(n): 
    
#     if n % 2 == 0: 
#           return n//2 
     
#     else:
#           return 3*n + 1
     
# def collatz(N): 
    
#     a = [ N ]
 
#     i = 0 
#     while a[i] != 1:  
#         a += [ f( a[i] ) ]
#         i += 1 
        
#     return a 


# print("Collatz(7) =", collatz(7) )






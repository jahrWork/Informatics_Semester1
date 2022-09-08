
import pandas as pd
from numpy import shape
    
#   it reads a filename and save its data in matrix A 
def load_matrix( filename ): 

     
    data = pd.read_csv(filename)

  # header 
    columns = data.columns.tolist()
    print(" header =", columns)

    return data.values 


    
#   It allows to test the load matrix function 
def Test_load_matrix():  
    
    
         A = load_matrix('./data/data.csv') 
         
       # print row ith 
         for i in range( shape(A)[0] ): 
            print( [ round(a,2) for a in A[i] ])
                 
    
         A = load_matrix('./data/data2.csv') 
         
         for i in range( shape(A)[0] ): 
            print( [ round(a,2) for a in A[i] ])  #end
         
    
    
    
    


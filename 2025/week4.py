#***************************************************
#   Lists cmprehesion. Input/Output CSV and TXT 
#***************************************************




import pandas as pd
from numpy import shape, prod, sum, zeros 
    
#******************************************************    
#   it reads a filename and save its data in matrix A 
#******************************************************
# def load_matrix( filename ): 
     
#     data = pd.read_csv(filename)

#   # header 
#     columns = data.columns.tolist()
#     print(" header =", columns)

#     return data.values 


# A = load_matrix("./week by week/data.csv") 
# print("\n")
# print(" type of A: ", type(A))
# print(A)
         
# # print row ith 
# (N,M) = shape(A)
# for i in range(0,N): 
#   print( A[i,:] )

# print( prod(A) )  
# print( sum( A, axis=0 ))                 
# print( sum( A, axis=1 ))  
    
 
 
 #*******************************************
 # Open and read a file 
 # ******************************************  
f = open("./week by week/data.csv", "r")
content = f.read()
print(type(content) )
print( content) 


 #*******************************************
 # Do the same without pandas 
 #******************************************  
lines = content.split("\n")
print( lines[0] )
print(lines)
char_numbers = lines[1].split(",")
print( char_numbers )
number = float( char_numbers[0] ) 
print("number =", number)


A = zeros( (3,4) )
for i in range(len(lines)-1):
   char_numbers = lines[i+1].split(",")
   for j in range(len(char_numbers)): 
       A[i,j] = float( char_numbers[j] ) 

print( A )



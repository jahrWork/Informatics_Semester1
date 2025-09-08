#***************************************************
#   Lists cmprehesion. Input/Output CSV and TXT 
#***************************************************




S = "my name is John"
# print( S.split(" ") )

# for c in S: 
#     print("c = ", c)
   
# print("\nString referred by index")    
# for i in range(len(S)): 
#     print("c = ", S[i])
    

# print( " S[0] =",  S[0] ) 
# #S[0] = "M"
# S = "M" + S[1:]
# print(S)

# S = S.upper()  
# print(S)



# n = 123 #input("Enter number  ")
# Base10 = ""
# l = len(n)
# for i in range(l): 
#     Base10 = Base10 + n[i] + " * 10 **" + str( l-i-1 ) + " + "  
    
# print( n, " =", Base10)    


# Transform integer number to binary base 
# n = int(input("Enter number  "))
# n = 0 
# print( bin(n) )

# if n==0: bits = "0"
# else:    bits = ""
# while n > 0: 
#     bits =  str(n % 2) + bits 
#     n = n // 2 
    
    
# # Transform binary base to integer number 
# bits = "1100"  
# l = len(bits) 
# n = 0 
# for i in range(l): 
#      n = n + int( bits[i] ) * 2**(l-i-1)
#      print( " i=", i, " n = ", n)
     
# print ( "n = ", n )     


    

# print(bits)
# l = len(bits)

# Base2 = ""
# for i in range(l): 
#       Base2 = Base2 + bits[i] + " * 2 **" + str( l-i-1 ) + " + "  
    
# print( n, " =", Base2)    


# n = 123
# digits = ""
# D ="01"
# while n>0: 
#     digits =  D[n%2]  + digits 
#     print(digits)
#     n = n // 2
# print(digits)

# Base2 = ""
# l = len(digits)
# for i in range(l): 
#     Base2 = Base2 + " + " + digits[i] + " x 2^" + str(l-i-1) 
# print(Base2)  






# n = 123
# D ="0123456789"
# digits = ""
# while n>0: 
#     digits =  D[n%10]  + digits 
#     print(digits)
#     n = n // 10
# print(digits)

# Base10 = ""
# l = len(digits)
# for i in range(l): 
#     Base10 = Base10 + " + " + digits[i] + " x 10^" + str(l-i-1) 
# print(Base10)   






# D ="0123456789ABCDEFG"
# n = 123
# digits = ""
# while n>0: 
#     digits =  D[n%16]  + digits 
#     n = n // 16
#     print(digits, " n = ", n )
# print(digits)

# Base16 = ""
# l = len(digits)
# for i in range(l): 
#     Base16 = Base16 + " + " + digits[i] + " x 16^" + str(l-i-1) 
# print("digits =", digits)
# print(Base16) 



def digits(base, n): 

    if base == "binary": 
           D = "01"
           den = 2
    elif base == "decimal": 
           D = "0123456789"
           den = 10
    elif base == "hexa": 
           D = "0123456789ABCDEF"
           den = 16 
    else: 
        print("Error: not implemented base = ", base)
              
    digits = ""
    while n>0: 
      digits =  D[n%den]  + digits 
      n = n // den 
    
    Base = ""
    l = len(digits)
    for i in range(l): 
      Base = Base + " + " + digits[i] + " x "+ str(den)+"^" + str(l-i-1) 

    return digits, Base
 


n = 123
d, B = digits("hexa", n) 
print("digits = ", d,  " Representation =", B)

d, B = digits("decimal", n) 
print("digits = ", d,  " Representation =", B)

d, B = digits("binary", n) 
print("digits = ", d,  " Representation =", B)



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

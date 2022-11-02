# S = "my name is John"
# print( S.split(" ") )

# for c in S: 
#     print("c = ", c)
   
# print("\nString referred by index")    
# for i in range(len(S)): 
#     print("c = ", S[i])
    

# # print( " S[0] =",  S[0] ) 
# # S[0] = "M"
# S = "M" + S[1:]
# print(S)

# S = S.upper()  
# print(S)



# n = input("Enter number  ")
# Base10 = ""
# l = len(n)
# for i in range(l): 
#     Base10 = Base10 + n[i] + " * 10 **" + str( l-i-1 ) + " + "  
    
# print( n, " =", Base10)    


# Transform integer number to binary base 
# n = int(input("Enter number  "))
n = 0 
print( bin(n) )

if n==0: bits = "0"
else:    bits = ""
while n > 0: 
    bits =  str(n % 2) + bits 
    n = n // 2 
    
    
# Transform binary base to integer number 
bits = "1100"  
l = len(bits) 
n = 0 
for i in range(l): 
     n = n + int( bits[i] ) * 2**(l-i-1)
     print( " i=", i, " n = ", n)
     
print ( "n = ", n )     


    

# print(bits)
# l = len(bits)

# Base2 = ""
# for i in range(l): 
#       Base2 = Base2 + bits[i] + " * 2 **" + str( l-i-1 ) + " + "  
    
# print( n, " =", Base2)    




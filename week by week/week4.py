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




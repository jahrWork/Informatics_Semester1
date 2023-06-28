from math import factorial 


N = 10
# N = int(  input("Enter N :") ) 
SN = 0 
for n in range(1,N+1): 
    
    print(n,  SN)
    # SN = SN + 1 / 2**n
#   print("n =", n, "factorial = ", factorial(n)  )
    SN = SN + n / ( 3**n  * factorial(n)  ) 
    
print("SN = ",SN, "N =", N)    


print( " ")

SN = 0 
f = 1 
for n in range(1,N+1): 
    
    print(n,  SN)
    # SN = SN + 1 / 2**n
    # f = 1 
    
    for i in range(1, n+1):
        f = f * i 
    print("n =", n, "factorial = ", f  )    
        
    SN = SN + n / ( 3**n  * f ) 
    
    
print("SN = ",SN, "N =", N)    



# S = 0 
# n = 1
# while 1/2**n > 1e-8:  
    
#     S = S + 1/2**n
    
#     print(n,  S)
    
#     n = n + 1  
    
   
    
# print("S = ",S, "n =", n-1) 


# def a(n): 
    
#     return 1/2**n 



# S = 0 
# n = 1
# while a(n) > 1e-8:  
    
#     S += a(n)
    
#     print(n,  S)
    
#     n = n + 1  
    
   
    
# print("S = ", S, " n = ", n-1)  
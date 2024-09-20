# Functions 
from numpy import array 



#***********************************************
# 0. ExampleS f: R -> R, f: R2 -> R, f: R2 -> R2  
#***********************************************
# def f1(x): 
    
#     return x**2 

# def f2(x, y): 
    
#     return x**2 + y**2 


# def f3(x): 
    
#     return array( [ x[1],  -x[0] ] )


# print( " f(2.) =", f1( 2. ) )
# print( " f(2.) =", f1( x = 2. ) )
# print( " f(2., 2.) =", f2(x  = 2, y = 2.) )
# print( " f( array( [1, 2]) =", f3( x = array([1, 2]) ) )


# L1 = [ 2, 5 ,7 ,3 ]
# L2 = [ 1, 2, 9, 10 ]

# L1.sort()
# print("L1 =", L1)
# print("L2 =", L2)

# U = set(L1) | set(L2)
# I = set(L1) & set(L2)

# print("shared elements =", list( set(L1) & set(L2) ) )
# print("not shared elements =", list( U - I  ) )

# def shared_elements(L1, L2): 
    
#     S = [ ]
#     for l1 in L1: 
#         if l1 in L2: 
#             S += [ l1 ] 
    
#     return S         
           
           
# def not_shared_elements(L1, L2): 
    
#     NS = [ ]
    
#     for l1 in L1: 
#         if l1 not in L2: 
#             NS += [ l1 ]
           
#     for l2 in L2: 
#         if l2 not in L1: 
#             NS += [ l2 ]  
            
#     return NS        
           
        
# print("shared elements =", shared_elements( L1, L2 ) )
# print("not shared elements =", not_shared_elements( L1, L2 ) )
    
    


# #***********************************************
# # 1. Determine a list of the first N primes 
# #***********************************************
# def is_prime(n): 
    
#       for i in range(2,n):
#           if n % i == 0:  
#             return False
         
#       return True and n > 1
        
    
   
# def First_primes(N): 

#   N_primes = 0 
#   n = 1   
#   primes = []
  
#   while N_primes < N: 
             
#         if is_prime(n): 
#             primes += [ n ]
#             N_primes += 1 
            
#         n += 1    
   
#   return primes   
   
    
   
# print("First N primes =", First_primes(7) )     


          
      

# #***********************************************
# # 2. Determine a list of the first N perfects 
# # is_perfect: N -> (T,F)
# #***********************************************   
# def is_perfect(n): 
    
#       S = 0 
#       for i in range(1,n):
#           if n % i == 0:
#             S = S + i   
          
#       return S == n  
   
# def First_perfect_numbers(N): 

#   N_perfects = 0 
#   n = 1 
#   perfects = [ ]   
  
#   while N_perfects < N: 
             
#         if is_perfect(n): 
#             perfects += [ n ]
#             N_perfects = N_perfects + 1 
            
#         n = n + 1 
   
#   return perfects      
      

# print("First N perfect numbers =", First_perfect_numbers(4)  )   







# #***********************************************
# # 3. Functions with different number of arguments 
# #***********************************************  
# def divisors(n): 
    
#       d = []
#       for i in range(1,n):
#           if n % i == 0:
#             d += [ i ] 
          
#       return d  

 
# def greatest_common_divisor( *numbers ): 
    
#       common_divisors = set (divisors( numbers[0] ) ) 

#       for i  in range(1, len(numbers)):  
#           D = set( divisors( numbers[i] ) ) 
#           common_divisors &= D 
              
#       return max(common_divisors)


# def common_elements(A, B): 

#       C = []
#       for a in A: 
#           if a  in B: 
#                   C += [ a ] 

#       return C  


# def greatest_common_divisor2( *numbers ): 
    
#       common_divisors = divisors( numbers[0] ) 

#       for i  in range(1, len(numbers)):  
#           D = divisors( numbers[i] )
#           common_divisors = common_elements( common_divisors, D)
     
#       return max(common_divisors)
 
# print(" GCD = ", greatest_common_divisor(24, 30, 72) ) 
# print(" GCD = ", greatest_common_divisor2(24, 30, 72) ) 



#***********************************************
# 4. Remove index position 
#***********************************************  
# def remove_index(L, i): 

    
#     S = L[:]
#     S.sort()

#     if i< len(L)+1: 
#           del S[i-1]

#     return S 

# L = [ 2.3, 1.4, 9.1, -2.2, 7.0, 43.2 ]
# print(" L = ",  L) 
# print(" remove = ",  remove_index(L, 3) ) 



#***********************************************
# 5. Differences = Union - Intersection  
#***********************************************  
# def diff(L1, L2): 

    
#     U = set(L1) | set(L2)
#     I = set(L1) & set(L2) 

#     return list( U - I )

# def diff2(L1, L2): 
    
#     L = [] 
#     for l1 in L1: 
#         if l1 not in L2: 
#             L += [l1] 

#     for l2 in L2: 
#         if l2 not in L1: 
#             L += [l2] 
   
#     return L

# L1 = [1,3,5,7,9]
# L2 = [1,2,3,4,5]
# print( " L1 =", L1, " L2 =", L2) 
# print(" diff = ", diff(L1, L2) ) 
# print(" diff = ", diff2(L1, L2) )



# #***********************************************
# # 6. Polynomial evaluation  
# #***********************************************  
# def polynomial(x, a): 

#     P = 0 
#     for i in range(len(a)): 
#         P  = a[i] * x**i 

#     return P 

 
# print(" polynomial = ", polynomial( x=2, a=[1, 2, 3] ) ) 


#***********************************************
# 7. Intersection  
#***********************************************  
# def shared_letters(S1, S2): 
    
#     return list( set(S1) & set(S2) ) 

# def intersection(S1, S2): 
    
#     return  [ s1 for s1 in list(S1) if s1 in list(S2)]

# print(" shared letters = ", shared_letters( "melon","jamón" ) )
# print(" shared letters = ", intersection( "melon","jamón" ) ) 

# #***********************************************
# # 8. Roots   
# #***********************************************  
# def roots(a, b, c): 
    
#     from cmath import sqrt 

#     x1 = ( - b + sqrt(b**2 -4*a*c) )/(2*a)
#     x2 = ( - b - sqrt(b**2 -4*a*c) )/(2*a)

#     if x1.imag != 0 : 
#        return [ [x1.real, x1.imag], [x2.real, x2.imag] ] 

#     elif x1.real == x2.real: 
#        return [ x1.real ]

#     else : 
#        return [ x1.real, x2.real ] 


# print( "roots =", roots(1,2,3))
# print( "roots =", roots(1,-2,1))
# print( "roots =", roots(1,-4,1))

#if __name__ == "__main__" : 

   

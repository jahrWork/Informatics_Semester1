
from numpy import array

# **********************************************************************
# Examples of sets, lists, tuples, dictionaries, vectors and matrices
# ***********************************************************************

# # sets
# S = {"Juan", 1, 5., 1}
# print(type(S), S)

# # tuples
# T = ("Juan", 1, 5., "Juan")
# # T[3] = "Lucia" # ERROR
# print(type(T), T, " T[0]=", T[0])

# # lists
# L = ["Juan", 1, 5., "Juan"]
# L[3] = "Lucia"
# print(type(L), L, " L[0]=", L[0])

# # dictionaries
# D = {"Juan": "DNI 1234", "Lucia": "DNI 5678"}
# print(type(D), D)

# for i, key in enumerate(D):
#     print("index in dictionary =", i, "key =", key, "value=", D[key])

# #vectors and matrices
# v = array( [1, 2, 3] )
# print(type(v), v)


# ***********************************************
# Operations with  lists
# ***********************************************

# L1 = [1, 2, 3]
# L2 = [4, 5, 6]

# print("L1 + L2 = ", L1 + L2)
# print("2 * L1 = ", 2 * L1)

# L1.insert(0, 2)  # insert 2 at position i=0
# print("new list L1 =", L1)
# L1.remove(3)    # remove value = 3 from list
# print("new list L1 =", L1)

# n = L1.count(2)

# print("new list L1 =", L1, "number of 2 =", n)

# L3 = L1[0:2]   # L3 = [ 2]

# print("new list L3= L1[0:1] = ", L3)
# print("index of 1 in L1 =", L1.index(1))
# print("max(L1) = ", max(L1), " min(L1) =", min(L1), "len(L1) =", len(L1))
# print("sum(L1) = ", sum(L1))

# S = 0
# for e in L1: # for all element in list L1
#     S += e  # S = S + e
# print("Sum(L1) =", S)

# *********************************************************
# Operations with  Tuples
# Since they are inmutable, insert or remove are not allowed
# *********************************************************

# T1 = (1, 2, 3)
# T2 = (4, 5, 6)

# print("T1 + T2 = ", T1 + T2)
# print("2 * T1 = ", 2 * T1)

# n = T1.count(2)

# print("number of 2 =", n)

# T3 = T1[0:1]

# print("new tuple T3= T1[0:1] = ", T3)
# print("index of 1 in T1 =", T1.index(1))
# print("max(T1) = ", max(T1), " min(T1) =", min(T1), "len(T1) =", len(T1))
# print("sum(T1) = ", sum(T1))

# *********************************************************
# Operations with  Vectors
# Since Python is not a vectorial language, numpy is used
# to overcome this limitation
# *********************************************************

# V1 = array([1, 2, 3])
# V2 = array([4, 5, 6])

# print("V1 + V2 = ", V1 + V2)
# print("2 * V1 = ", 2 * V1)


# V3 = V1[0:1]
# print(" type of V3 ", type(V3))

# print("new vector V3= V1[0:1] = ", V3)
# print("max(V1) = ", max(V1), " min(V1) =", min(V1), "len(V1) =", len(V1))
# print("sum(V1) = ", sum(V1))

# M = array( [ [1,2], [3,4] ] )
# print("M = ", M[0,0], M[0, 1] )
# print(" first row of M = ", M[0,:])
# print(" first column of M = ", M[:,0])
          


# ***************************************************************
#  Remove the second smallest of a list
# ***************************************************************
# L = [2, 3, 4, 5, 6, 2, 1, -3, 7]
# L1 = L # L[:]  # WARNING cloning not alias L1 = L
# print(" L =", L, "\n L1 =", L1)
# m1 = min(L1)
# print(" m1 = ", m1)
# L1.remove(m1)
# m2 = min(L1)
# print(" m2 = ", m2)

# print("Remove the second smallest of :")
# print("L =", L)
# L.remove(m2)
# print("new list = ", L)



#***************************************************************
# Obtain the differences between two lists
#***************************************************************
# L1 = [1, 2, 3, 4]
# L2 = [2, 3, 4, 5, 6, 2, 7]
# print("L1 =", L1)
# print("L2 =", L2)
# print("set(L1) =", set(L1))
# print("set(L2) =", set(L2))

# Union = set(L1) | set(L2)
# print("Union L1 L2 =", Union)

# Intersection = set(L1) & set(L2)
# print("Intersection L1 L2 =", Intersection)

# diff = list(Union - Intersection)

# print("diff = ", diff)



#***************************************************
#  Write a function to return:  
#   a list of shared elements and 
#   a list of not shared elements 
#***************************************************
# def shared_and_differents(L1,L2): 
     
#      U = set(L1) | set(L2)
#      I = set(L1) & set(L2)

#      return list(I), list( U - I)

# L1 = [ 2, 5 ,7 ,3 ]
# L2 = [ 1, 2, 9, 10 ]
# print("shared elements and no shared =", shared_and_differents(L1,L2) )



# def shared_elements(L1, L2): 
    
#      S = [ ]
#      for l1 in L1: 
#          if l1 in L2: 
#             S += [ l1 ] 
    
#      return S         
           
         
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
    
 


#***********************************************
#  Shared letters in two strings 
#***********************************************  
# def shared_letters(S1, S2): 
    
#     return list( set(S1) & set(S2) ) 

# def shared_letters2(S1, S2): 
    
#     return  [ s1 for s1 in list(S1) if s1 in list(S2)]

# print( "list =", list("melon"))
# print( "set =", set("melon"))
# print(" shared letters = ", shared_letters( "melon","jamón" ) )
# print(" shared letters = ", shared_letters2( "melon","jamón" ) ) 


L = [2, 6, 2, 1, -3, 7]
a = 1 
b = 4 
print(L) 
n = 0
for l in L:
    if l >= a and l <= b:
         n += 1
print("n = ", n)



# ***************************************************************
# Count elements of a list |e| in [a, b]
# ***************************************************************
# def count_in_a_b1( L, a, b ): 
  
#   n = 0
#   for l in L:
#     if l >= a and l <= b:
#         n += 1

#   return n 
  

# L1 = [2, 6, 2, 1, -3, 7]

# print("Number of elements of  L=", L1,  "in [1, 4]:", 
#        count_in_a_b1( L = L1, a=1, b=4))


# def count_in_a_b( L, a, b ): 

#    return  [l for l in L if a >= l <= b]



# print("Number of L in [a,b]=", count_in_a_b( L = [1, 2, 3, 4,5 ], a = 1, b = 4 )) 



#************************************
#  palindrome 
#************************************
# def is_palindrome1(S): 
    
#  S1 = S.replace(" ", "")
#  print("S1 =", S1)
#  P = S1[::-1]
#  #print( "reversed =",  S[2:-1:-1]) # WARNING: it does not work 
#  print("S =", S1, "P =", P)

#  if P == S1:
#       return True 


# S = "somos o no somos"     
# print("S =", S, " is palindrome: ", is_palindrome1(S))






# def is_palindrome(S): 

#    S = S.lower()
#    S = S.replace(" ", "")
#    print(S)

#    vowels = [("á", "a"), ("é", "e"), ("í", "i"), ("ó", "o"), ("ú", "u")]

#    count = []
#    for (a, v) in vowels:
#      S = S.replace(a, v)
#      count = count + [S.count(v)]

#    print("Number of vowels =", count)
#    P = S[::-1]
#    print(" S =", S)
#    print(" P =", P)

#    if P == S:
#      return True 

# S = "Dábale arroz a la zorra el abad"
# print("S =", S, " is palindrome: ", is_palindrome(S))




 
# #***********************************************
# # divisors of a number  
# #***********************************************  
# def divisors(n): 
    
#       d = []
#       for i in range(1,n):
#           if n % i == 0:
#             d += [ i ] 
          
#       return d  

# print(" divisors of 15 : ", divisors(15) )

# #***********************************************
# # Greatest common divisor of different numbers 
# #  Functions with different number of arguments 
# #***********************************************  
# def greatest_common_divisor( *numbers ): 
    
#       common_divisors = set( divisors( numbers[0] ) ) 

#       for i  in range(1, len(numbers)):  
#           D = set( divisors( numbers[i] ) ) 
#           common_divisors &= D 
              
#       return max(common_divisors)

# print(" GCD(24,30,72) = ", greatest_common_divisor(24, 30, 72) ) 
# from math import gcd 
# print(" gcd(24,30,72) = ", gcd(24, 30, 72) ) 




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
 

# print(" GCD = ", greatest_common_divisor2(24, 30, 72) ) 


 




            
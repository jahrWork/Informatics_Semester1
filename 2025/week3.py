#***************************************************
#   Lists, tuples, dictionaries and sets  
#***************************************************



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
# #  Determine a list of the first N perfects 
# #***********************************************
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
# Obtain the differences between two lists without functions 
#***************************************************************
# List_1 = [1, 2, 3, 4]
# List_2 = [2, 3, 4, 5, 6, 2, 7]
# print("List_1 =", List_1)
# print("List_2 =", List_2)
# print("set(List_1) =", set(List_1))
# print("set(List_2) =", set(List_2))

# Union = set(List_1) | set(List_2)
# print("Union List_1 List_2 =", Union)

# Intersection = set(List_1) & set(List_2)
# print("Intersection List_1 List_2 =", Intersection)

# diff = list(Union - Intersection)
# print("diff = ", Union - Intersection)
# print("diff = ", diff)

# Once the algorithm is clear, 
# we try to encapsule the code into a function:
# def shared_and_differences( L1, L2 ) 
# note that the name of arguments has nothing to do with 
# the names of the lists when this function is used


#***************************************************
# Write a function to  differenciate between 
# common and diferent elements of two lists
# input: 
#        L1 : list 
#        L2 : list 
# return:  
#   a list of shared elements and 
#   a list of not shared elements 
#***************************************************
# def shared_and_differents(L1, L2): 
     
#      U = set(L1) | set(L2)
#      I = set(L1) & set(L2)

#      return list(I), list( U - I)

# List_a = [ 2, 5 ,7 ,3 ]
# List_b = [ 1, 2, 9, 10 ]
# print("shared elements and no shared =", 
#        shared_and_differents(L1 = List_a,L2 = List_b ) )

# print("shared elements and no shared =", 
#        shared_and_differents(List_a,List_b ) )



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
#  accented vowels and different  
#*********************************************** 
# L1 = list("melon")
# S1 = set("melon") 
# S2 = set("jamón") 
# print( "list =", L1)
# print( "set 1 =", S1)
# print( "set 2 =", S2)

# print( " intersection set(S1) & set(S2) =", S1 & S2 )


# def shared_letters(S1, S2): 
    
#     return list( set(S1) & set(S2) ) 

# def shared_letters2(S1, S2): 
    
#     return  [ s1 for s1 in list(S1) if s1 in list(S2)]


# print(" shared letters = ", shared_letters( "melon","jamón" ) )
# print(" shared letters = ", shared_letters2( "melon","jamón" ) ) 



# ***************************************************************
# Count elements of a list |e| in [a, b]
# ***************************************************************


# L1 = [2, 6, 2, 1, -3, 7]
# a = 1 
# b = 4 
# print(L1) 
# n = 0
# for l in L1:
#     if l >= a and l <= b:
#          n += 1
# print("n = ", n)


# def count_in_a_b1( L, a, b ): 
  
#   n = 0
#   for l in L:
#     if l >= a and l <= b:
#         n += 1

#   return n 


# def count_in_a_b( L, a, b ): 

#    return  len( [e for e in L if e >= a and e <= b] )
  
# L1 = [2, 6, 2, 1, -3, 7]

# print("Number of elements of  L=", L1,  "in [1, 4]:", 
#        count_in_a_b1( L = L1, a=1, b=4))

# print("Number of elements of  L=", L1,  "in [1, 4]:", 
#        count_in_a_b1( [2, 6, 2, 1, -3, 7], 1, 4))


# print("Number of L in [a,b]=", 
#        count_in_a_b( L = [1, 2, 3, 4,5 ], a = 1, b = 4 )) 



















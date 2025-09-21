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



#***************************************************
# sum of numeric series with a list 
#***************************************************
def a(n): 
    return 1/2**n 

N = 10
SN = sum( [ a(i) for i in range(1,N+1)] ) 
print(" SN = ", SN)

def sum_series(a, i0, N): 
    
    return sum( [ a(i) for i in range(i0, N+1)] ) 

print(" SN = ", sum_series(a, i0=1, N=10))









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



#************************************
#  palindrome 
#************************************
# Reserve a string 
S = "abc" 
print(S[::-1])
print(S[len(S)-1:-1:-1]) # it does not work 
print("S =", S[len(S)-1:0:-1] + S[0] ) # it does  work 
L = [S[e] for e in range(len(S)-1, -1, -1) ]
print(L, "".join(L) )


# S = "somos o no somos"
 
# S1 = S.replace(" ", "")
# print("S1 =", S1)

# P = S1[::-1]
#  #print( "reversed =",  S[2:-1:-1]) # WARNING: it does not work 
# print("S =", S1, "P =", P)

# if P == S1:
#   print(" is palindrome :", True )





# def is_palindrome1(S): 
    
#  S1 = S.replace(" ", "")
#  P = S1[::-1]

#  if P == S1:
#       return True 
#  else:
#       return False

# print("S  is palindrome: ", 
#       is_palindrome1( S = "somos o no somos" )  )






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
#    else: 
#      return False

# S = "Dábale arroz a la zorra el abad"
# print("S =", S, " is palindrome: ", is_palindrome(S))




 
#***********************************************
# divisors of a number  n
#***********************************************  
# def divisors(n): 
    
#       d = []
#       for i in range(1,n):
#           if n % i == 0:
#             d += [ i ] 
          
#       return d  

# print(" divisors of 15 : ", divisors(15) )

#***********************************************
# Greatest common divisor of different numbers 
#  Functions with different number of arguments 
#***********************************************  
# def greatest_common_divisor( *numbers ): 
    
#       common_divisors = set( divisors( numbers[0] ) ) 
#       print("number =", numbers[0], " common divisors =", common_divisors)

#       for i  in range(1, len(numbers)):  
#           D = set( divisors( numbers[i] ) ) 
#           print("number =", numbers[i], " D =", D)
#           common_divisors &= D 
#           print(" common divisors =", common_divisors)
#           input("press enter")
              
#       return max(common_divisors)

# print(" GCD(24,30,72) = ", greatest_common_divisor(24, 30, 72) ) 
# from math import gcd 
# print(" gcd(24,30,72) = ", gcd(24, 30, 72) ) 


# def greatest_common_divisor2( n1, n2 ): 
    
#       D1 = set( divisors( n1 ) ) 
#       print("number =", n1, " D1 =", D1)
 
#       D2 = set( divisors( n2 ) ) 
#       print("number =", n2, " D2 =", D2)

#       common_divisors = D1 & D2  
#       print(" common divisors =", common_divisors)
#       input("press enter")
              
#       return max(common_divisors)




# print(" GCD(24,30) = ", greatest_common_divisor(24, 30) ) 
# print(" GCD(24,30) = ", greatest_common_divisor2(24, 30) ) 



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







# Dictionaries


# ********************************************
#  1. Remove duplicates with dictionaries
# ********************************************

# S = "This is a list"
# S = S.replace(" ", "")
# print(" S = ", S)
# L = list(S)
# print(" L = ", L)

# D = dict.fromkeys(L)
# print(" D = ", D)

# L1 = list(D)
# print(" L1 = ", L1)
# S1 = "".join(L1)
# print(" S1 = ", S1)


# # Equivalent to
# S2 = ""
# for l in L1:
#     S2 += l  # S2 = S2 + l
# print("S2 =", S2)



# ****************************
# 3. merging dictionaries
# ****************************

# A = {"a": 1, "b": 1}
# B = {"b": 2, "c": 1}
# print("A =", A)
# print("B =", B)


# C = A.copy()  # cloning
# # C = A  # alias
# # C = A[:] not possible
# print("C=", C)
# print("A=", A)


# print("C=", C)
# C.update(B)  # merge c and b
# print("C=", C)
# print("A=", A)


# ************************************
#  4. count different letters with dictionaries
# ************************************
# S = "There are 9 letters:e in this sentence"
# L = list(S)
# print(" L =", L)
# D = {}

# for letter in L:

#     if letter in D:

#         D[letter] += 1

#     else:

#         D[letter] = 1

# print(D)
# print("Number of e:", D["e"])


# #*************************************
# #  5. count words with dictionaries
# #*************************************
#S = "over and over again. The word over appears in this sentence 3 times"
# S = "over and over again. The word over appears in this sentence 3 times"
# L = list(S.split(" "))

# print(" L = ", L)

# # L1 = L[:]
# # for word in L:

# #     if word == "":
# #         L1.remove(word)

# print(" L = ", L)
# D = {}

# for word in L:

#     if word in D:

#         D[word] += 1

#     else:

#         D[word] = 1

# print(D)


# #*****************************************
# # 6. Graphs by means of dictinaries
# #*****************************************

# graph = { "n1" : [ "n2", "n3" ],
#           "n2" : [ "n1", "n4" ],
#           "n3" : [ "n5" ],
#           "n4" : [ "n2" ],
#           "n5" : ["n3", "n2" ]
#         }
# print(" graph =", graph)


# nodes = [ "n1", "n2", "n3", "n4", "n5"  ]
# edges = [ ("n1", "n2"), ("n1", "n3"),  ("n2", "n4"),   ("n2", "n1"),
#           ("n3", "n5"), ("n4", "n2"),  ("n5", "n3"),   ("n5", "n2") ]

# print("nodes =", nodes)
# print("edges =", edges)
# print("")
# #print("edges =", edges)

# g = {}

# for n in nodes:

#       g[n] = []


# print(" g = ", g)


# for n in nodes:
#     for (v1, v2) in edges:

#         if n == v1:
#             g[n] += [ v2 ]

# print(" g = ", g)


# Example1:  https://github.com/OfirKP/Whatsapp-Net

# Example:   https://tuangauss.github.io/projects/networkx_basemap/networkx_basemap.html




#********************************************************
# 7. Count the frequency of words in the lyrics of a song
#********************************************************
# lyrics_hit_the_road_jack = """
# Hit the road Jack and don't you come back
# No more, no more, no more, no more
# Hit the road Jack and don't you come back no more
# What you say?
# Hit the road Jack and don't you come back
# No more, no more, no more, no more
# Hit the road Jack and don't you come back no more
# Old woman, old woman, don't treat me so mean
# You're the meanest old woman that I've ever seen
# I guess if you said so
# I'll have to pack my things and go (that's right)
# Hit the road Jack and don't you come back
# No more, no more, no more, no more
# Hit the road Jack and don't you come back no more
# What you say?
# Hit the road Jack and don't you come back
# No more, no more, no more, no more
# Hit the road Jack and don't you come back no more
# Now baby, listen baby, don't ya treat me this way
# 'Cause I'll be back on my feet some day
# (Don't care if you do 'cause it's understood)
# (You ain't got no money, you just ain't no good)
# Well, I guess if you say so
# I'll have to pack my things and go (that's right)
# Hit the road Jack and don't you come back
# No more, no more, no more, no more
# Hit the road Jack and don't you come back no more
# What you say?
# Hit the road Jack and don't you come back
# No more, no more, no more, no more
# Hit the road Jack and don't you come back no more
# Well (don't you come back no more)
# Uh, what you say? (Don't you come back no more)
# I didn't understand you (don't you come back no more)
# You can't mean that (don't you come back no more)
# Oh, now baby, please (don't you come back no more)
# What you tryin' to do to me? (Don't you come back no more)
# Oh, don't treat me like that (don't you come back no more)
# """


# lyrics = lyrics_hit_the_road_jack.lower()
# eliminate = ["(", ")", "," ]
# #eliminate = ["(", ")", ",", "'" ]


# print("lyrics with CR=", lyrics)
# lyrics = lyrics.replace("\n", " ")
# print("lyrics without CR=", lyrics)

# for e in eliminate:
#     lyrics = lyrics.replace(e, "")
# print("\n \n lyrics without ( ) , =", lyrics)

# words = lyrics.split(" ")
# print("\nwords =", words)
# words.remove("")
# words.remove("")

# print("words =", words)

# different_words = []
# frequency = []
# for w in words:

#     if w in different_words:
#         i = different_words.index(w)
#         frequency[i] += 1
#     else:
#         different_words += [w]
#         frequency += [1]

# print("\n different_words =", different_words)
# print("\n frequency =", frequency)
# exit()

# m = max(frequency)
# print( "max =",  m )
# i = frequency.index(m)
# print( " word with max frequency:", different_words[i])




# dictionary = dict()
# for w in words: 
#     if w not in dictionary: 
#          dictionary[w] = 1 
#     else: 
#          dictionary[w] += 1 

# print("dictionary =", dictionary)

# print(" word with max frequency", max(dictionary, key = dictionary.get ) ) 

# # List of words ordered by frequency 
# sorted_words =  sorted(dictionary, key = dictionary.get) 

# sorted_words.reverse()

# for w in sorted_words: 
#      print( w, dictionary[w] )



#****************************************************************
# Find if a substring: s is inside a string: S
# Return a list containing the indexes of S where the substring s begins 
# Example: S = "1234561234", find s="34". Return [2, 8]
#****************************************************************

# S = "1234561234"
# s="34"
# i = S.find(s) 
# print( " i = ", i)

# i = S.find(s, i+1) 
# print( " i = ", i)

# i = S.find(s, i+1) 
# print( " i = ", i)


# def find_substring(s, S): 

#    index = []
#    i = -1 
#    while  i<len(S)-1: 
#       i = S.find(s, i+1) 
#       if i>=0: 
#         index += [i] 
#       else:
#         break

#    if index == []:
#        index += [ S.find(s) ]
#    return index 

# print( find_substring(s="34", S = "1234561234" ) )
# print( find_substring(s="34567", S = "123345671234567" ) )

#****************************************************************
# Determine the largest substring starting at first position 
# in S and a list of indexes where the substring begins in S.
# Example: S = "123345671234567",  Return "123",  [0, 8]
#****************************************************************
# def largest_substring(S): 

#   patterns = dict()
#   j = 0 
#   for i in range(j+1,len(S)-1):
#          s = S[j:i+1]  
#          index = find_substring(s, S)
#         # print("s =", s, index)
#          if sum(index) > 0: 
#                   patterns[s] = index

#   print(patterns)
#   max_key ="" 
#   for key in patterns: 
#     if len(key) > len(max_key): 
#       max_key = key 
 
#   if max_key =="": 
#       return "", []
#   else: 
#       return max_key, patterns[max_key]   
  
# print( largest_substring(S = "123345671234567") )


#****************************************************************
# Split a given string S into the largest substrings which appears of S.
# Return a list of substrings and a list of list  where the substrinf begins in S. 
# Example: S = "123345671234567",  Return ["123","34567", "12" ] [ [0, 8], [3, 10], [] ]
#****************************************************************
# def split_into_substrings(S): 
    
#     S1 = S 
#     S_split = []
#     index = []

#     while len(S1) > 0: 
#       s1, i1 = largest_substring(S1) 
#       print("s1 =", s1, i1)
      
#       if s1=="":
#              S_split += [S1]
#              print("S1 =", S1, "find ", find_substring(S1, S))
#              index += [find_substring(S1, S)]
#              print("index =", index)
#              break 
#       else: 
#           S_split += [s1]
#           index += [ find_substring(s1, S) ]
#           S1 = S1.replace(s1, "")
      
      

#     return S_split, index   

# print( split_into_substrings("123345671234567")) 
# print( split_into_substrings("123+3+4567+123+4567")) 





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
















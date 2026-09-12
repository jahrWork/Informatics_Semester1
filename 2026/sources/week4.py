




#***************************************************
#   Lists comprehesion. Input/Output CSV and TXT and Sympy (week4.ipynb) 
#***************************************************




import pandas as pd
from numpy import shape, prod, sum, zeros 
    
#******************************************************    
#   it reads a filename and save its data in matrix A 
#******************************************************
def load_matrix( filename ): 
     
    data = pd.read_csv(filename)

  # header 
    columns = data.columns.tolist()
    print(" header =", columns)

    return data.values 


A = load_matrix("./2025/data.csv") 
print("\n")
print(" type of A: ", type(A))
print(A)
         
# # print row ith 
# (N,M) = shape(A)
# for i in range(0,N): 
#   print( A[i,:] )

# print( prod(A) )  
# print( sum( A, axis=0 ))                 
# print( sum( A, axis=1 ))  
    
  

#*******************************************
# Do the same without pandas 
#******************************************    
 
 
 #*******************************************
 # Open and read a file 
 # ******************************************  
f = open("./2025/data.csv", "r")
content = f.read()
print(type(content) )
print( content) 

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

print( type(A), A )

print(  A )


#***************************************************
# sum of numeric series with a list 
#***************************************************
# def a(n): 
#     return 1/2**n 

# N = 10
# SN = sum( [ a(i) for i in range(1,N+1)] ) 
# print(" SN = ", SN)

# def sum_series(a, i0, N): 
    
#     return sum( [ a(i) for i in range(i0, N+1)] ) 

# print(" SN = ", sum_series(a, i0=1, N=10))


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
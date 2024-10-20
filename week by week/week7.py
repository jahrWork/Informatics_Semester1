
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
# for e in L1:
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


# #***************************************************************
# # 1. Partition of segment [a, b] in N intervals.
# # Determine interior nodes x_i = a + (b-a)/N i from i=0 to i=N
# #***************************************************************
# N = 5
# a, b = 0., 1.
# x = array([a + (b-a)/N * i for i in range(0, N+1)])
# print(" x =", x)
# print(" type of x =", type(x))


# #***************************************************************
# # 2. Obtain the differences between two lists
# #***************************************************************
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


# ***************************************************************
# 3. Remove the second smallest of a list
# ***************************************************************
# L = [2, 3, 4, 5, 6, 2, 1, -3, 7]
# L1 = L[:]  # WARNING cloning not alias L1 = L
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


# ***************************************************************
# 4. Count elements of a list |e| in [a, b]
# ***************************************************************
# L = [2, 3, 4, 5, 6, 2, 1, -3, 7]
# (a, b) = (1, 4)

# n = 0
# for l in L:
#     if l >= a and l <= b:
#         n += 1
# print("Number of L in [a,b]=", [a, b])
# print(" L = ", L)
# print("n =", n)

# L1 = [l for l in L if b >= l >= a]
# print("L1 =", L1, "n=", len(L1))


# ************************************************************
# 5. Even though lists are not vectors,
# lists can be used to perform vector operations.
# Calculate the dot product of two lists(vectors)
# ************************************************************
# U = [ 1, 2, 3 ]
# V = [ 4, 5, 6 ]
# dot = 0
# for i in range(len(U)):
#     dot += U[i]* V[i]  # dot = dot + U[i]*V[i]
# print("U=", U, "V =", V)
# print(" dot_product(U,V) =", dot)


# #************************************
# #  6. palindrome and count vowels
# #************************************

# S = "somos o no somos"
# S1 = S.replace(" ", "")
# print("S1 =", S1)
# P = S1[::-1]
# print("S =", S1, "P =", P)
# if P == S1:
#     print("S =", S, " is palindrome")


# print("*************")
# S = "Dábale arroz a la zorra el abad"
# print(S)
# S = S.lower()
# print(S)
# S = S.replace(" ", "")
# print(S)

# vowels = [("á", "a"), ("é", "e"), ("í", "i"), ("ó", "o"), ("ú", "u")]

# count = []
# for (a, v) in vowels:
#     S = S.replace(a, v)
#     count = count + [S.count(v)]

# P = S[::-1]
# print(" S =", S)
# print(" P =", P)

# if P == S:
#     print("It is palindrome")

# print("Number of vowels =", count)


# #********************************************************
# # 7. Count the frequency of words in the lyrics of a song
# #********************************************************
lyrics_hit_the_road_jack = """
Hit the road Jack and don't you come back
No more, no more, no more, no more
Hit the road Jack and don't you come back no more
What you say?
Hit the road Jack and don't you come back
No more, no more, no more, no more
Hit the road Jack and don't you come back no more
Old woman, old woman, don't treat me so mean
You're the meanest old woman that I've ever seen
I guess if you said so
I'll have to pack my things and go (that's right)
Hit the road Jack and don't you come back
No more, no more, no more, no more
Hit the road Jack and don't you come back no more
What you say?
Hit the road Jack and don't you come back
No more, no more, no more, no more
Hit the road Jack and don't you come back no more
Now baby, listen baby, don't ya treat me this way
'Cause I'll be back on my feet some day
(Don't care if you do 'cause it's understood)
(You ain't got no money, you just ain't no good)
Well, I guess if you say so
I'll have to pack my things and go (that's right)
Hit the road Jack and don't you come back
No more, no more, no more, no more
Hit the road Jack and don't you come back no more
What you say?
Hit the road Jack and don't you come back
No more, no more, no more, no more
Hit the road Jack and don't you come back no more
Well (don't you come back no more)
Uh, what you say? (Don't you come back no more)
I didn't understand you (don't you come back no more)
You can't mean that (don't you come back no more)
Oh, now baby, please (don't you come back no more)
What you tryin' to do to me? (Don't you come back no more)
Oh, don't treat me like that (don't you come back no more)
"""


lyrics = lyrics_hit_the_road_jack.lower()
eliminate = ["(", ")", "," ]
#eliminate = ["(", ")", ",", "'" ]


print("lyrics with CR=", lyrics)
lyrics = lyrics.replace("\n", " ")
print("lyrics without CR=", lyrics)

for e in eliminate:
    lyrics = lyrics.replace(e, "")
print("\n \n lyrics without ( ) , =", lyrics)

words = lyrics.split(" ")
print("\nwords =", words)
words.remove("")
words.remove("")

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


dictionary = dict()
for w in words: 
    if w not in dictionary: 
         dictionary[w] = 1 
    else: 
         dictionary[w] += 1 

print("dictionary =", dictionary)

print(" word with max frequency", max(dictionary, key = dictionary.get ) ) 

# List of words ordered by frequency 
sorted_words =  sorted(dictionary, key = dictionary.get) 

sorted_words.reverse()

for w in sorted_words: 
     print( w, dictionary[w] )
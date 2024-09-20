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


# *****************************************
# 2. Remove duplicates with sets
# *****************************************

# S = "This is a list"
# S = S.replace(" ", "")
# B = set(S)
# print(" B =", B)
# L = list(S)
# A = set(L)

# C1 = ""
# for e in A:
#     C1 += e

# C2 = ""
# for e in B:
#     C2 += e

# print(" L = ", L)
# print(" A = ", A)
# print(" C1 = ", C1)
# print(" C2 = ", C2)


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
#  4. count letters with dictionaries
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
#S = "over     and over again. The word over appears in this sentence 3 times"
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
# # 6. Graphs by means of dictoinaries
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

# S = "Hello"
# for i,c  in enumerate(S):
#     print("index i in string S =", i, " S[i] = ", S[i], " character in S = ", c )

# L = [ 11, 22, 33, 44 ]
# for i,e  in enumerate(L):
#     print("index i in list L =", i, " L[i] = ", L[i], " element in L = ", e )

# for e  in L:
#     print( " element in L = ", e )


def a(n): 
    return 1/2**n 

def a1(n): 
    return 1/n**2 

# N = 10
# SN = sum( [ a(i) for i in range(1,N+1)] ) 
# print(" SN = ", SN)

# SN = 0
# for n in range(1,N+1): 
#     SN = SN + a(n)
# print(" SN = ", SN)

# S = 0; SN = 1
# n = 1
# while S != SN :
#    SN = S 
#    S = S + a(n)
#    print("n = ", n, " S = ", S, " S-SN =", S-SN, " a(n) = ", a(n) )
#    n = n + 1

def sum_N(N, a): 
    return sum( [ a(i) for i in range(1,N+1)] ) 

def sum_inf(a): 

    S = 0; SN = 1; n = 1
    while S != SN :
      SN = S 
      S = S + a(n)
      print("n = ", n, " S = ", S, "S-SN =", S-SN, "a(n) = ", a(n) )
      n = n + 1
      
    return S 

print("FINITE sum (a) = ", sum_N(10, a))
print("INFINITE sum (a) = ", sum_inf(a))

# from math import factorial


# N = 30
# # N = int(  input("Enter N :") )
# SN = 0
# for n in range(1, N+1):

#     print(n,  SN)
#     SN = SN + 1 / factorial(n)
# #   print("n =", n, "factorial = ", factorial(n)  )
#     # SN = SN + n / ( 3**n  * factorial(n)  )

# print("SN = ", SN, "N =", N)


# print( " ")

# SN = 0
# f = 1
# for n in range(1,N+1):

#     print(n,  SN)
#     # SN = SN + 1 / 2**n
#     # f = 1

#     for i in range(1, n+1):
#         f = f * i
#     print("n =", n, "factorial = ", f  )

#     SN = SN + n / ( 3**n  * f )


# print("SN = ",SN, "N =", N)


# # S = 0
# # n = 1
# # while 1/2**n > 1e-8:

# #     S = S + 1/2**n

# #     print(n,  S)

# #     n = n + 1


# # print("S = ",S, "n =", n-1)


# # def a(n):

# #     return 1/2**n


# # S = 0
# # n = 1
# # while a(n) > 1e-8:

# #     S += a(n)

# #     print(n,  S)

# #     n = n + 1


# # print("S = ", S, " n = ", n-1)

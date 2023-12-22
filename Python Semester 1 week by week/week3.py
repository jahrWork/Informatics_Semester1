# from math import sqrt, factorial


# # Imperative program (sequence of steps, how to )
# n = 6
# f = 1
# for i in range(1, n+1):
#        f = f * i
#        print("f =", f)

# # Declarative program (what to do)
# print( "factorial(n) = ", factorial(n))


# z = 3

# # Imperative program (sequence of steps, how to )
# x = 1
# f = 1 # f should be zero because f = x**2 - y
# while abs(f) > 0.001 :
#    f =  x**2 - z
#    x =  x - 0.1 * f
#    print(x)

# # Declarative program (what to do)
# print("sqrt(z)=", sqrt(z))


# print("prime numbers")
# n = 13
# for i in range(2,n):
#     if n % i == 0:
#           break

# if i<n-1:
#         print(n, "is not prime")
# else:
#         print(n, "is prime")


# print("perfect numbers")
# n = 6
# S = 0
# for i in range(1,n):
#     if n % i == 0:
#           print( i, "is a factor")
#           S = S + i

# if S==n:
#         print(n, "is perfect")
# else:
#         print(n, "is not perfect")


N = 10
print("Determine N=", N, "first primes")

S_prime = 0
N_prime = 0
n = 2
while N_prime < N:

    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            # print( n, " is not prime because ", i, "is a factor")
            is_prime = False
            break

    if is_prime:
        print(n, "is prime")
        N_prime = N_prime + 1
        S_prime = S_prime + n

    else:
        print(n, "is not prime")
        pass

    n = n + 1

print("\n \n")
print(S_prime)

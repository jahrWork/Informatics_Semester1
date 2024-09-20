from math import sqrt, exp, factorial, sin, cos
# Functions


# """
#     It determines the first derivative

#     Inputs:
#           f : function f: R -> R
#           x : point to evaluate the derivative

#     Output
#           approximated derivative at x

# """


# def Derivative3(x, z):

#     Dx = 1e-6

#     return (x(z+Dx) - x(z)) / Dx  # lim h->0 ( f(x+h) - f(x) )/h


# def Derivative(f, x):

#     Dx = 1e-6

#     return (f(x+Dx) - f(x)) / Dx  # lim h->0 ( f(x+h) - f(x) )/h


# def Derivative2(f, x):

#     Dx = 1e-6

#     return (f(x+Dx) - f(x-Dx)) / (2*Dx)


# # *********************************************************
# # 1. Determine derivative of h(x) = sqrt(x) at x=0.1
# #    for a given tolerance
# # *********************************************************
# def g(x):

#     return sqrt(x)


# def g1(y):

#     return sin(y)


# x0 = 0.1
# D = Derivative(g, x0)
# De = 1/2 * x0**(-1/2)
# print("Derivative = ",  D, "Error = ", De - D)

# D = Derivative2(g, x0)
# De = 1/2 * x0**(-1/2)
# print("Derivative = ",  D, "Error = ", De - D)


# D = Derivative2(g1, x0)
# De = cos(x0)
# print("Derivative = ",  D, "Error = ", De - D)


# D = Derivative3(g1, x0)
# De = cos(x0)
# print("Derivative = ",  D, "Error = ", De - D)


# def Integral(f, a, b):

#     M = 10000
#     dx = (b-a)/M

#     F = [f(a+dx*i) for i in range(M)]

#     return dx * sum(F)


# def h(x):

#     return sqrt(x)


# # *********************************************************
# # 2. Determine integral of h(x) = sqrt(x) from a=0 to b=1
# #    for a given tolerance
# # *********************************************************
# a, b = 0., 1.
# I = Integral(h, a, b)
# Ie = 2/3 * (b**(3/2) - a**(3/2))
# print("Integral = ",  I, "Error = ", Ie - I)


# I = Integral(f=h, a=0., b=1.)
# Ie = 2/3
# print("Integral = ",  I, "Error = ", Ie - I)


def Taylor(df, x0, x, N):
    """"
        Taylor expansion =  sum _{k=0} ^N f_k(x0) (x-x0)**k / k!
            Inputs:
              df   : function kth derivative of f(x)
              x0   : origin of Taylor expansion
                x   : point where Taylor is evaluated
                N   : last term of Taylor expansion

            return:
                Taylor expansion evaluated at x
    """

    def b(k):

        return df(x0, k) * (x - x0)**k / factorial(k)

    return sum([b(k) for k in range(N+1)])


# ************************************************************************
# 4. Taylor expansion of exp(x) origen x0=0 at x =1 with tolerance eps
# ************************************************************************
def dexp(x, k):

    return exp(x)


# T = Taylor(df=dexp, x0=0., x=1., N=12)
# print(" T = ", T, " E =", exp(1.) - T)

N = [1, 2, 3, 4, 5, 6, 7, 8, 16]
for n in N:
    T = Taylor(df=dexp, x0=0., x=1., N=n)
    E = exp(1.) - T
    print("N=", n, "Taylor exp(1.) x0=0   :", T, "Error =", E)

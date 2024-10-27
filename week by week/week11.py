from math import sqrt, exp, factorial, sin, cos


# #***************************************************
# # Implement Taylor cosine expansion 
# #***************************************************
def Taylor_cosine(x, tol): 
    
    T = 0; n = 0 
    
    while abs( cos(x)-T) >= tol:
        T += (-1)**n * x**(2*n) / factorial(2*n)
        n += 1 
  
    return T 

print("Taylor(1, 1e-3) =", Taylor_cosine(x = 1, tol = 1e-3), "cos(1) =", cos(1.))




# #***************************************************
# # Implement Taylor expansions 
# #***************************************************
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

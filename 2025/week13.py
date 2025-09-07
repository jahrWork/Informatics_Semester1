# Vectors and matrices

from numpy import zeros, sum, dot, matmul, array,  max, argmax, transpose, size, shape, trace, identity


def Matrices_allocation():

    S = sum([trace(Vandermonde(M)) for M in range(1, 11)])
    print("1. sum from M=1 to 10 of  trace ( A_M ) =   ", S)

    S = sum([ trace(matmul(Vandermonde(M), Vandermonde(M))) for M in range(1, 6)])
    print("2. sum from M=1 to 5 of traces ( A_M **2 ) = ", S)

    Ak = array(zeros([8, 8, 6]))
    for k in range(6):
        Ak[:, :, k] = power(Vandermonde(8), k)

    S = trace(sum(Ak, axis=2))  # trace( I + Ak + Ak**2 +... Ak**5 )
    print("3. trace ( sum from k=0 to 10 of A_5**k )=", S)


#  Vandermonde matrix A of dimension MxM
def Vandermonde(N):
    
    V = zeros( (N, N) )
    for i in range(1, N+1): 
        for j in range(1, N+1): 
            V[i-1,j-1] = (i/float(N))**(j-1)

    return V


# It determines the kth power of matrix A
def power(A, k):

    (N, M) = shape(A)

    if k == 0:
        return identity(N)
    else:
        return matmul(power(A, k-1), A)


Matrices_allocation()

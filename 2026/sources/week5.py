#***************************************************
#   Numpy: Matrices, +, -, transpose, inverse, determinant
#***************************************************
from numpy import array



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

# M = array( [ [1,2], [3,4] ] )
# print("M = ", M[0,0], M[0, 1] )
# print(" first row of M = ", M[0,:])
# print(" first column of M = ", M[:,0])
          




# Vectors and matrices + PEI2 simulacro

from numpy import zeros, sum, dot, matmul, array,  max, argmax, transpose, size, shape
from numpy import set_printoptions
from numpy.linalg import det, norm


# A = array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# u = array([1, 1, 1])

# print(type(A))
# print("\n A = ", A)
# print("\n u = ", u)

# A[0, 0] = 0

# print("\n A = ", A)

# A[:, 0] = -1

# print("\n A = ", A)

# A[1, :] = -2

# print("\n A = ", A)


# # # # print("\n A[0,1] = ", A[0, 1])

# print("\n A u = ", matmul(A, u))

# # B = A
# # print(" id of A =", id(A), id(B))
# # print("\n A + B = ", A+B)


# print("\n 3 A = ", 3 * A)

#print("\n det(A) = ", det(A))

# # copy submatrix
# N = 4
# A = array([[j**2+i for j in range(1, N+1)] for i in range(1, N+1)])

# print("A =", A)

# B = A[0:2, 0:2]
# C = A[2:4, 2:4]
# print("B =", B, " C =", C)


A = array( [ [1,2], [3,4] ] )
b = array( [ 1, 0 ] )
print("A= \n", A) 
print("b= \n", b) 
print("element wise operations A*b =\n", A*b) 
print( "matmul  A b = ", matmul(A,b) )


print("\n\n By definition 0**0= ", 0**0, "\n ")
# ***********************************************************
# * Examples of vectorial and matrix operations
# ************************************************************
def Matrix_operation_examples():

    N = 5
    V = zeros( (N+1) )
    for i in range(0, N+1): 
        V[i] = 1/(i+1)**2 
   
    W = array( [(-1)**(i+1)/(2*i+1.) for i in range(0, N+1)] )

    A = array( [ [(i/N)**j for j in range(0, N+1) ] for i in range(0, N+1)])

    print(" 1. Sum ( V ) = ", sum(V))
    print(" 2. Sum ( A ) = ", sum(A))
    print(" 3. Sum ( V, V>0 ) = ", sum(V[V > 0]))
    print(" 4. Sum ( A, A>0.1 ) = ", sum(A[A > 0.1]))
    print(" 5. dot product  ( V, W ) = ", dot(V, W))
    print(" 6. dot product V and A(:,N) = ", dot(V, A[:, N-1]))
    print(" 7. mat multiply A times V = ", matmul(A, V))

    print(" 9. transpose (A) = ")
    B = transpose(A)
    set_printoptions(precision=3, threshold=8, suppress=True)
    print(" B = \n", B)

    print("10. maxval (A) = ", max(A))
    print("11. maxloc (A) = ", argmax(A))
    # WARNING: index is for the flattened matrix


Matrix_operation_examples()





# Vectors and matrices
print("\n")
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

def Vandermonde(N): 

    return array( [ [ (i/N)**(j-1) for j in range(1,N+1)] for i in range(1, N+1) ])

def trace(A): 
 
    N, M = shape(A) 

    return sum( array( [ A[i,i] for i in range(0, N) ]  ) ) 

print("\n Trace Vandermonde(2) =", trace( Vandermonde(2)))

from numpy import sin, pi 

#***************************************************************
# Partition of segment [a, b] in N intervals.
# Determine interior nodes x_i = a + (b-a)/N i from i=0 to i=N
#***************************************************************
def partition(a, b, N): 
  
  return array([a + (b-a)/N * i for i in range(0, N+1)])

def f(x): 
    return sin(pi*x)

def derivative(f,  x, h=1e-3): # h=1e-3 if iti is not specified 
    return ( f(x+h) - f(x-h) )/(2*h)




print("\nFunctions. Image of an isolated point:")
xi = 0.5
yi = f(xi)
ypi = derivative(f, xi) 
print(" xi=", xi)
print(" yi =", yi)


print("\nFunctions. Image of whole set of points:")
x = partition(a=0., b=1., N=20)
y = f(x)
yp = derivative(f, x) 
print(" x=", x)
print(" y =", y)


# boolean masks 
X = array( [[1,1], [2,2], [3,3], [4,4], [5,5], [6,6] ])
labels = array( [1,1,2,2,3,3])
X_2 = X[labels==2,:]
print("X_1 value 1:", X_2 )


x = array([1,2,3])
for i,xi in enumerate(x): 
    print(i,xi, x[i])

from numpy import concatenate
y = array([4,5,6])     
z = concatenate( (x,y) )
print(z)
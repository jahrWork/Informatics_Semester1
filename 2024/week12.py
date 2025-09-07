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

print("\n det(A) = ", det(A))

# # copy submatrix
# N = 4
# A = array([[j**2+i for j in range(1, N+1)] for i in range(1, N+1)])

# print("A =", A)

# B = A[0:2, 0:2]
# C = A[2:4, 2:4]
# print("B =", B, " C =", C)


# ***********************************************************
# * Examples of vectorial and matrix operations
# ************************************************************
# def Matrix_operation_examples():

#     N = 5
#     V = zeros( (N) )
#     for i in range(1, N+1): 
#         V[i-1] = 1/i**2 
   
#     W = array( [(-1)**(i+1)/(2*i+1.) for i in range(1, N+1)] )

#     A = array( [ [(i/N)**(j-1) for j in range(1, N+1) ] for i in range(1, N+1)])

#     print(" 1. Sum ( V ) = ", sum(V))
#     print(" 2. Sum ( A ) = ", sum(A))
#     print(" 3. Sum ( V, V>0 ) = ", sum(V[V > 0]))
#     print(" 4. Sum ( A, A>0.1 ) = ", sum(A[A > 0.1]))
#     print(" 5. dot product  ( V, W ) = ", dot(V, W))
#     print(" 6. dot product V and A(:,N) = ", dot(V, A[:, N-1]))
#     print(" 7. mat multiply A times V = ", matmul(A, V))

#     print(" 9. transpose (A) = ")
#     B = transpose(A)
#     set_printoptions(precision=3, threshold=8, suppress=True)
#     print(" B = \n", B)

#     print("10. maxval (A) = ", max(A))
#     print("11. maxloc (A) = ", argmax(A))
#     # WARNING: index is for the flattened matrix


# Matrix_operation_examples()

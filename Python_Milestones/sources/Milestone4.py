from numpy import zeros, sum, dot, matmul, array,  max, argmax, transpose, size, shape
from numpy import set_printoptions

    
#***********************************************************
#* Examples of vectorial and matrix operations
#************************************************************  
def Matrix_operation_examples():  

    N = 10 
  
    V = array( [  1./i**2 for i in range(1, N+1) ] )
    W = array( [ (-1)**(i+1)/(2*i+1.) for i in range(1, N+1) ] ) 
    A = array( [ [ (i/float(N))**(j-1) for j in range(1,N+1) ] for i in range(1, N+1) ] )
        
    print( " 1. Sum ( V ) = ", sum(V) )
    print( " 2. Sum ( A ) = ", sum(A) ) 
    print( " 3. Sum ( V, V>0 ) = ", sum( V[ V>0 ] ) )
    print( " 4. Sum ( A, A>0.1 ) = ", sum( A[ A>0.1 ] ) ) 
    print( " 5. dot product  ( V, W ) = ", dot(V, W)   ) 
    print( " 6. dot product V and A(:,N) = ", dot( V, A[:,N-1] ) ) 
    print( " 7. mat multiply A times V = ", matmul( A, V ) )
    print( " 8. my_matmul sum(A times A) = ", sum( my_matmul(A,A) ) )
    
    print( " 9. transpose (A) = ") 
    B = transpose(A) 
    set_printoptions(precision=3, threshold=8, suppress=True )
    print(" B = \n", B ) 
    
    print( "10. maxval (A) = ", max(A) )
    print( "11. maxloc (A) = ", argmax(A) ) 
    # WARNING: index is for the flattened matrix
  
  

#********************************************************
# Dot product of two vectors of dimension N 
#    sum from i=1 to i=N ( u_i * v_i ) 
#********************************************************
def my_dot_product( u, v ):  
   
    
    N = size(u) 
    
    S = 0 
    for i in range(1, N+1):   
        S = S + u[i] * v[i]   
    
    return S 
    

#***********************************************************
# Matrix multiplication  of two matrices A, B
#    of dimension NxM and MxL  
#    C_ij = A_ik * B_kj
#***********************************************************   
def my_matmul( A, B ):  
     
    N, M = shape(A)
    L = shape(B)[1]     

    C = array( zeros( [N,L] ) )
   

    for i in range(N): 
        for j in range(L): 
            
            S = 0 
            for k in range(M): 
                S = S + A[i,k] * B[k,j] 
            C[i,j] = S 

    return C 

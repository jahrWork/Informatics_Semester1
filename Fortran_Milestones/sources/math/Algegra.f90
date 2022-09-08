module Algebra 
   
    implicit none 
    
    contains 
    
! It calculates the trace of a square matrix 
function trace(A) result(S) 
    real, intent(in) :: A(:, :)  ! assumed shape
    real :: S 
    
    integer :: k ! index of diagonal 
    integer :: N ! matrix dimension 
    
    N = size( A, dim=1)  ! rows dim=1, columns dim=2  
    
    S = 0 
    do k=1, N 
        S = S + A(k, k)
    end do 
    
end function 

! It creates a Vandermonde matrix of dimension N x N 
function Vandermonde(N) result(A) 
    integer, intent(in) :: N  ! Vandermonde dimension 
    real :: A( N, N )  
    
    integer :: i, j  ! row, column 
    
    do i=1, N 
        do j=1, N 
            A(i,j) = ( i / real(N) )**(j-1) 
        end do 
    end do
    
    
end function


! It calculates the kth power of matrix A 
function power(A, k) result(B) 
    real, intent(in) :: A(:, :)  
    integer, intent(in) :: k  ! kth power 
    real :: B( size(A,dim=1), size(A,dim=1) )  
    
     integer :: i, N  
    
    ! A**k = A A**(k-1) 
    N = size( A, dim=1) 
    
    B = Identity(N)
    
    do i=1, k 
        B = matmul( B, A )  ! k=1, B <- I A
                            ! k=2  B <- A A
                            ! k=3  B <- A**2 A 
    end do 
       
end function 


function Identity(N) result(A) 
    integer, intent(in) :: N  ! Identity dimension 
    real :: A( N, N )  
    
    integer :: i, j  ! row, column 
    
    do i=1, N 
        do j=1, N 
            
            if (i==j) then 
                A(i,j) = 1 
            else 
                A(i,j) = 0 
            end if 
            
        end do 
    end do
    
    
end function  

    
end module 
    
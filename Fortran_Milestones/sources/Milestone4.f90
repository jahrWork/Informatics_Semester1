
!****************************************************************************
!  PURPOSE:  Operations with vector an matrices 
!****************************************************************************

module  Milestone4

    use my_operations
    implicit none
    
    
contains 
    
subroutine vector_operations 
    
    integer, parameter :: N = 3
    real :: V(N)                 ! vi = 1/i**2, i = 1, . . .N
    real :: W(N)                 ! wi = (−1)**(i+1)/(2i + 1), i = 1, . . .N
    real :: A(N,N)               ! aij = (i/N)**(j-1) , i = 1, . . .N, j = 1, . . .N
    integer :: i                 ! index or component 
    integer :: j                 ! column 
    real :: B(N,N) 
    
    do i=1, N                    ! explicit loop 
        V(i) = 1. / i**2 
        W(i) = (-1)**(i+1) / real(2*i + 1) 
        do j=1, N 
            A(i,j) = ( i/ real(N) ) **(j-1)
        end do
    end do 
    
    V = [ ( 1. / i**2, i=1, N )  ]   ! implicit loop 
  
    write(*,*) " Sum ( V ) = ", sum(V) 
    write(*,*) " Sum ( A ) = ", sum(A)
    write(*,*) " Sum ( V, V>0 ) = ", sum(V, V>0) 
    write(*,*) " Sum ( W ) = ", sum(W)
    write(*,*) " Sum ( W, W>0 ) = ", sum(W, W>0) 
    write(*,*) " Sum ( W, W>0 ) = ", sum_gt_zero(W)
    write(*,*) " dot product  ( V, W ) = ", dot_product(V, W) 
    write(*,*) " A v =   ", matmul(A, V) 
    
    B = transpose(A)
    write(*,*) " 8. transpose (A) = "
    do i=1, N ! print row by row 
        write(*,'(100f8.3)') (B(i, j), j=1, N) 
    enddo 
    
     write(*,*) " 9. maxval (A) = ", maxval(A)
     write(*,*)" 10. maxloc (A) = ", maxloc(A)
     write(*,*)" 11. minloc (A) = ", minloc(A)
    
    B = my_transpose(A) 
    write(*,*) " 8. my transpose (A) = "
    do i=1, N
        write(*,'(100f8.3)') (B(i, j), j=1, N) 
    enddo 
  
    write(*,*) " 9. my maxval (A) = ", my_maxval(A)
    !write(*,*) " 10. my maxloc (A) = ", my_maxloc(A)
    
    write(*,*) " 6. dot product V and A(:,N) = ", dot_product( V, A(:,N) ) 
    write(*,*) " 7. mat multiply A times V = ", matmul( A, V )
    
    B = matmul( A, A )
    write(*,*) " 10. mat multiply A times A = "
    do i=1, N
        write(*,*) (B(i,j), j=1, N) 
    end do 
    
    write(*,*) " 10. mat multiply A times A = "
    B = my_matmul( A, A )
    do i=1, N
        write(*,*) (B(i,j), j=1, N) 
    end do 
    
end subroutine 
    
end module 



!****************************************************************************
!  PURPOSE: Dynamic allocation and functional paradigm 
!****************************************************************************
module Milestone5

    use Algebra 
     
    implicit none

    
contains     
   
subroutine dynamic_allocation 

    real :: S                        ! sum 
    integer :: M                     ! Vandermonde dimension 
    real, allocatable :: Ak(:, :, :) ! rows, columns, kth power
    integer :: k                     ! index k of power 
    real, allocatable :: A(:, :)
    
        
    S = sum( [ ( trace( Vandermonde(M) ), M=1, 10)  ] )
    write(*,*) "1. S = ", S 
    
    S = 0 
    do M=1, 10 
        
        allocate( A(M,M) ) 
        do k=1, M 
            S = S + (k / real(M))**(k-1)     ! (i/M)**(j-1)
        end do 
        deallocate( A ) 
        
    end do 
    write(*,*) "1. S = ", S 
    
    
    
    allocate( Ak(8, 8, 0:5) ) 
    
    do k=0, 5 
     Ak(:, :, k) = power( Vandermonde(8), k) 
    end do 
    
    S = trace( sum( Ak, dim=3) )  ! trace( I + Ak + Ak**2 +... Ak**5 ) 
    
    write(*,*) "3. S = ", S 
    
end subroutine 


end module 
    


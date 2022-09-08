

!****************************************************************************
!
!  MODULE: Milestone3
!
!  PURPOSE:  Sum of numerical series 
!
!****************************************************************************

    module Milestone3
    
    use sum_series 
    implicit none

    
    contains 
    
    subroutine sum_series_examples
    
       real :: Tolerance ! allowed error 
       integer :: N  ! number of terms 
       integer :: k  ! index of series 
       real :: SN    ! sum 
   
 
       
     ! sum by means of summation function  
      do 
          
       write(*,*) " ____________________________ "   
       write(*,*) " Enter series number = ? "
       write(*,*) " 0:  exit        "
       write(*,*) " 1:  sum n    N terms   "
       write(*,*) " 2:  sum 2n-1 N terms "
       write(*,*) " 4:  sum 1/n**2 infinite terms "
       write(*,*) " 5:  sum 1/2**n infinite terms "
       write(*,*) " 6:  sum (-1)**(n+1) / 2**n infinite terms "
       write(*,*) " 7:  sum 1 / n! infinite terms "
       read(*,*) k 
       
       select case(k) 
       case(0)
           exit 
       case (1:3)
           write(*,*) " Enter number of terms N = ? "; read(*,*) N
           SN = summationN( k, N ) 
           
       case (4:7) 
           write(*,*) " Enter tolerance = ? "; read(*,*) tolerance 
           SN = summation( k, tolerance )
           
      case default
          write(*,*) "  series is not implemented k=", k 
       end select
       
       
      end do 
      
      
    end subroutine 
    
    end module


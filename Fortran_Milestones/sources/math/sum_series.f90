module sum_series 
    
    
    implicit none 
    real (kind=8), parameter :: PI = 4 * atan(1.) ! tan( PI/4) = 1 
    private 
    public :: summation, summationN 
    
    contains 
  
!**************************************************
! Summation of  numerical series
!      Inputs: 
!              k         : 1 (n), 2 (2n-1) 
!              N         :  number of terms
!**************************************************    
function summationN(k, N) result(S)
     integer, intent(in) :: k, N  
     real :: S     
    
    
    integer :: i  ! index 
    integer :: ai ! general term 
    
    S = 0; 
    do i=1, N 
           
          select case(k) 
          case(1)
             ai = i
          case(2)
             ai = 2*i-1 
          case default
              write(*,*) k, " :  number not implemented"
              stop 
          end select 
          
          S = S + ai       ! sum of n terms 
                    
          write(*,*) " i=", i, " ai =", ai,  " S =", S
      end do 
      
      write(*,*) " S =",  S 
    
 
 end function      
    
     
    
!**************************************************
! Summation of  numerical series of infinity terms 
!      Inputs: 
!              k         : 4,5 (1/n**2, 1/2**n ) 
!              tolerance : allowed error  
!**************************************************    
function summation(k, tolerance) result(Sn)
     integer, intent(in) :: k 
     real, intent(in) :: tolerance 
     
     real (kind=4) :: Sn 
      
    real (kind=4) :: an                ! general term 
    real (kind=4) :: Error             ! error of the partial sum 
    integer :: n, Nmax = 1000000       ! counter and max iterations 
       
      Sn = 0; n = 1;  Error = 1
      an = 1 
      
      do while (Error > tolerance .and. n < Nmax ) 
           
          select case(k) 
          case(4)
             an = 1 / real(n)**2  ! general term ( 1/real(n**2) might be wrong )
             Error = 1 / real(n)  ! error of the partial sum  
             
          case(5)
             an = 1 / 2.**n        ! general term
             Error = an / log(2.)  ! error of the partial sum 
             
          case(6)
             an = (-1)**(n+1) / 2.**n     ! general term
             Error = 10 * abs(an)         ! error of the partial sum 
             
          case(7)
             an = an / n       ! a1 <- a1 / 1, a2 <-  a1/2, a3 <- a2/3, a4 <- a3/4    
           ! an = 1. / gamma( real(n+1) )       !  n! general term
             Error = 10 * abs(an)      ! error of the partial sum    
              
             
          case default
              write(*,*) k, " :  number not implemented"
              stop 
          end select 
          
          Sn = Sn + an       ! sum of n terms 
          n = n + 1          ! counter 
                    
          write(*,'(a, i5, 3(a, es20.10))') " n=", n, " an =", an,  " Sn =", Sn, " Error =", Error
      end do 
     
      
      write(*,'(a,e20.15)') " Sn =",  Sn; 
      
end function 


    
    
end module 
    
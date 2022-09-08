  
!****************************************************************************
!  PURPOSE:  Taylor series 
!****************************************************************************
module Milestone7

    use Taylor_expansion
    use plots 
    use dislin
    
    implicit none

    
    
contains    
    
subroutine Taylor_examples 
    
    real :: PI = 4 * atan(1.) 

      
  !  Association: M is dummy argument, 4 is actual argument 
     write(*,*) " Taylor exp(1.) x0=0 with 2 terms  :", Taylor( fk = dkexp, x0 = 0., x = 1., M = 1) 
     write(*,*) " Taylor exp(1.) x0=0 with 5 terms  :", Taylor( fk = dkexp, x0 = 0., x = 1., M = 4) 
     write(*,*) " Taylor exp(1.) x0=0 eith infinity terms  :", Taylor( fk = dkexp, x0 = 0., x = 1. )
     write(*,*) " Press enter to continue";  read(*,*) 
    
     
     call plot_ini(xmin = 0., xmax = 2*PI, ymin = -2., ymax = 2.) 
     call plotf( cosine ) 
     call color("red")
     call plotf( Taylor_cosine )
     call disfin                  ! show all plots 
     
     call plot_ini(xmin = -0.9, xmax = 0.9, ymin = 0., ymax = 5.) 
     call plotf( fraction )  
     call color("red") 
     call plotf( Taylor_fraction ) 
     call disfin 
     
end subroutine     
     
    
function Taylor_cosine(x) result(h) 
      real, intent(in) :: x 
      real :: h 
      
        h = Taylor( fk = dk_cosine, x0 = 0., x = x, M = 10 ) 
        
end function    
    
 function dk_cosine(x, k) result(dk) 
      real, intent(in) :: x 
      integer, intent(in) :: k 
      real :: dk  
      
        complex :: I = (0., 1.) 
        
        ! Z = exp( I * x)             = cos(x) + I sin(x) 
        ! Zk = (I)**k * exp( I * x )  = dk( cos(x) )/dxk + I dk( sin(x) ) /dxk 
        ! Z'= I * exp( I * x) 
        ! Zk = (I)**k * exp( I * x ) 
      
        dk = real ( I**k * exp( I * x) ) ! cosine 
     !  dk = imag ( I**k * exp( I * x) ) ! sine 
        
end function   

function cosine(x) result(h) 
      real, intent(in) :: x 
      real :: h 
      
        h = cos( x) 
        
end function

function Taylor_fraction(x) result(h) 
      real, intent(in) :: x 
      real :: h 
      
        h = Taylor( fk = dk_fraction, x0 = 0., x = x, M = 5 ) 
        
end function    
    
 function dk_fraction(x, k) result(dk) 
      real, intent(in) :: x 
      integer, intent(in) :: k 
      real :: dk  
            
     ! f(x) = 1/ ( 1 - x) 
     ! f' = + 1 / ( 1 - x ) **2 
     ! fk = k! (1-x)**(-k-1)  
     ! k! = gamma(k+1) 
       dk =  gamma( real(k+1) ) * ( 1 - x ) **(-k-1) 
        
end function   

function fraction(x) result(h) 
      real, intent(in) :: x 
      real :: h 
      
        h = 1 / ( 1 - x ) 
        
end function

function exponential(x) result(h) 
      real, intent(in) :: x 
      real :: h 
      
        h = exp( x) 
        
end function
  
function dkexp(x, k) result(dk) 
      real, intent(in) :: x 
      integer, intent(in) :: k 
      real :: dk  
      
        dk = exp( x) 
        
end function

function dksinh(x, k) result(dk) 
      real, intent(in) :: x 
      integer, intent(in) :: k 
      real :: dk  
      
      if ( mod(k, 2) == 0 ) then 
          dk = sinh(x) 
      else 
          dk = cosh(x) 
      end if  
        
end function


end module 


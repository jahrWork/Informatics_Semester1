  
!****************************************************************************
!  PURPOSE:  Plot functions, integrals and derivatives.
!****************************************************************************

module Milestone6

    use calculus
    use plots 
    implicit none 
    
    real, parameter :: PI = 4 * atan(1.)  
    
contains 
    
subroutine piecewise_functions     
    
     
      real :: a = -2*PI, b = 2*PI 
      
     call plot( f = sine1x, a =0.05, b = 0.1 )       ! plot sine function  
     call plot( sine, a, b )       ! plot sine function 
     
     call plot( piecewise, a, b)   ! plot piecewise function 
     call plot( Dpiecewise, a, b)  ! plot derivative of piecewise function 
     call plot( Ipiecewise, a, b)  ! plot integral of piecewise function 
    
end subroutine 
   
function sine1x(x) result(h) 
      real, intent(in) :: x 
      real :: h 
       
      real :: p1 = 0.6062483
      real :: PI = 4 * atan(1.) 
      
        h = sin( PI * (1+p1)/x ) 
        
end function    
    
function sine(x) result(h) 
      real, intent(in) :: x 
      real :: h 
      
        h = sin( x) 
        
end function
    
function piecewise(x) result(g) 
      real, intent(in) :: x 
      real :: g 
      
       if ( x < -PI/2 ) then 
           
            g = 0 
            
       else if ( x < PI/2 ) then 
           
            g = cos(x) 
            
       else 
           
            g = 0 
            
       end if 
      
end function 
    
function Ipiecewise(x) result(Ig)
      real, intent(in) :: x 
      real :: Ig 
      
        Ig = integral( piecewise, a = -1., b = x ) 
       
      
end function 
    
function Dpiecewise(x) result(dg) 
      real, intent(in) :: x 
      real :: dg 
      
        dg = derivative( piecewise, x ) 
      
      
end function 
     
   

end module 


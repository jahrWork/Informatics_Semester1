module calculus 
    
    implicit none 
    
    interface 
     function f_R_R(x) result(f)
        real, intent(in) :: x 
        real :: f 
      end function 
    end interface 
    
    
contains 


function derivative( f, x0 ) result(df)
 procedure (f_R_R) :: f 
 real, intent(in) :: x0 
 real :: df 
 
    real :: h  
    
      h = 1e-5 
      
      df = ( f(x0+h) - f(x0) ) / h  ! lim h->0 ( f(x0+h) - f(x0) )/h 
   
end function 

function integral( f, a, b ) result(I)
 procedure (f_R_R) :: f 
 real, intent(in) :: a, b 
 real :: I  
 
    integer :: k, M  
    real :: dx, xk  
     
      dx = 1e-3
      M = abs(b-a)/dx  ! with dx and M => X_M  /= b 
      dx = (b-a)/M     ! to assure X_{M} = b 
  
    ! int f(x) dx = lim dx-> sum ( dx f(xk) )  
      I = dx * sum( [ ( f( a + dx*k ), k=0, M-1) ] ) 
      
   
end function 

    
end module
    
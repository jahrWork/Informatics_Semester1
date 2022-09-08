module plots
    
    use dislin 
    implicit none 
    
    interface 
     function f_R_R(x) result(f)
        real, intent(in) :: x 
        real :: f 
      end function 
    end interface 
    
    real, save :: xmin_, xmax_  
    
    
contains 

subroutine plot( f, a, b ) 
 procedure (f_R_R) :: f 
 real, intent(in) :: a, b 
 
 
    integer, parameter :: M = 200  
    integer :: i 
    real :: x(0:M), y(0:M)    
    
      x = [ ( a + (b-a)*i/real(M), i=0, M) ] 
      
      y = [ ( f( x(i) ), i=0, M) ]
      
      call scrmod("reverse")
      call metafl('XWIN')
      call qplot(x, y, M+1) 
      
    
    
end subroutine 

    
   
    
subroutine plot_ini( xmin, xmax,  ymin, ymax ) 
    real, intent(in) ::  xmin, xmax, ymin, ymax 

    
    call metafl("xwin")
    CALL PAGE (4000, 4000)
    call scrmod("reverse")
    call disini  
    call graf(xmin, xmax, xmin, (xmax-xmin)/10, ymin, ymax, ymin, (ymax-ymin)/10) 
   
    xmin_ = xmin 
    xmax_ = xmax 
    
end subroutine    
    
    
subroutine plotf( f ) 
 procedure (f_R_R) :: f 
 
 
    integer, parameter :: M = 200  
    integer :: i 
    real :: x(0:M), y(0:M)    
    
      x = [ ( xmin_ + (xmax_-xmin_)*i/real(M), i=0, M) ] 
      
      y = [ ( f( x(i) ), i=0, M) ]
      
      call curve(x, y, M+1) 
      
    
    
end subroutine 





    
end module
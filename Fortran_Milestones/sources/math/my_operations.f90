module my_operations 
   
    implicit none 
    
    contains    
  

function sum_gt_zero( V ) result(S) 
  real, intent(in) :: V(:)  ! assumed shape 
  real :: S 
  
    integer :: i, N 
    
  N = size(V) 
  S = 0 
  do i=1, N 
      if (V(i) > 0 ) then 
                          S = S + V(i) 
      else 
              
      endif 
  end do 
  
  
end function 

function my_transpose( A ) result(B) ! A dummy argument 
  real, intent(in) :: A(:, :)  ! assumed shape 
  real :: B( size(A, dim=2), size(A, dim=1) )  
  
   integer :: i, j  ! row sand column
   integer :: N 
   
   N = size(A, dim=1) ! rows dim=1, columns dim=2 
   
   do i=1, N 
       do j=1, N 
           B(i,j) = A(j,i) 
       end do 
   end do 
   
  
end function 

function my_maxval( A ) result(S) ! A dummy argument 
  real, intent(in) :: A(:, :)  ! assumed shape 
  real :: S  
  
   integer :: i, j  ! row sand column
   integer :: N, M  ! rows and columns  
   
   N = size(A, dim=1) ! rows dim=1 
   M = size(A, dim=2) ! columns dim=2 
   
   S = -1e30
   
   do i=1, N 
       do j=1, M
           
           if (A(i,j) > S) then 
               S = A(i,j) 
           end if 
           
       end do 
   end do 
   
end function 

function my_matmul( A, B ) result(C) 
  real, intent(in) :: A(:, :), B(:,:)  ! assumed shape 
  real :: C( size(A, dim=1), size(B, dim=2) )   
  
   integer :: i, j  ! rows and column
   integer :: N, M  ! rows and columns of A 
   integer ::  L    ! rows and columns of B 
   real :: S 
   integer :: k 
   
   N = size(A, dim=1) ! rows dim=1 
   M = size(A, dim=2) ! columns dim=2 
   M = size(B, dim=1) ! rows dim=1 
   L = size(B, dim=2) ! columns dim=2 
    
 ! C_ij = sum from k=1 to M ( A_ik * B_kj )    
   do i=1, N 
       do j=1, L 
           
           S = 0. 
           do k=1, M 
               S = S + A(i,k) * B(k,j) 
           end do 
           C(i,j) = S
           
       end do 
   end do 
   
end function 
    
end module 
    

!****************************************************************************
!  PROGRAM: Milestone8 Read data file 
!****************************************************************************

module Milestone8
    
    
       use Read_files
       implicit none

  
contains 
    
!   It allows to test the load matrix function 
subroutine Test_load_matrix 
    
         real, allocatable :: A(:,:) 
         integer :: i 
    
         A = load_matrix('data.csv') 
         
         do i=1, size(A, dim=1) 
            write(*,'(10f8.3)') A(i,:) ! print row ith 
         end do 
                 
         A = load_matrix('data2.csv') 
         
         do i=1, size(A, dim=1) 
            write(*,'(10f8.3)') A(i,:) 
         end do 
         
end subroutine
    
end module
    
    


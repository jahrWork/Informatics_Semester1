module Read_files 
    
    
    implicit none 
    
    contains 
    
!   it reads a filename and save its data in matrix A 
    function load_matrix( filename ) result(A) 
        character(len=*), intent(in) :: filename ! string of characters 
        real, allocatable :: A(:,:) 
        
      ! Local variables   
        integer :: i_file = 8        ! file unit to read 
        character(len=400) :: header ! text header row 
        integer ::  M, N             ! rows(M) and columns(N) 
        integer :: i 
               
        open( unit = i_file, file = filename)  ! it associates 8 to filename
        read( unit = i_file, fmt = '(A)') header 
            
        N = columns( string = header, s = "," ) 
        M = 0
        do  
            read(unit = i_file, fmt = *, end = 10) ! if end of file then, go to 10
            M = M + 1 
        end do 
10      write(*,*) " N =", N, "M = ", M  
                
        allocate( A(M, N) )
        
        rewind(unit = i_file)
        read(i_file, '(A)' ) header       ! header 
        do i=1, M 
            read( i_file, *) A(i, :) 
        end do 
        
        close(i_file)   ! to allow others to read filename 
        
    end function 
    
!   it counts the number of colummns by counting delimiters s
    integer function columns( string, s) result(M) 
       character(len=*), intent(in) :: string 
       character, intent(in) :: s             ! delimiter 
       
       integer :: i, L ! length
       
       L = len_trim(string)  ! length without blanks 
       
       M = 1
       do i=1, L 
           if (string(i:i) == s ) then 
               M = M + 1 
           end if 
       end do 
       
    end function 
  
    
end module 
    
    
    
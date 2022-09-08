
!****************************************************************************
!  PROGRAM: GUI Graphical user interface 
!****************************************************************************
    program GUI

    use dislin 
    implicit none

      integer :: i, j, id_screen, id 
      integer :: ox, oy, o1, o2, ip(8, 8), idt 
      integer :: sx, sy 
         
      call wgini('form',id) ! wigdet initialization with id: identifier
    
      sx = 70; sy = 70  ! size in x and y 
      o1 = -50; o2 = 0  ! origen 
      
      call swgsiz(sx,sy) ! set wigdet size 
      do i=1, 8 
          do j=1, 8 
              ox = o1 + sx * i  
              oy = o2 + sy * j 
              call swgpos(ox, oy)              ! position widget 
              call wgpbut(id, 'A', ip(i,j) )   ! push button with ip(i,j) identifier
              call swgcbk(ip(i,j), callback_subroutine) ! link push button and subroutine
          end do 
      end do 
    
    call wgfin
       
    contains 
!*************************************************    
! It is executed when some push button is clicked  
!*************************************************    
subroutine callback_subroutine(ib) 
    integer, intent(in) :: ib       ! identifier of the clicked widget 
     
      integer :: i2, i, j 
      
      !row and column of widgets 
       i = (ib-2)/8 + 1
       j = (ib-1) - 8*(i-1) 
       
       write(*,*) " ib = ", ib, " i= ", i, " j= ", j  
      
       ! x_i = o1 + i * sx = -50 + 3 * 70 position 
       call swgatt(ip(i,j), 'invisible', 'status')    ! make invisible 
       call swgpos(o1 + i*sx, o2 + j*sy)              ! set the same position    
       call wgpbut(id, '11', i2)                       ! create new push button
                                                      ! i2 is the idenfier of the new button
       
       call swgatt(ip(i-1,j), 'invisible', 'status')  ! make invisible  
       call swgpos(o1 + (i-1)*sx, o2 + j*sy)          ! set the same position    
       call wgpbut(id, '22', i2)                       ! create new push button
       
       call swgatt(ip(i+1,j), 'invisible', 'status')  ! make invisible 
       call swgpos(o1 + (i+1)*sx, o2 + j*sy)          ! set the same position    
       call wgpbut(id, '33', i2)                       ! create new push button
    
end subroutine 
    
subroutine strings_examples 
  
   character(len=100) :: string = "la vida loca" 
   integer :: i, di, L  
    
   L = len_trim(string); i = 1
   
   do while (i<L) 
       
     di = index(string(i:L), " ") 
     
     if (di == 0) then 
         exit
     else 
          string( i+di-1:i+di-1 ) = "-"  
          i = i + di + 1 
          write(*,*) "processed string = ", string 
          write(*,*) " i= ", i, "di =", di 
          read(*,*)
     end if 
    
   end do 
   
end subroutine 



end program GUI


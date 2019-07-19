program wallis
      implicit none
      real*4 :: tmp_, pi
      integer :: i, n = 100000000

      pi = 2.0
      tmp_ = 0.0

      do i = 1, n

        tmp_ = 4.0*real(i)**2;
        pi = pi * tmp_/(tmp_ - 1.0);

      end do
    
      print *, n, " -> ", pi

end program 


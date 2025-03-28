module arithmetics

    implicit none

    contains

        subroutine matmul(A, B, C, Na, Nb, Nc)

            implicit none

            double precision, intent(in)  :: A(Na, Nb)
            double precision, intent(in)  :: B(Nb, Nc)
            double precision, intent(out) :: C(Na, Nc)
            integer         , intent(in)  :: Na
            integer         , intent(in)  :: Nb
            integer         , intent(in)  :: Nc

            integer :: i, j, k

            C(:, :) = 0.d0

            !$OMP PARALLEL PRIVATE(k)
            !$OMP DO COLLAPSE(2) SCHEDULE(dynamic)
            do i=1, Nc
                do j=1, Na
                    !$OMP SIMD
                    do k=1, Nb
                        C(j, i) = C(j, i) + A(j, k)*B(k, i)
                    end do
                end do
            end do
            !$OMP END DO
            !$OMP END PARALLEL

        end subroutine matmul

end module arithmetics
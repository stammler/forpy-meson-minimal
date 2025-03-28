! Module contains subroutines to compute the matrix-matrix product.

module arithmetics

    ! Variable to set the number of threads in parallel environment
    use parallel, only: N_threads

    implicit none

    contains

        subroutine matmul(A, B, C, Na, Nb, Nc)
            ! Function computes matrix-matrix product.
            ! C = A @ B
            !
            ! Parameters
            ! ----------
            ! A : array, shape (Na, Nb)
            ! B : array, shape (Nb, Nc)
            ! Na : integer
            ! Nb : integer
            ! Nb : integer
            !
            ! Returns
            ! -------
            ! B : array, shape (Na, Nc)

            implicit none

            double precision, intent(in)  :: A(Na, Nb)
            double precision, intent(in)  :: B(Nb, Nc)
            double precision, intent(out) :: C(Na, Nc)
            integer         , intent(in)  :: Na
            integer         , intent(in)  :: Nb
            integer         , intent(in)  :: Nc

            integer :: i, j, k

            ! Initializig output array with zeros
            C(:, :) = 0.d0

            !$OMP PARALLEL NUM_THREADS(N_threads) SHARED(A, B, C) PRIVATE(i, j, k) 
            !$OMP DO COLLAPSE(2) SCHEDULE(static)
            do i=1, Nc
                do j=1, Na
                    !!$OMP SIMD
                    do k=1, Nb
                        C(j, i) = C(j, i) + A(j, k)*B(k, i)
                    end do
                end do
            end do
            !$OMP END DO
            !$OMP END PARALLEL

        end subroutine matmul

        subroutine matmul_blocked(A, B, C, Na, Nb, Nc, block_size)
            ! Function computes matrix-matrix product including loop blocking.
            ! C = A @ B
            !
            ! Parameters
            ! ----------
            ! A : array, shape (Na, Nb)
            ! B : array, shape (Nb, Nc)
            ! Na : integer
            ! Nb : integer
            ! Nb : integer
            ! block_size : integer
            !
            ! Returns
            ! -------
            ! B : array, shape (Na, Nc)

            implicit none

            double precision, intent(in)  :: A(Na, Nb)
            double precision, intent(in)  :: B(Nb, Nc)
            double precision, intent(out) :: C(Na, Nc)
            integer         , intent(in)  :: Na
            integer         , intent(in)  :: Nb
            integer         , intent(in)  :: Nc
            integer         , intent(in)  :: block_size

            integer :: i, ii, j, jj, k, kk

            ! Initializig output array with zeros
            C(:, :) = 0.d0

            !$OMP PARALLEL NUM_THREADS(N_threads) SHARED(A, B, C, block_size) PRIVATE(i, j, k, ii, jj, kk)
            !$OMP DO collapse(3) SCHEDULE(static)
            ! This reduces cache misses in the inner loops.
            do i=1, Nc, block_size
                do j=1, Na, block_size
                    do k=1, Nb, block_size
                        do ii=i, min(Nc, i+block_size-1)
                            do jj=j, min(Na, j+block_size-1)
                                !&OMP SIMD
                                do kk=k, min(Nb, k+block_size-1)
                                    C(jj, ii) = C(jj, ii) + A(jj, kk)*B(kk, ii)
                                end do
                            end do
                        end do
                    end do
                end do
            end do
            !$OMP END DO
            !$OMP END PARALLEL

        end subroutine matmul_blocked

end module arithmetics
! Module contains subroutines to set up the parallel environment.

module parallel

    use omp_lib

    implicit none

    ! Shared variable to set number of threads
    integer :: N_threads

    contains

        subroutine in_parallel_true(flag)
            ! Function checks if multithreading with OpenMP is available.
            !
            ! Returns
            ! -------
            ! flag : int
            !   1, if OpenMP available
            !   0, if OpenMP not available

            implicit none

            logical, intent(out) :: flag

            !$OMP PARALLEL
            flag = omp_in_parallel()
            !$OMP END PARALLEL

        end subroutine in_parallel_true


        subroutine set_num_threads(N)
            ! Function sets the number of threads that should be used
            ! in N_threads variable. Will not be greater than the
            ! maximum number of available threads.
            !
            ! Parameters
            ! ----------
            ! N : int
            !   Number of threads to be used

            implicit none

            integer, intent(in) :: N

            N_threads = min(N, omp_get_max_threads())

        end subroutine set_num_threads


        subroutine init()
            ! Function initializes N_threads with the maximum number of
            ! available threads.

            implicit none

            N_threads = omp_get_max_threads()

        end subroutine init

end module parallel
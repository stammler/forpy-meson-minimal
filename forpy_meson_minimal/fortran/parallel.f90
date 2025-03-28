module parallel

    use omp_lib

    implicit none

    integer :: N_threads

    contains

        subroutine in_parallel_false(flag)

            implicit none

            logical, intent(out) :: flag

            flag = omp_in_parallel()

        end subroutine in_parallel_false

        subroutine in_parallel_true(flag)

            implicit none

            logical, intent(out) :: flag

            !$OMP PARALLEL
            flag = omp_in_parallel()
            !$OMP END PARALLEL

        end subroutine in_parallel_true

        subroutine set_num_threads(N)

            implicit none

            integer, intent(in) :: N

            N_threads = min(N, omp_get_max_threads())

        end subroutine set_num_threads

        subroutine init()

            implicit none

            N_threads = omp_get_max_threads()

        end subroutine init

end module parallel
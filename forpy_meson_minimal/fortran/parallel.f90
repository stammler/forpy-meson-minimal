module parallel

    use omp_lib

    implicit none

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

end module parallel
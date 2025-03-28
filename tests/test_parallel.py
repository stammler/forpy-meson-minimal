from forpy_meson_minimal.fortran import parallel


def test_in_parallel_true():
    # Tests if the parallel environment is detected successfully.
    assert parallel.in_parallel_true() == 1

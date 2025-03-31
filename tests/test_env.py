from forpy_meson_minimal.fortran import parallel


def test_env():
    # Tests if the parallel environment is not detected in
    # non-parallel installation.
    assert parallel.in_parallel_true() == 0


def test_env_parallel():
    # Tests if the parallel environment is detected successfully.
    assert parallel.in_parallel_true() == 1

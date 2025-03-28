from forpy_meson_minimal.fortran import parallel


def test_in_parallel_true():
    assert parallel.in_parallel_true() == 1


def test_in_parallel_false():
    assert parallel.in_parallel_false() == 0

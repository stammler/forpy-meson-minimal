from forpy_meson_minimal import matmul
import numpy as np
import pytest


def test_matmul_input_shapes():
    A = np.empty((1))
    B = np.empty((1, 2))
    with pytest.raises(RuntimeError):
        matmul(A, B)
    A = np.empty((1, 2))
    B = np.empty((1, 1, 1))
    with pytest.raises(RuntimeError):
        matmul(A, B)
    A = np.empty((1, 2))
    B = np.empty((1))
    with pytest.raises(RuntimeError):
        matmul(A, B)


def test_matmul_shape_mismatch():
    A = np.empty((1, 2))
    B = np.empty((1, 2))
    with pytest.raises(RuntimeError):
        matmul(A, B)


def test_matrix_vector_multiplication():
    A = np.array(
        [
            [1., 2., 3.],
            [4., 5., 6.],
            [7., 8., 9.],

        ]
    )
    B = np.array([1., 2., 3.])
    C_res = np.array([14., 32., 50.])
    C = matmul(A, B)
    # Dimension check
    assert C.shape == (3, )
    # Result check
    assert np.allclose(C, C_res)


def test_matrix_matrix_multiplication():
    A = np.array(
        [
            [1., 2., 3.],
            [4., 5., 6.],
            [7., 8., 9.],

        ]
    )
    B = np.array(
        [
            [1., 2.],
            [3., 4.],
            [5., 6.],
        ]
    )
    C_res = np.array(
        [
            [22.,  28.],
            [49.,  64.],
            [76., 100.],
        ]
    )
    C = matmul(A, B)
    # Dimension check
    assert C.shape == (3, 2)
    # Result check
    assert np.allclose(C, C_res)

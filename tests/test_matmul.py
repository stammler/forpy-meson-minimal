from forpy_meson_minimal import matmul
import numpy as np
import pytest


def test_matmul_input_block_size_any():
    # Tests for correct catches of incorrect block sizes
    A = np.empty((1))
    B = np.empty((1, 2))
    with pytest.raises(RuntimeError):
        block_size = "block_size"
        matmul(A, B, block_size=block_size)
    with pytest.raises(RuntimeError):
        block_size = 0
        matmul(A, B, block_size=block_size)


def test_matmul_input_shapes_any():
    # Tests for correct catches of incorrect input shapes
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


def test_matmul_shape_mismatch_any():
    # Tests for correct catch of dimension mismatch in inputs
    A = np.empty((1, 2))
    B = np.empty((1, 2))
    with pytest.raises(RuntimeError):
        matmul(A, B)


def test_matrix_vector_multiplication_any():
    # Tests matrix-vector multiplication
    A = np.array(
        [
            [1.0, 2.0, 3.0],
            [4.0, 5.0, 6.0],
            [7.0, 8.0, 9.0],
        ]
    )
    B = np.array([1.0, 2.0, 3.0])
    C_res = np.array([14.0, 32.0, 50.0])
    C = matmul(A, B)
    # Dimension check
    assert C.shape == (3,)
    # Result check
    assert np.allclose(C, C_res)


def test_matrix_matrix_multiplication_any():
    # Tests matrix-matrix multiplication
    A = np.array(
        [
            [1.0, 2.0, 3.0],
            [4.0, 5.0, 6.0],
            [7.0, 8.0, 9.0],
        ]
    )
    B = np.array(
        [
            [1.0, 2.0],
            [3.0, 4.0],
            [5.0, 6.0],
        ]
    )
    C_res = np.array(
        [
            [22.0, 28.0],
            [49.0, 64.0],
            [76.0, 100.0],
        ]
    )
    C = matmul(A, B)
    # Dimension check
    assert C.shape == (3, 2)
    # Result check
    assert np.allclose(C, C_res)


def test_matrix_vector_multiplication_blocked_any():
    # Tests matrix-vector multiplication with loop blocking
    A = np.array(
        [
            [1.0, 2.0, 3.0],
            [4.0, 5.0, 6.0],
            [7.0, 8.0, 9.0],
        ]
    )
    B = np.array([1.0, 2.0, 3.0])
    C_res = np.array([14.0, 32.0, 50.0])
    C = matmul(A, B, block_size=32)
    # Dimension check
    assert C.shape == (3,)
    # Result check
    assert np.allclose(C, C_res)


def test_matrix_matrix_multiplication_blocked_any():
    # Tests matrix-matrix multiplication with loop blocking
    A = np.array(
        [
            [1.0, 2.0, 3.0],
            [4.0, 5.0, 6.0],
            [7.0, 8.0, 9.0],
        ]
    )
    B = np.array(
        [
            [1.0, 2.0],
            [3.0, 4.0],
            [5.0, 6.0],
        ]
    )
    C_res = np.array(
        [
            [22.0, 28.0],
            [49.0, 64.0],
            [76.0, 100.0],
        ]
    )
    C = matmul(A, B, block_size=32)
    # Dimension check
    assert C.shape == (3, 2)
    # Result check
    assert np.allclose(C, C_res)

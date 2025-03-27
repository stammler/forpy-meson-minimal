from forpy_meson_minimal.fortran import arithmetics


def matmul(A, B):

    # Input shapes
    if len(A.shape) != 2:
        raise RuntimeError("Array A needs to be two-dimensional")
    if len(B.shape) > 2 or len(B.shape) < 1:
        raise RuntimeError("Array B needs to be one- oder two-dimensional.")

    # Dimension mismatch
    if A.shape[1] != B.shape[0]:
        raise RuntimeError("Dimension mismatch of input arrays.")

    # Making sure B has two dimensions
    B = B.reshape((B.shape[0], -1))

    # Compute the result
    C = arithmetics.matmul(A, B)

    # Squeeze back to one dimension if possible
    C = C.squeeze()

    return C

import forpy_meson_minimal as forpy
import numpy as np
from timeit import default_timer

N_threads = [2**i for i in range(6)]

rng = np.random.default_rng()

K = 4_000
L = 3_000
M = 2_000

A = rng.random((K, M))
B = rng.random((M, L))

print()

print("PARALLEL TIMING TEST")
print("--------------------")

print()

print(f"Matrix-matrix multiplication:\n  C({K}x{L}) = A({K}x{M}) @ B({M}x{L})")

print()

for N in N_threads:
    forpy.fortran.parallel.set_num_threads(N)
    print(f"# Running with {forpy.fortran.parallel.n_threads:d} threads ...")
    t_start = default_timer()
    C = forpy.matmul(A, B)
    print(f"  - elapsed time: {default_timer() - t_start:.2f} s")

print()

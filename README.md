# Fortran-Python-Meson Minimal

Minimum working example of a Python project utilizing compiled Fortran functions using the Meson build system. This minimum working example includes optional parallelization with OpenMP.

## Installation

To install the package with OpenMP routines run

```{.bash}
pip install .
```

in the base directory. To install the package without OpenMP parallelization run

```{.bash}
pip install . --config-settings=setup-args="-Dopenmp=false"
```

The `openmp` option is by default `true`.

## Tests

The repository contains unit tests, which can be invoked by running `pytest`. If the package has been installed using OpenMP routines, the unit tests can be executed with:

```{.bash}
pytest -k "parallel or any"
```

in the base directory. If all unit tests pass the installation was successfull and parallelization with OpenMP is available.

If the package has been installed without OpenMP parallelization run the unit tests with:

```{.bash}
pytest -k "not parallel or any"
```

## Usage

The package computes the matrix-vector multiplication

$
\vec{c} = \mathcal{A} \cdot \vec{b}
$

or the matrix-matrix multiplication

$
\mathcal{C} = \mathcal{A} \cdot \mathcal{B}
$

using parallelized Fortran subroutines.

```{.python}
import forpy_meson_minimal as forpy
import numpy as np

rng = np.random.default_rng()

Na, Nb, Nc = 30, 20, 10

A = rng.random((Na, Nb))
B = rng.random((Nb, Nc))

C = forpy.matmul(A, B)
```

The number of threads can be set with

```{.python}
import forpy_meson_minimal as forpy

forpy.fortran.parallel.set_num_threads(4)
```

The module contains additionally subroutines utilizing loop blocking, which can be activated by passing the `block_size` keyword argument:

```{.python}
import forpy_meson_minimal as forpy
import numpy as np

rng = np.random.default_rng()

Na, Nb, Nc = 30, 20, 10
block_size = 32
N_threads

forpy.fortran.parallel.set_num_threads(N_threads)

A = rng.random((Na, Nb))
B = rng.random((Nb, Nc))

C = forpy.matmul(A, B, block_size=block_size)
```

## Examples

The repository contains two examples in the `examples/` directory. One runs timed test problems with different numbers of threads (works only in the parallel installation) without loop blocking:

```
python timing_threads.py
```

```{.text}
PARALLEL TIMING TEST
--------------------

Matrix-matrix multiplication:
  C(4000x3000) = A(4000x2000) @ B(2000x3000)

# Running with 1 threads ...
  - elapsed time: 50.66 s
# Running with 2 threads ...
  - elapsed time: 25.53 s
# Running with 4 threads ...
  - elapsed time: 11.55 s
# Running with 8 threads ...
  - elapsed time: 6.78 s
# Running with 16 threads ...
  - elapsed time: 6.11 s
# Running with 32 threads ...
  - elapsed time: 4.56 s
```

The other example runs timed test problems with a fixed number of threads but with loop blocking of varying block sizes:

```
python timing_blocks.py
```
```{.text}
PARALLEL TIMING TEST
--------------------

Matrix-matrix multiplication:
  C(4000x3000) = A(4000x2000) @ B(2000x3000)

# Running with block_size = 1 ...
  - elapsed time: 4.27 s
# Running with block_size = 2 ...
  - elapsed time: 6.27 s
# Running with block_size = 4 ...
  - elapsed time: 3.76 s
# Running with block_size = 8 ...
  - elapsed time: 2.74 s
# Running with block_size = 16 ...
  - elapsed time: 1.97 s
# Running with block_size = 32 ...
  - elapsed time: 2.27 s
# Running with block_size = 64 ...
  - elapsed time: 2.17 s
# Running with block_size = 128 ...
  - elapsed time: 2.10 s
# Running with block_size = 256 ...
  - elapsed time: 2.80 s
# Running with block_size = 512 ...
  - elapsed time: 3.25 s
```

#### Acknowledgements

I would like to thank the developers of NumPy for removing `distutils`. Without that decision I would have never had the pleasure of working with Meson.
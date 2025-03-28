"""
Minimum working example of a Python project utilizing compiled Fortran
functions using the Meson build system. The minimum working example includes
parallelization with OpenMP.
"""

from importlib import metadata
from .matmul import matmul
from . import fortran

__name__ = "forpy-meson-minimal"
__version__ = metadata.version("forpy_meson_minimal")

__all__ = [
    "matmul",
    "fortran",
]

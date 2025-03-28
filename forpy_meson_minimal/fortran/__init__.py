"""
Module contains Fortran modules arithmetics, that does the heavy lifting of
the matrix multiuplication, and parallel, that has utilities to set up the
parallel environment.
"""

from .fortran import arithmetics
from .fortran import parallel

__all__ = [
    "arithmetics",
    "parallel",
]

# Initialize threads in parallel module
parallel.init()

from importlib import metadata
from .matmul import matmul
from . import fortran

__version__ = metadata.version("forpy_meson_minimal")
__all__ = [
    "matmul",
    "fortran",
]

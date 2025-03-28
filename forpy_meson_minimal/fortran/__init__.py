from .fortran import arithmetics
from .fortran import parallel

__all__ = [
    "arithmetics",
    "parallel",
]

# Initialize threads in parallel module
parallel.init()
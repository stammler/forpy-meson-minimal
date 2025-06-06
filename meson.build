# Project setup
project(
  'forpy_meson_minimal',  # Name of project
  'c',                    # Default language
  default_options : [     # Default options
    'optimization=3',     # Optimization level
  ]
)
add_languages('fortran')  # Adding Fortran to languages

# Setting up OpenMP dependency
# User can deactivate compilation with OpenMP. Default is true.
# The option has to be described in 'meson_options.txt' first.
use_openmp = get_option('openmp')
if use_openmp
  # Do not raise error if OpenMP is not available
  omp_dep = dependency('openmp', required : false)
else
  omp_dep = []
endif

# Python setup
py_mod = import('python')
py = py_mod.find_installation(pure : false) # Python executable
py_dep = py.dependency()                    # Python dependencies

# NumPy include directory
incdir_numpy = run_command(
  py,
  ['-c', 'import os; os.chdir(".."); import numpy; print(numpy.get_include())'],
  check : true
).stdout().strip()

# f2py include directory
incdir_f2py = run_command(py,
    ['-c', 'import os; os.chdir(".."); import numpy.f2py; print(numpy.f2py.get_include())'],
    check : true
).stdout().strip()

# NumPy and f2py includes
inc_np = include_directories(incdir_numpy, incdir_f2py)

# Going to project sub-directory
subdir('forpy_meson_minimal')
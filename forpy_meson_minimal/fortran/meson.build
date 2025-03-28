# Installing Python files
python_sources = [
    '__init__.py',
]
py.install_sources(python_sources, subdir: 'forpy_meson_minimal/fortran')

# Compiling arithmetics modules
arithmetics_source = custom_target(
  'arithmeticsmodule.c',                                              # Target files to be created
  input : ['arithmetics.f90'],                                        # Input file to be compiled
  output : ['arithmeticsmodule.c', 'arithmetics-f2pywrappers2.f90'],  # Output files
  command : [                                                         # Compile command to be executed
    py, '-m', 'numpy.f2py',                                           # Running f2py
    '-m', 'arithmetics',                                              # Module name
    '--lower',                                                        # Convert Fortran to lower case
    '--build-dir', 'forpy_meson_minimal/fortran',                     # Build files in directory
    '@INPUT@'                                                         # Files to be compiled
  ]
)
# Building Python extension for arithmetics module
py.extension_module(
  'arithmetics',                                                      # Module name
  ['arithmetics.f90', arithmetics_source],                            # Source files
  incdir_f2py / 'fortranobject.c',
  include_directories: inc_np,                                        # Directories to include
  dependencies : [py_dep, omp_dep],                                   # Dependencies to be used
  install : true,                                                     # Install extension
  subdir : 'forpy_meson_minimal/fortran',                             # Directory to install extension in
)

# Compiling parallel module
parallel_source = custom_target(
  'parallelmodule.c',                                                 # Target files to be created
  input : ['parallel.f90'],                                           # Input file to be compiled
  output : ['parallelmodule.c', 'parallel-f2pywrappers2.f90'],        # Output files
  command : [                                                         # Compile command to be executed
    py, '-m', 'numpy.f2py',                                           # Running f2py
    '-m', 'parallel',                                                 # Module name
    '--lower',                                                        # Convert Fortran to lower case
    '--build-dir', 'forpy_meson_minimal/fortran',                     # Build files in directory
    '@INPUT@'                                                         # Files to be compiled
  ]
)
# Building Python extension for parallel module
py.extension_module(
  'parallel',                                                         # Module name
  ['parallel.f90', parallel_source],                                  # Source files
  incdir_f2py / 'fortranobject.c',
  include_directories: inc_np,                                        # Directories to include
  dependencies : [py_dep, omp_dep],                                   # Dependencies to be used
  install : true,                                                     # Install extension
  subdir : 'forpy_meson_minimal/fortran',                             # Directory to install extension in
)
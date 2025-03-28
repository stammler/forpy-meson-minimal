# Installing Python files
python_sources = [
    '__init__.py',
]
py.install_sources(python_sources, subdir: 'forpy_meson_minimal/fortran')

# Compiling Fortran module
source_files = ['parallel.f90', 'arithmetics.f90']            # Source files to be compiles
fortran_source = custom_target(
  'fortranmodule.c',                                          # Target files to be created
  input : source_files,                                       # Source files
  output : ['fortranmodule.c', 'fortran-f2pywrappers2.f90'],  # Output files
  command : [                                                 # Compile command to be executed
    py, '-m', 'numpy.f2py',                                   # Running f2py
    '-m', 'fortran',                                          # Module name
    '--lower',                                                # Convert Fortran to lower case
    '--build-dir', 'forpy_meson_minimal/fortran',             # Build files in directory
    '@INPUT@'                                                 # Files to be compiled
  ]
)
# Building Python extension for Fortran module
py.extension_module(
  'fortran',                                                  # Module name
  [source_files, fortran_source],                             # Source files
  incdir_f2py / 'fortranobject.c',
  include_directories: inc_np,                                # Directories to include
  dependencies : [py_dep, omp_dep],                           # Dependencies to be used
  install : true,                                             # Install extension
  subdir : 'forpy_meson_minimal/fortran',                     # Directory to install extension in
)
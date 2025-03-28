python_sources = [
    '__init__.py',
]
py.install_sources(python_sources, subdir: 'forpy_meson_minimal/fortran')

inc_np = include_directories(incdir_numpy, incdir_f2py)

arithmetics_source = custom_target('arithmeticsmodule.c',
  input : ['arithmetics.f90'],
  output : ['arithmeticsmodule.c', 'arithmetics-f2pywrappers2.f90'],
  command : [
    py, '-m', 'numpy.f2py',
    '-m', 'arithmetics',
    '--lower', '--verbose',
    '--build-dir', 'forpy_meson_minimal/fortran',
    '@INPUT@'
  ]
)
py.extension_module('arithmetics',
  ['arithmetics.f90', arithmetics_source],
  incdir_f2py / 'fortranobject.c',
  include_directories: inc_np,
  dependencies : [py_dep, omp_dep],
  install : true,
  subdir : 'forpy_meson_minimal/fortran',
)

parallel_source = custom_target('parallelmodule.c',
  input : ['parallel.f90'],
  output : ['parallelmodule.c', 'parallel-f2pywrappers2.f90'],
  command : [
    py, '-m', 'numpy.f2py',
    '-m', 'parallel',
    '--lower', '--verbose',
    '--build-dir', 'forpy_meson_minimal/fortran',
    '@INPUT@'
  ]
)
py.extension_module('parallel',
  ['parallel.f90', parallel_source],
  incdir_f2py / 'fortranobject.c',
  include_directories: inc_np,
  dependencies : [py_dep, omp_dep],
  install : true,
  subdir : 'forpy_meson_minimal/fortran',
)
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.1] - 2025-03-31

### Added

- Optional compilation with OpenMP. To install wihtout OpenMP use  
`pip install . --config-settings=setup-args="-Dopenmp=false"`.  
The `openmp` option is `true` by default.
import forpy_meson_minimal
from importlib import metadata


def test_version():
    # Tests that the version passed correctly
    v1 = forpy_meson_minimal.__version__
    v2 = metadata.version("forpy_meson_minimal")
    assert v1 == v2

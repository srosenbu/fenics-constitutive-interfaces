from __future__ import annotations

import importlib.metadata

import fenics_constitutive_interfaces as m


def test_version():
    assert importlib.metadata.version("fenics_constitutive_interfaces") == m.__version__

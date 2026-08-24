import os
import sys

sys.path.insert(0, os.path.dirname(__file__))


import mpmath
import pytest


@pytest.fixture(autouse=True)
def _reset_mpmath_precision():
    """Module-level mp.dps writes must not leak across the suite."""
    mpmath.mp.dps = 15
    yield
    mpmath.mp.dps = 15

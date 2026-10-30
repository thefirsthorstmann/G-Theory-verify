import os
import sys

import mpmath
import pytest

sys.path.insert(0, os.path.dirname(__file__))


@pytest.fixture(autouse=True, scope="module")
def _mpmath_precision_quarantine():
    """Reset mpmath to its default precision at every module boundary.

    Fourth incident of the dps-pollution class (2026-08-22): pytest imports
    every battery at collection, so a module-level `mp.dps = N` executes
    before ANY test runs and the alphabetically LAST setter wins for the
    whole suite. A new battery setting 20 at import starved the archimedes
    battery (needs 120) and the pi-structure battery (needs 70), which had
    been passing on the accident of import order.

    The rule this fixture enforces: no battery may lean on another's
    precision. A battery needing more than the default declares it at
    runtime — `with mp.workdps(N):` per computation, or an autouse fixture
    of its own — never at module level.
    """
    mpmath.mp.dps = 15
    yield
    mpmath.mp.dps = 15


# A failed `assert fragment not in TEXT` must report, not hang (2026-10-07).
#
# The language-pass batteries join a whole record into one line and assert that retired wording is absent. When such
# an assertion fails, pytest explains it by diffing TEXT against TEXT with the fragment removed; the two lengths
# differ, so the trailing context is not trimmed, and difflib compares two single lines of about 300,000 characters
# character by character, which runs for hours and prints nothing. One battery run and, indirectly, the whole suite
# stalled this way on 7 October. Above a size at which no diff could be read, the sizes are reported instead; the
# assertion's own message (the fragment) still names what failed. `_diff_text` is pytest's private helper, so the
# guard installs only where it exists, and `test_the_assertion_guard.py` pins that it does.
try:
    import _pytest.assertion.util as _assertion_util
    _pytest_diff_text = _assertion_util._diff_text
except (ImportError, AttributeError):                    # a pytest without the helper: nothing to guard
    _assertion_util = None

DIFF_LIMIT = 20000


def _bounded_diff_text(left, right, *args, **kwargs):
    if max(len(left), len(right)) > DIFF_LIMIT:
        return [f"(no diff computed: texts of {len(left)} and {len(right)} characters)"]
    return _pytest_diff_text(left, right, *args, **kwargs)


if _assertion_util is not None:
    _assertion_util._diff_text = _bounded_diff_text

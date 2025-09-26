"""Test suite for basic calculator operations.

This module contains small, explicit pytest tests for the four
arithmetic functions provided by the calculator package.
"""

from __future__ import annotations

import pytest

from addition import add
from subtraction import subtract
from multiplication import multiply
from division import divide


def test_addition() -> None:
    """Ensure addition works for two integers."""
    assert add(2, 3) == 5


def test_subtraction() -> None:
    """Ensure subtraction works for two integers."""
    assert subtract(5, 2) == 3


def test_multiplication() -> None:
    """Ensure multiplication works for two integers."""
    assert multiply(4, 3) == 12


def test_division() -> None:
    """Ensure division works for two integers."""
    assert divide(10, 2) == 5


def test_division_by_zero() -> None:
    """Division by zero should raise ValueError."""
    with pytest.raises(ValueError):
        divide(5, 0)

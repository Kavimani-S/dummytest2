# test_calculator.py
import sys
import os
import pytest



# Add the parent directory to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from dummytest.main import Calculator
def test_add():
    calc = Calculator()
    assert calc.add(1, 2) == 3
    assert calc.add(-1, 1) == 0
    assert calc.add(0, 0) == 0

def test_subtract():
    calc = Calculator()
    assert calc.subtract(3, 1) == 2
    assert calc.subtract(0, 0) == 0
    assert calc.subtract(-1, -1) == 0

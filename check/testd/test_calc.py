# test.py
import sys
import os
import unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from dummytest.main import Calculator

class TestCalculator(unittest.TestCase):
    def test_add(self):
        calc = Calculator()
        self.assertEqual(calc.add(1, 2), 3)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(0, 0), 0)

if __name__ == "__main__":
    unittest.main()

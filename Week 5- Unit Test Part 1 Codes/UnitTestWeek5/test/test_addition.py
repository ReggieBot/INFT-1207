import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.addition import Addition

class TestAddition(unittest.TestCase):
    def test_add_method_returns_correct_result(self):
        calc = Addition()
        self.assertEqual(calc.add(2,2), 4)
        self.assertEqual(5, calc.add(2,3))

    def test_add_method_raises_typeerror(self):
        calc = Addition()
        self.assertRaises(TypeError, calc.add, "Hello", "World")
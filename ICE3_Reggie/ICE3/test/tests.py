# Reggie Brown
# 12/02/25
# ICE 3
# Professor Patel
# Desc: Test cases for ICE2
# Github: https://github.com/ReggieBot/INFT-1207/tree/main/ICE3_Reggie/ICE3/test
# References:
# https://docs.python.org/3/reference/import.html

import unittest
import sys
import os


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.minimum_finder import find_minimum

class TestMinimum(unittest.TestCase):

    def test_1A(self):
        self.assertEqual(find_minimum([90]), 90)

    def test_1B(self):
        self.assertEqual(find_minimum([12, 10]), 10)

    def test_1C(self):
        self.assertEqual(find_minimum([10, 12]), 10)

    def test_1D(self):
        self.assertEqual(find_minimum([12, 14, 36]), 12)

    def test_1E(self):
        self.assertEqual(find_minimum([36, 14, 12]), 12)

    def test_1F(self):
        self.assertEqual(find_minimum([14, 12, 36]), 12)

    def test_2A(self):
        self.assertRaises(ValueError, find_minimum, [])

    def test_3A(self):
        self.assertEqual(find_minimum([10, 23, 34, 81, 97]), 10)

    def test_3B(self):
        self.assertEqual(find_minimum([97, 81, 34, 23, 10]), 10)

    def test_4A(self):
        self.assertEqual(find_minimum([10, -2, 5, 23]), -2)

    def test_4B(self):
        self.assertEqual(find_minimum([10, -2, -24, 4]), -24)

    def test_5A(self):
        self.assertEqual(find_minimum([-23, -31, -45, -56]), -56)

    def test_5B(self):
        self.assertEqual(find_minimum([-6, -203, -2, -78]), -203)

    def test_6A(self):
        self.assertRaises(ValueError, find_minimum, [23, 34.56, 67, 33])

    def test_7A(self):
        self.assertRaises(ValueError, find_minimum, [23, 'hi', 32, 1])

    def test_7B(self):
        self.assertRaises(ValueError, find_minimum, [12, '&', '*', '34m', '!'])

    def test_8A(self):
        self.assertEqual(find_minimum([3, 4, 6, 9, 6]), 3)

    def test_8B(self):
        self.assertEqual(find_minimum([13, 6, 6, 9, 15]), 6)

    def test_9A(self):
        self.assertEqual(find_minimum([530, 4294967297, 23, 46, 59]), 23)


if __name__ == '__main__':
    unittest.main()

# Conclusion
# Tests failed.
# All of the assertEqual checks passed, 
# But the assertRaises failed
# I believe this is because instead of doing input validation inside of the find_minimum function,
# I did some of the validation in the main method itself, which is not what's being tested.
# Good thing I ran some tests huh. 
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
        self.assertEqual(find_minimum([12, 10]))






if __name__ == '__main__':
    unittest.main()

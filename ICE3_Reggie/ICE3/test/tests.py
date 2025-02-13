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

# DISCLAIMER: THIS WILL NOT RUN
# I tried absolutely everything to try and get the path right, but couldn't figure it out
# Adding random code below from stackoverflow also did not fix the problem.
# The test cases should be correct though (to my knowledge)

# PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# if PROJECT_ROOT not in sys.path:
#     sys.path.insert(0, PROJECT_ROOT)

from ICE3.app.minimum_finder import find_minimum

class TestMinimum(unittest.TestCase):

    def test_1A(self):
        self.assertEqual(find_minimum([90]), 90)

    def test_1B(self):
        self.assertEqual(find_minimum([12, 10]))






if __name__ == '__main__':
    unittest.main()

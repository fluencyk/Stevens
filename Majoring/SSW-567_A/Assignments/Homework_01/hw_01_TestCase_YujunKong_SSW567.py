# ===== Python - UTF-8 ===== #
"""/**
School: Stevens Institute of Technology
Course: SSW 567 - A
Instructor: Prof. Andre Bondi
---------------------------------------
Topic: Homework # 01 <- Unittest Case
---------------------------------------
Coder with CWID: Yujun Kong / 1046 6820
*/"""
# ===== CODING BEGINS ===== #

import sys, gc, unittest
from hw_01_YujunKong_SSW567 import classify_triangle, Valio
from typing import Any, Optional

# <{test case}>
class Test_If_Object(unittest.TestCase):

    def test_if_object(self):

        v = Valio()
        self.assertIsInstance(v, Valio)

class Test_If_Positive_Number(unittest.TestCase):

    def test_if_positive_number(self):

        v = Valio()
        self.assertIsNone(v.if_positive_number("1024.2048"))
        self.assertFalse(v.if_positive_number("-9999"))
        self.assertFalse(v.if_positive_number("abcdefg"))

class Test_If_Equal(unittest.TestCase):

    def test_classify_triangle(self):

        self.assertEqual(classify_triangle(2, 2, 2), "Equilateral")
        self.assertEqual(classify_triangle(2, 2, 4), "Isosceles")
        self.assertEqual(classify_triangle(3, 11, 33), "Scalene")
        self.assertEqual(classify_triangle(3, 4, 5), "Right")

        self.assertNotEqual(classify_triangle(1, 1, 3), "Equilateral")
        self.assertNotEqual(classify_triangle(3, 6, 9), "Isosceles")
        self.assertNotEqual(classify_triangle(4, 4, 7), "Scalene")
        self.assertNotEqual(classify_triangle(5, 9, 22), "Right")
# </{t}>

"""/** test cases program executes below */"""

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)

# ===== CODING ENDS ===== #
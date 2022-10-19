# -*- coding: utf-8 -*-
"""
School: Stevens Institute of Technology
Course: SSW 567 - A
Instructor: Prof. Andre Bondi
----- ----- ----- ----- -----
Topic: Homework # 05 / Test Cases
Requirement: Using static code analysis techniques and tools
----- ----- ----- ----- -----
@author: Yujun Kong
"""
import unittest
from hw_05_perfection_yujun_kong import Fraction, FractionsCalculator

class TestFraction(unittest.TestCase):
    """ test base class Fraction """
    def test_fraction_constructor(self):
        """ test constructor of target class """
        result = Fraction(0, 2).value
        self.assertEqual(result, "0")

        result = Fraction(10, -20).numerator
        self.assertEqual(result, -1)

        result = Fraction(-30, -30).value
        self.assertEqual(result, "1")

        result = Fraction(40, 20).value
        self.assertEqual(result, "2")

class TestFractionCalculator(unittest.TestCase):
    """ test calculation methods """

    def test_plus(self):
        """ test plus method """
        f_a = Fraction(39, -78)
        f_b = Fraction(10, 20)

        tfc = FractionsCalculator()
        tfc.plus(f_a, f_b)
        result = tfc.result.value
        self.assertEqual(result, "0")

    def test_minus(self):
        """ test minu method """
        f_a = Fraction(49, 70)
        f_b = Fraction(14, 20)

        tfc = FractionsCalculator()
        tfc.minus(f_a, f_b)
        result = tfc.result.value
        self.assertEqual(result, "0")

    def test_multiply_01(self):
        """ test multiply method 01 """
        f_a = Fraction(10, 50)
        f_b = Fraction(0, 60)

        tfc = FractionsCalculator()
        tfc.multiply(f_a, f_b)
        result = tfc.result.value
        self.assertEqual(result, "0")

    def test_multiply_02(self):
        """ test multiply method 02 """
        f_a = Fraction(25, 50)
        f_b = Fraction(30, 60)

        tfc = FractionsCalculator()
        tfc.multiply(f_a, f_b)
        result = tfc.result.value
        self.assertEqual(result, "1/4")

    def test_devide_01(self):
        """ test devide method 01 """
        f_a = Fraction(0, 70)
        f_b = Fraction(10, 80)

        tfc = FractionsCalculator()
        tfc.devide(f_a, f_b)
        result = tfc.result.value
        self.assertEqual(result, "0")

    def test_devide_02(self):
        """ test devide method 02 """
        f_a = Fraction(-35, 70)
        f_b = Fraction(40, 80)

        tfc = FractionsCalculator()
        tfc.multiply(f_a, f_b)
        result = tfc.result.value
        self.assertEqual(result, "-1/4")

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

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

        result = Fraction(2, 0).value
        self.assertEqual(result, "Not a Valid Fraction!")

        result = Fraction(10, -20).numerator
        self.assertEqual(result, -1)

        result = Fraction(-30, -30).value
        self.assertEqual(result, "1")

        result = Fraction(40, 20).value
        self.assertEqual(result, "2")

        result = Fraction(40, -40).value
        self.assertEqual(result, "-1")

class TestFractionCalculator(unittest.TestCase):
    """ test calculation methods """

    f_a = Fraction(0, 1)
    f_b = Fraction(1, 2)

    f_c = Fraction(1, 2)
    f_d = Fraction(0, 1)

    f_e = Fraction(11, -22)
    f_f = Fraction(33, 66)

    f_g = Fraction(11, 22)
    f_h = Fraction(33, 132)

    def test_plus(self):
        """ test plus method """

        tfc = FractionsCalculator()
        tfc.plus(self.f_a, self.f_b)
        result = tfc.result.value
        self.assertEqual(result, "1/2")

        tfc.plus(self.f_c, self.f_d)
        result = tfc.result.value
        self.assertEqual(result, "1/2")

        tfc.plus(self.f_e, self.f_f)
        result = tfc.result.value
        self.assertEqual(result, "0")

        tfc.plus(self.f_g, self.f_h)
        result = tfc.result.value
        self.assertEqual(result, "3/4")

    def test_minus(self):
        """ test minu method """

        tfc = FractionsCalculator()
        tfc.minus(self.f_a, self.f_b)
        result = tfc.result.value
        self.assertEqual(result, "-1/2")

        tfc.minus(self.f_c, self.f_d)
        result = tfc.result.value
        self.assertEqual(result, "1/2")

        tfc.minus(self.f_e, self.f_f)
        result = tfc.result.value
        self.assertEqual(result, "-1")

        tfc.minus(self.f_g, self.f_h)
        result = tfc.result.value
        self.assertEqual(result, "1/4")

    def test_multiply(self):
        """ test multiply method """

        tfc = FractionsCalculator()
        tfc.multiply(self.f_a, self.f_b)
        result = tfc.result.value
        self.assertEqual(result, "0")

        tfc = FractionsCalculator()
        tfc.multiply(self.f_c, self.f_d)
        result = tfc.result.value
        self.assertEqual(result, "0")

        tfc = FractionsCalculator()
        tfc.multiply(self.f_e, self.f_f)
        result = tfc.result.value
        self.assertEqual(result, "-1/4")

        tfc = FractionsCalculator()
        tfc.multiply(self.f_g, self.f_h)
        result = tfc.result.value
        self.assertEqual(result, "1/8")

    def test_devide(self):
        """ test devide method """

        tfc = FractionsCalculator()
        tfc.devide(self.f_a, self.f_b)
        result = tfc.result.value
        self.assertEqual(result, "0")

        tfc = FractionsCalculator()
        tfc.devide(self.f_e, self.f_f)
        result = tfc.result.value
        self.assertEqual(result, "-1")

        tfc = FractionsCalculator()
        tfc.devide(self.f_g, self.f_h)
        result = tfc.result.value
        self.assertEqual(result, "2")

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

# -*- coding: utf-8 -*-
"""
School: Stevens Institute of Technology
Course: SSW 567 - A
Instructor: Prof. Andre Bondi
Topic: Homework # 02.a, fix bugs, refactor coding, and improve logic flow for the original program of classifying triangles and test cases

Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk

Fixed Sep 21, 2022
The purpose of the fixed part is to pinpoint the bugs and logical faults existed in the original coding and then fix them

@author: Yujun Kong
"""

import unittest
from Triangle_Fixed import classify_triangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class Test_Right_Triangles(unittest.TestCase): # Test Cases 01, 02, 03
    """ if each tested triangle is Right """

    def test_right_triangle_01(self): 
        self.assertEqual(classify_triangle(3, 4, 5),'Right','3, 4, 5 is a Right triangle')

    def test_right_triangle_02(self): 
        self.assertEqual(classify_triangle(5, 3, 4),'Right','5, 3, 4 is a Right triangle')

    def test_right_triangle_03(self): 
        self.assertNotEqual(classify_triangle(6, 7, 8),'Right','6, 7, 8 is a Right triangle')

class Test_Equilateral_Triangles(unittest.TestCase): # Test Cases 04, 05
    """ if each tested triangle is Equilateral """
        
    def test_equilateral_triangle_01(self): 
        self.assertEqual(classify_triangle(1, 1, 1),'Equilateral','1, 1, 1 should be equilateral')

    def test_equilateral_triangle_02(self): 
        self.assertNotEqual(classify_triangle(3, 5, 3),'Equilateral','3, 5, 3 should be equilateral')

class Test_Isosceles_Triangles(unittest.TestCase): # Test Cases 06, 07
    """ if each tested triangle is Isosceles but Not Right """

    def test_isosceles_triangle_01(self):
        self.assertEqual(classify_triangle(6, 6, 9),'Isosceles but Not Right','6, 6, 9 should be isoceles')

    def test_isosceles_triangle_02(self):
        self.assertNotEqual(classify_triangle(11, 12, 13),'Isosceles but Not Right','11, 12, 13 should be isoceles')

class Test_Scalene_Triangles(unittest.TestCase): # Test Cases 08, 09
    """ if each tested triangle is Scalene """

    def test_scalene_triangle_01(self):
        self.assertEqual(classify_triangle(7, 9, 11),'Scalene','7,9,11 should be scalene')

    def test_scalene_triangle_02(self):
        self.assertNotEqual(classify_triangle(8.21, 6.33, 8.21),'Scalene','8.21, 6.33, 8.21 should be scalene')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
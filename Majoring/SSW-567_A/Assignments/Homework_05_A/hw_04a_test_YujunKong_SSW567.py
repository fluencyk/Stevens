# -*- coding: utf-8 -*-
"""
School: Stevens Institute of Technology
Course: SSW 567 - A
Instructor: Prof. Andre Bondi
----- ----- ----- ----- -----
Topic: Homework # 04.a
Requirement: Get REST APIs of GitHub to peek user repos to output info
----- ----- ----- ----- -----
Testcase For: Homework # 04.a
----- ----- ----- ----- -----
@author: Yujun Kong
"""

import unittest
from hw_04a_YujunKong_SSW567 import GitHub_Info_Getter

class Test_GitHub_Info_Getter(unittest.TestCase):

    def test_get_info(self):

        gig = GitHub_Info_Getter("fluencyk")
        self.assertIn("fluencyk", gig.repo_info)

    def test_format_info(self):

        gig = GitHub_Info_Getter("fluencyk")
        self.assertIn("Number of commits", gig.format_info())

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
# -*- coding: utf-8 -*-
"""
School: Stevens Institute of Technology
Course: SSW 567 - A
Instructor: Prof. Andre Bondi
----- ----- ----- ----- -----
Topic: Homework # 05.a
Requirement: Understanding mock testing techniques
----- ----- ----- ----- -----
Testcase For: Homework # 05.a
----- ----- ----- ----- -----
@author: Yujun Kong
"""
import unittest
from unittest import mock
from hw_04a_ykong_ssw567 import GitHubInfoGetter

class TestGitHubInfoGetter(unittest.TestCase):
    """Pass"""
    def test_validate_user(self):
        """ test if validate method worked out """
        gig_01 = GitHubInfoGetter("stevens")
        result_01 = mock.Mock(return_value = gig_01.validate_user())
        self.assertFalse(result_01.return_value)

        gig_02 = GitHubInfoGetter("fluencyk")
        result_02 = mock.Mock(return_value = gig_02.validate_user())
        self.assertTrue(result_02.return_value)

    def test_get_info(self):
        """ test if getting correct pattern of the data structure """
        gig_03 = GitHubInfoGetter("fluencyk")

        result_01 = mock.Mock(return_value = len(gig_03.gh_mock_repos_stats[0].get("Repo")))
        self.assertEqual(result_01.return_value, 12)

        result_02 = mock.Mock(return_value = len(gig_03.gh_mock_repos_stats[0].get("Number of commits")))
        self.assertEqual(result_02.return_value, 1)

    def test_format_info(self):
        """ test if formatting out correct pattern look of ouput string """
        gig_04 = GitHubInfoGetter("fluencyk")

        result_01 = mock.Mock(return_value = gig_04.format_info())
        self.assertIn("Repo:", result_01.return_value)

        result_02 = mock.Mock(return_value = str(type(gig_04.format_info())))
        self.assertEqual(result_02.return_value, "<class 'str'>")

if __name__ == "__main__":
    print("Running unit tests")
    unittest.main()

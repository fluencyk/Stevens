"""/***
School: Stevens Institute of Technology
Course: SSW 810 - B
Instructor: Zhongyuan Yu
Teaching Assistant: Kavish Shanghvi
Homework: # 04 / Topic: Iteration
Coder Name with The CWID: Name: Yujun Kong / CWID: 1046 6820
***/"""


# * import the potentially usable utilities *
import sys

# * import testing tool, target files and classes *
import unittest
from HW04_Yujun_Kong_04 import count_vowels, last_occurrence, Fraction, my_enumerate


""" define glob objs """
# {format} for to print blank line
def BL():
        print()

# {/format/}
"""/* dgo end */"""


""" # CORE DEFINING BEGINS HERE # """
# --------------------------------- #

""" for to test # 01 function """
# <class> define a class for to test by using unitTest utility tool:
class CountVowelsTest(unittest.TestCase):

    def test_count_vowels(self) -> None:
        self.assertEqual(count_vowels("aeiou"), 5)

# </class>

""" for to test # 02 function """
# <class> define a class for to test by using unitTest utility tool:
class LastOccurenceTest(unittest.TestCase):

    def test_last_occurrence(self) -> None:
        self.assertEqual(last_occurrence(20, [1, 3, 5, 7, 3, 10, 20]), 6)
        self.assertNotEqual(last_occurrence(30, [1, 3, 5, 7, 3, 10, 20]), 6)

# </class>

""" for to test # 03 function """
# <class> define a class for to test by using unitTest utility tool:
class FractionTest(unittest.TestCase):

    def test_simplify(self) -> None:

        sf = Fraction(50, -250).simplify()
        
        self.assertEqual(sf, [-1, 5])
        self.assertNotEqual(sf, [10, 50])

# </class>

""" for to test # 04 function """
# <class> define a class for to test by using unitTest utility tool:
class MyEnumerateTest(unittest.TestCase):

    def test_my_enumerate(self) -> None:
        self.assertEqual(my_enumerate(['A', 'B', 'C']), [0, 'A', 1, 'B', 2, 'C'])

# </class>

# ------------------------------- #
""" # CORE DEFINING ENDS HERE # """

"""///*** define main program and execute it below ***///"""

def main():

    pass

"""///*** main program ends ***///"""

"""///*** main program execute below ***///"""

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)

"""///*** main program ends ***///"""
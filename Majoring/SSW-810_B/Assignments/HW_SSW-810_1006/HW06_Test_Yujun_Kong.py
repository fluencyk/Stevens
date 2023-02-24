"""/*
School: Stevens Institute of Technology
---------------------------------------
Course: SSW 810 - B
Instructor: Prof. Zhongyuan Yu
Teaching Assistant: Kavish Shanghvi
-----------------------------------
Homework: # 06 / Topic: List
------------------------------------------------
Coder Name with The CWID: Yujun Kong / 1046 6820
*/"""
# //
# ===== CODING BEGINS ===== #


# * import the potentially usable utilities *
import sys

# * import the supporting types *
from typing import Any, Counter, List, Sequence, Optional, Iterator, IO

# * import testing tool, target files and classes *
import unittest
from HW06_Yujun_Kong import list_Copy, list_Intersect, list_Difference, remove_Vowels, check_Password, Donut_Queue


""" # Global Objects Begin # """
# {format} for to print blank line:
def BL():
    print ()

# {format} for to print a separating line:
def SL():
    print ('-'*100)

# {format} for to print if some codes are okay:
def OK():
    print ('Okay')

# {/format/}
""" # /Global Objects End # """


""" # CORE DEFINING BEGINS HERE # """
# --------------------------------- #

""" for to test # 01 function """
# <class> define a class for to test by using unitTest utility tool:
class List_Copy_Test(unittest.TestCase):

    def test_list_Copy(self) -> None:

        self.assertEqual( list_Copy(['x', 'y', 'z']), ['x', 'y', 'z'] )
        self.assertNotEqual( list_Copy(['x', 'y', 'z']), ['r', 's', 't'] )

# </class>

""" for to test # 02 function """
# <class> define a class for to test by using unitTest utility tool:
class List_Intersect_Test(unittest.TestCase):

    def test_list_Intersect(self) -> None:
        
        self.assertEqual( list_Intersect([10, 20, 30], [10, 15, 30]), [10, 30] )
        self.assertNotEqual( list_Intersect([10, 20, 30], [10, 20, 300]), [10, 30] )

# </class>

""" for to test # 03 function """
# <class> define a class for to test by using unitTest utility tool:
class List_Difference_Test(unittest.TestCase):

    def test_list_Difference(self) -> None:

        self.assertEqual( list_Difference([5, 6, 7], [5, 10, 7]), [6] )
        self.assertNotEqual( list_Difference([1, 3, 5], [1, 5, 7]), [30] )

# </class>

""" for to test # 04 function """
# <class> define a class for to test by using unitTest utility tool:
class Remove_Vowels_Test(unittest.TestCase):

    def test_remove_Vowels(self) -> None:

        self.assertEqual( remove_Vowels('Akira is amazing Vitra Fighter character'), 'Vitra Fighter character' )
        self.assertNotEqual( remove_Vowels('Akira is amazing Vitra Fighter character'), 'Akira is mazing Vitra Fighter character' )
       
       

# </class>

""" for to test # 05 function """
# <class> define a class for to test by using unitTest utility tool:
class Check_Password_Test(unittest.TestCase):

    def test_check_Password(self) -> None:
       
       self.assertTrue( check_Password('007_James_Bond') )
       self.assertFalse( check_Password('Steve-Jobs') )


# </class>

""" for to test # 06 class """
# <class> define a class for to test by using unitTest utility tool:
class Donut_Queue_Test(unittest.TestCase):

    def test_Donut_Queue(self):

        dq = Donut_Queue()

        self.assertIsNone(dq.next_customer())
        dq.arrive("Candy", False)
        dq.arrive("Dina", False)
        dq.arrive("Armstrong", True)
        dq.arrive("Emma", False)

        self.assertEqual(dq.waiting(), "Armstrong, Candy, Dina, Emma")

        dq.arrive("Bianca", True)

        self.assertEqual(dq.waiting(), "Armstrong, Bianca, Candy, Dina, Emma")

        self.assertEqual(dq.next_customer(), "Armstrong")
        self.assertEqual(dq.next_customer(), "Bianca")
        self.assertEqual(dq.next_customer(), "Candy")

        self.assertEqual(dq.waiting(), "Dina, Emma")
        self.assertEqual(dq.next_customer(), "Dina")
        self.assertEqual(dq.next_customer(), "Emma")
        self.assertIsNone(dq.next_customer())

# </class>

# ------------------------------- #
""" # CORE DEFINING ENDS HERE # """


"""///*** main program execute below ***///"""

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)

"""///*** main program ends ***///"""

# ===== CODING ENDS ===== #
# ///

"""/*
School: Stevens Institute of Technology
---------------------------------------
Course: SSW 810 - B
Instructor: Prof. Zhongyuan Yu
Teaching Assistant: Kavish Shanghvi
-----------------------------------
Homework: # 08 / Parameters and Modules
------------------------------------------------
Coder Name with The CWID: Yujun Kong / 1046 6820
*/"""
# //
# ===== CODING BEGINS ===== #


# * import the potentially usable utilities *
import sys

# * import the supporting types *
from typing import Optional, List, Tuple, DefaultDict, Set

# * import testing tool, target files and classes *
import unittest
from HW08_Yujun_Kong import date_arithmetic, file_reader, FileAnalyzer


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
# <class>
class Date_Arithmetic_Test(unittest.TestCase):

    def test_date_arithmetic(self) -> None:

        self.assertEqual( date_arithmetic(), ('Mar 02, 2021', 'Mar 01, 2020', 124) )
        self.assertNotEqual( date_arithmetic(), ('Mar 02, 9021', 'Mar 01, 9020', 421) )

# </>

""" for to test # 02 function """
# <class>
class File_Reader_Test(unittest.TestCase):

    def test_file_reader(self) -> None:
        
        self.assertNotIn( "This legal No.6 line's content is ('100', 'William', 'Customer Service').", file_reader('Reader_Test.txt', 3) )

# </>

""" for to test # 03 function """
# <class>
class FileAnalyzer_Test(unittest.TestCase):

    def test_FileAnalyzer(self) -> None:

        fa = FileAnalyzer("HW08_Attached-Files/")

        self.assertIn( 'HW07_Test_Sample.py', fa.files_summary )
        self.assertNotIn( 'HW04_Test_Sample.py', fa.files_summary )

# </>

# ------------------------------- #
""" # CORE DEFINING ENDS HERE # """


"""///*** main program execute below ***///"""

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)

"""///*** main program ends ***///"""

# ===== CODING ENDS ===== #
# ///

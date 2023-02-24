"""/*
School: Stevens Institute of Technology
---------------------------------------
Course: SSW 810 - B
Instructor: Prof. Zhongyuan Yu
Teaching Assistant: Kavish Shanghvi
-----------------------------------
Homework: # 07 / Topic: Containers
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
from HW07_Yujun_Kong_01 import anagrams_lst, anagrams_dd, anagrams_cntr, covers_alphabet, web_analyzer


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
class Anagrams_List_Test(unittest.TestCase):

    def test_anagrams_lst(self) -> None:

        self.assertTrue( anagrams_lst( "ice tea", "eat ice" ) )
        self.assertFalse( anagrams_lst( "bill gates", "steve jobs" ) )

# </class>

""" for to test # 02 function """
# <class>
class Anagrams_DefaultDictionary_Test(unittest.TestCase):

    def test_anagrams_dd(self) -> None:
        
        self.assertTrue( anagrams_dd( "maclix", "climax" ) )
        self.assertFalse( anagrams_dd( "Justin Timberlake", "Lake Justimber" ) )

# </class>

""" for to test # 03 function """
# <class>
class Anagrams_Counter_Test(unittest.TestCase):

    def test_anagrams_cntr(self) -> None:

        self.assertTrue( anagrams_cntr( "Broad Way", "Way Board" ) )
        self.assertFalse( anagrams_cntr( "Happy Bell", "Bill Hippy" ) )

# </class>

""" for to test # 04 function """
# <class>
class Covers_Alphabet_Test(unittest.TestCase):

    def test_covers_alphabet(self) -> None:

        self.assertTrue( covers_alphabet("We promptly judged antique ivory buckles for the next prize") )
        #self.assertFalse( covers_alphabet('Akira is an amazing Vitra Fighter character') )  

# </class>

""" for to test # 05 function """
# <class>
class Web_Analyzer_Test(unittest.TestCase):
    
    def test_web_analyzer(self) -> None:

        summy_List: List = [ ('hearthstone.com', ['Jaina', 'Uther']), ('warcraft.com', ['Jaina', 'Thrall']) ]
       
        self.assertEqual( web_analyzer( [("Uther", "hearthstone.com"), ("Thrall", "warcraft.com"), ("Jaina", "warcraft.com"), ("Jaina", "hearthstone.com")] ), summy_List )

# </class>

# ------------------------------- #
""" # CORE DEFINING ENDS HERE # """


"""///*** main program execute below ***///"""

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)

"""///*** main program ends ***///"""

# ===== CODING ENDS ===== #
# ///

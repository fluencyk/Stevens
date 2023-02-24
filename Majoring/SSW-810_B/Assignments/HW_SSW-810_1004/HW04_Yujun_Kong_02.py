"""/*
School: Stevens Institute of Technology
Course: SSW 810 - B
Instructor: Zhongyuan Yu
Teaching Assistant: Kavish Shanghvi
Topic: Fractions Calculation
Coder Name with The CWID: Name: Yujun Kong / CWID: 1046 6820
*/"""


# * import the potentially usable utilities *
import sys

# * import testing tool, target files and classes *
import unittest
from typing import Optional


""" define glob objs """
# {format} for to print blank line
def BL():
        print()

# {/format/}
"""/* dgo end */"""


""" define functions """

""" # 01 function """
# (function) define a function can return all numbers of the recieved string:
def count_vowels(s: str) -> int:
    
    counter:int = 0

    for i in s:
        #print(i)
        counter = counter + 1
        
    #print(counter)
    return counter

# (/function)
# <class> define a class for to test by using unitTest utility tool:
class CountVowelsTest(unittest.TestCase):

    def test_count_vowels(self) -> None:
        self.assertEqual(count_vowels("aeiou"), 5)

# </class>

""" # 02 function """
# (function) define a function can return type of an arbitrary sequence to matches list or str or other:
def last_occurrence(target:int, seq:list) -> Optional[str]:

    lastIdx:int = len(seq) - 1

    lastOcc = seq[lastIdx]

    if target == lastOcc:
        return lastIdx
        #print(lastIdx)

    else:
        return None
        #print("None")

# (/function)
# <class> define a class for to test by using unitTest utility tool:
class LastOccurenceTest(unittest.TestCase):

    def test_last_occurrence(self) -> None:
        self.assertEqual(last_occurrence(20, [1, 3, 5, 7, 3, 10, 20]), 6)
        self.assertNotEqual(last_occurrence(30, [1, 3, 5, 7, 3, 10, 20]), 6)

# </class>

""" # 03 function """
# <class> define a class for to get and calculate by fraction arithmetic:
class Fraction(unittest.TestCase):

    # ((method)) define the constructor for the class:
    def __init__(self, numerator: int, denominator: int) -> None:
        if denominator == 0:            
            raise ValueError("Denominator of the fraction cannot be 0.") 
        self.numerator = numerator
        self.denominator = denominator

        #self.auto_Get_Fraction_Tuple()
        
    # ((/method))

    def auto_Get_Fraction_Tuple(self, nu, de):

        n = nu
        d = de

        ft : tuple = (n, d)

        return ft

    # ((method)) define a method for to simplify the fraction from:
    def simplify(self):

        nu = self.numerator
        de = self.denominator

        # ultimately simplifing
        if nu % de == 0:
            nu = nu // de
            de = 1

            sft : tuple = (nu, de)
            #print(f"{nu} / {de}")
            return sft

        # ultimately simplifing
        elif de % nu == 0:
            de = de // nu
            nu = 1

            sft : tuple = (nu, de)
            #print(f"{nu} / {de}")
            return sft

        # if the numerator and denominator are both negative numbers, the fraction actually is a positive fraction!
        elif (nu < 0) and (de < 0):
            nu = abs(nu)
            de = abs(de)
        
            for i in range(2, nu):
                while (nu % i == 0) and (de % i == 0):
                    nu = nu // i
                    de = de // i

            sft : tuple = (nu, de)
            #print(f"{nu} / {de}")
            return sft

        # if the numerator and denominator are both positive numbers, the fraction simplify itself under normal status.
        elif (nu > 0) and (de > 0):
        
            for i in range(2, nu):
                while (nu % i == 0) and (de % i == 0):
                    nu = nu // i
                    de = de // i

            sft : tuple = (nu, de)
            #print(f"{nu} / {de}")
            return sft

        # whatever anyone of the numerator and denominator is negative, the fraction always remains negative.
        elif (nu < 0) and (de > 0):
            nu = abs(nu)

            for i in range(2, nu):
                while (nu % i == 0) and (de % i == 0):
                    nu = nu // i
                    de = de // i

            sft : tuple = (nu, de)
            #print(f"{nu} / {de}")
            return sft

        # whatever anyone of the numerator and denominator is negative, the fraction always remains negative.
        elif (nu > 0) and (de < 0):
            de = abs(de)

            for i in range(2, nu):
                while (nu % i == 0) and (de % i == 0):
                    nu = nu // i
                    de = de // i

            sft : tuple = (nu, de)
            #print(f"{nu} / {de}")
            return sft

    # ((/method))
# </class>
# <class> define a class for to test by using unitTest utility tool:
class FractionTest(unittest.TestCase):

    def test_simplify(self) -> None:

        f = Fraction

        self.assertEqual(f(6, 18).simplify(), f(1, 3))



# (/function)

""" define ends """

"""///*** define main program and execute it below ***///"""

def main():

    #count_vowels("aeiou")

    #last_occurrence(20, [1, 3, 5, 7, 3, 10, 20])

    f = Fraction
    f(60, -30).simplify()


"""///*** main program ends ***///"""

"""///*** main program execute below ***///"""

if __name__ == '__main__':
    main()

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)

"""///*** main program ends ***///"""
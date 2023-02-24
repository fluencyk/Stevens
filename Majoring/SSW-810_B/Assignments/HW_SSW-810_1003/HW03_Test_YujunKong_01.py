"""
/*
School: Stevens Institute of Technology
Course: SSW 810 - B
Instructor: Zhongyuan Yu
Teaching Assistant: Kavish Shanghvi
Topic: Fractions Calculation
Coder Name with The CWID: Name: Yujun Kong / CWID: 1046 6820
*/
"""

# import testing tool, target file and class
import unittest
from HW03_YujunKong_01 import Fraction

""" define glob vars, cons, lists, dicts, and others """

test = 0

"""/* define vcldo ends */"""


""" define print format method """

# <define blank line>
def BL():
    print()
# <>

"""/* define pf-m ends */"""


"""/* define preset class and method */"""

# <define support-class="ezIO" for esay to re-use some repeatable codes>
class ezIO:

    def __init__(self):
        pass

    def get_Valid_InputVal(self,pmpt):

        while True:
            rawVal = input(pmpt)
            if str(rawVal).isalpha():
                print("Invalid input! The input must be a number without 0 value.")
                print("Try again...")
                continue
            elif int(rawVal) == 0:
                print("Invalid input! The input number can not be 0, which makes the fraction untanable.")
                print("Try again...")
                continue
            #Below can not be worked
            elif len(rawVal) == 0:
                print("Invalid input! The input can not contain space inputting.")
                print("Try again...")
                continue
            #Below can not be worked
            elif rawVal.isspace():
                print("Invalid input! The input can not contain space inputting.")
                print("Try again...")
                continue
            else:
                return int(rawVal)
            # I can not handle all of the odd or weird input by user's possibility. Will overcome in near future!
# <>

# <define test-class>

class Test_Fraction():

    def __init__(self) -> None:
        pass
    

# <>

"""/* define class and method ends */"""



"""///*** define main program and execute it below ***///"""

def main():

    x = Fraction()

    x.welcome()
    x.get_Frac_Calcu()

    main()

# mian program execution
if __name__ == '__main__':
    main()

"""///*** main program ends ***///"""
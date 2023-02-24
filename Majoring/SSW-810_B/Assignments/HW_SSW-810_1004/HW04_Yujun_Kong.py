"""/*
School: Stevens Institute of Technology
Course: SSW 810 - B
Instructor: Zhongyuan Yu
Teaching Assistant: Kavish Shanghvi
Homework: # 04 / Topic: Iteration
Coder Name with The CWID: Name: Yujun Kong / CWID: 1046 6820
*/"""


# * import the potentially usable utilities *
import sys

# * import testing tool, target files and classes *
import unittest
from typing import Iterator, Optional, Sequence


""" # Global Objects Begin # """
# {format} for to print blank line:
def BL():
        print()

# {/format/}
""" # Global Objects End # """


""" # CORE DEFINING BEGINS HERE # """
# --------------------------------- #

""" # 01 function """
# (function) define a function can return all numbers of the recieved string:
def count_vowels(s: str) -> int:
    
    counter:int = 0

    for i in s:

        counter = counter + 1
        
    #print(counter) # <- for self coding check:
    return counter

# (/function)


""" # 02 function """
# (function) define a function can return type of an arbitrary sequence to matches list or str or other:
def last_occurrence(target:int, seq:list) -> Optional[str]:

    lastIdx:int = len(seq) - 1

    lastOcc = seq[lastIdx]

    if target == lastOcc:
        #print(lastIdx) # <- for self coding check:
        return lastIdx
        

    else:
        #print("None") # <- for self coding check:
        return None
        

# (/function)


""" # 03 function in the class 'Fraction' """
# <class> define a class for to get and calculate by fraction arithmetic:
class Fraction:

    # ((method)) define the constructor for the class:
    def __init__(self, numerator: int, denominator: int) -> None:
        if denominator == 0:            
            raise ValueError("Denominator of the fraction cannot be 0.") 
        self.numerator = numerator
        self.denominator = denominator
        
    # ((/method))

    # ((method)) define a method for to simplify the fraction from:
    def simplify(self):

        f:list = []

        nu = self.numerator
        de = self.denominator

        # whatever anyone of the numerator and denominator is negative, the fraction always remains negative.
        if (nu < 0) and (de > 0):
            nu = abs(nu)

            for i in range(2, nu):
                while (nu % i == 0) and (de % i == 0):
                    nu = nu // i
                    de = de // i
                if nu % de == 0:
                    nu = nu // de
                    de = 1
                elif de % nu == 0:
                    de = de // nu
                    nu = 1

            nu = -nu

            f.append(nu)
            f.append(de)
            return f

        # whatever anyone of the numerator and denominator is negative, the fraction always remains negative.
        elif (nu > 0) and (de < 0):
            de = abs(de)

            for i in range(2, nu):
                while (nu % i == 0) and (de % i == 0):
                    nu = nu // i
                    de = de // i
                if nu % de == 0:
                    nu = nu // de
                    de = 1
                elif de % nu == 0:
                    de = de // nu
                    nu = 1

            nu = -nu

            f.append(nu)
            f.append(de)
            return f

        # if the numerator and denominator are both negative numbers, the fraction actually is a positive fraction!
        elif (nu < 0) and (de < 0):
            nu = abs(nu)
            de = abs(de)
        
            for i in range(2, nu):
                while (nu % i == 0) and (de % i == 0):
                    nu = nu // i
                    de = de // i
                if nu % de == 0:
                    nu = nu // de
                    de = 1
                elif de % nu == 0:
                    de = de // nu
                    nu = 1

            f.append(nu)
            f.append(de)
            return f

        # if the numerator and denominator are both positive numbers, the fraction simplify itself under normal status.
        elif (nu > 0) and (de > 0):
        
            for i in range(2, nu):
                while (nu % i == 0) and (de % i == 0):
                    nu = nu // i
                    de = de // i
                if nu % de == 0:
                    nu = nu // de
                    de = 1
                elif de % nu == 0:
                    de = de // nu
                    nu = 1

            f.append(nu)
            f.append(de)
            return f

    # ((/method))
# </class>


""" # 04 function """
# (function) define a function for to provide the functionality is like the build-in iterator:
def my_enumerate(seq: Sequence[int]) -> Iterator[int]:

    i: int = 0
    k: list = []

    for j in seq:
        
        k.append(i)
        k.append(seq[i])
        i += 1

    return k

# (/function)

# ------------------------------- #
""" # CORE DEFINING ENDS HERE # """


"""///*** define main program and execute it below ***///"""

def main():

    count_vowels("aeiou")

    last_occurrence(20, [1, 3, 5, 7, 3, 10, 20])

    f = Fraction
    f(50, -250).simplify()

    my_enumerate(['A', 'B', 'C'])


"""///*** main program ends ***///"""

"""///*** main program execute below ***///"""

if __name__ == '__main__':
    main()

"""///*** main program ends ***///"""
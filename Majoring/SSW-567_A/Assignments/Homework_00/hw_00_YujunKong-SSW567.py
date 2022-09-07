# ===== Python - UTF-8 ===== #
"""/*
School: Stevens Institute of Technology
Course: SSW 567 - A
Instructor: Prof. Andre Bondi
---------------------------------------
Topic: Homework # 00
---------------------------------------
Coder with CWID: Yujun Kong / 1046 6820
*/"""
# ===== CODING BEGINS ===== #

import sys

# <class>
class SayHello:

    # ([constructor])
    def __init__(self) -> None:
        
        self.helloSaying: str = "Hello world!"

    # ((method))
    def say(self) -> None:

        print(f"--= ' {self.helloSaying} ' =--")

# </>

# (((main)))
def main():

    s = SayHello()
    s.say()

    sys.exit()

"""///*** main program executes below ***///"""

if __name__ == '__main__':
    main()

# ===== CODING ENDS ===== #

# /// The Coding Experience and Conclusion ///
"""/'
Nope...
'/"""
# ///

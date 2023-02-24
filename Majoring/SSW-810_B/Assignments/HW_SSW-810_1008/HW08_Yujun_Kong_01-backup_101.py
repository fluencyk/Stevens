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
import sys, os

# * import the supporting types *
from typing import Optional, List, Tuple, DefaultDict, Set, Iterator, IO

# * import the supporting modules *
from datetime import datetime, timedelta


""" # Global Objects Begin # """
# {format} for to print blank line:
def BL():
    print ()

# {format} for to print a separating line:
def SL():
    print ('-' * 150)

# {format} for to print if some codes are okay:
def OK():
    print ('Okay')

# {/}
""" # /Global Objects End # """


""" # Supporting Classes Begin # """
# <class> define supporting class"ezIO" for to reuse codes:
class ezIO:

    # ([constructor]) define a constructor for class itself:
    def __init__(self):
        pass
    
    # ((method)) define a method for to print out the welcoming words:
    def welcome(self):

        welcoming = "-== Welcome to ' Parameters and Modules ' ==-"
        BL()
        print(welcoming)
        print ( '-' * len(welcoming) )
        BL()

    # ((method)) define a method for to quit the main program:
    def quit_Main(self):

        BL()
        print("--- Thanks for your checking, Bye! ---")
        BL()
        sys.exit()

# </>
""" # /Supporting Classes End # """


""" # CORE DEFINING BEGINS HERE # """
# --------------------------------- #

""" # 01 function """
# (function)
def date_arithmetic() -> Optional[ Tuple[datetime, datetime, int] ]:
    """ calculate a date before or after the pointed date. """

    date1: str = "Feb 27, 2021"
    date2: str = "Feb 27, 2020"

    date3: str = "Feb 1, 2021"
    date4: str = "Sep 30, 2020"

    dt1: datetime = datetime.strptime(date1, '%b %d, %Y')
    dt2: datetime = datetime.strptime(date2, '%b %d, %Y')

    dt3: datetime = datetime.strptime(date3, '%b %d, %Y')
    dt4: datetime = datetime.strptime(date4, '%b %d, %Y')

    three_days_number: int = 3

    date_A: datetime = dt1 + timedelta(days = three_days_number)
    date_B: datetime = dt2 + timedelta(days = three_days_number)

    return ( date_A.strftime('%b %d, %Y'), date_B.strftime('%b %d, %Y'), (dt3 - dt4).days )
       
# (/)

""" # 02 function """
# (function)
def file_reader(path: str, fields: int, sep=', ', header = False) -> Iterator[Tuple[str]]:
    """ Your docstring should go here for the description of the function."""

    # Test Path: " HW08_Attached-Files\file_Reader_Test.txt "
    
    try:
        file: IO = open(path, 'r')
    except FileNotFoundError:
        print (f"Error! Can not found the file ' {path} ' in current directory, file not exist or wrong file path.")
        sys.exit()
    with file:
        
        counter = 1
        iter: Iterator = []

        for line in file:
            tpl: tuple[str] = ( ''.join(item for item in line).strip('\n').replace('|', sep) )
            counter += 1
            try:
                if tpl[0].isnumeric():
                #try:
                    yield len(tpl)
                
                continue
            except:
                continue
                #try:
                    #yield tpl
                #except ValueError:
                    #print("AAAAAAAAAAAAAAAAAAAAAA")
            #continue
            
            
            
                
            #yield line
            

# (/)

""" # 03 function """
# <class>
class FileAnalyzer:
    """ Your docstring should go here for the description of the class."""
    def __init__(self, directory: str) -> None:
        """ Your docstring should go here for the description of the method."""
        self.directory: str = directory # NOT mandatory!
        #self.files_summary: Dict[str, Dict[str, int]] = dict() 

        self.analyze_files() # summerize the python files data

    def analyze_files(self) -> None:
        """ Your docstring should go here for the description of the method."""
        pass # implement your code here

    def pretty_print(self) -> None:
        """ Your docstring should go here for the description of the method."""
        pass # implement your code here

# </>

# ------------------------------- #
""" # CORE DEFINING ENDS HERE # """


"""///*** define main program and execute it below ***///"""
# (((main function)))
def main(): #!! <- Main Program Procedure Flow !!#

    e = ezIO() #! <- Supporting Input/Output Class !#

    e.welcome() #! <- Print Out The Header !#
    
    # // "run # 01 function"
    #print (f"The function # 01's return is ' { date_arithmetic() } '")
    #SL()
    #BL()

    # // "run # 02 function"
    fder = file_reader('HW08_Attached-Files/file_Reader_Test.txt', 3)
    print (f"The function # 02's return is ' { next(fder) } '")
    print (f"The function # 02's return is ' { next(fder) } '")
    print (f"The function # 02's return is ' { next(fder) } '")
    SL()
    BL()



    
    
    # // "quit the program"
    e.quit_Main()

# (((/main function)))

"""///*** main program execute below ***///"""

if __name__ == '__main__':
    main()

"""///*** main program define and execution ends ***///"""

# ===== CODING ENDS ===== #
# //



# /// The Coding Experience and Conclusion ///
"""/'
Dear respectable and erudite Prof. and TA,

1, I still found there're too many logical flows can not be written by the coding way of one solo "'container'-comprehensions" expression.
    I feel like someday I cound finally figure out all of the ways to conduct the lowest-compexity programming expertise.

Yujun Kong
'/"""
# ///
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
from typing import Optional, List, Tuple, Dict, DefaultDict, Set, Iterator, IO

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
    """ Calculate a date before or after the pointed date, and calculate the days between two date. """

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
def file_reader(path: str, fields: int, sep = ',', header: bool = False) -> Optional [ Iterator[Tuple[str]] ]:
    """ Read a file to get each line's data fields and judge which has incomplete data fields and response its info. """

    # Test Path: " HW08_Attached-Files/file_Reader_Test.txt "
    
    try:
        file: IO = open(path, 'r')
    except FileNotFoundError:
        print (f"Error! Can not found the file ' {path} ' in current directory, file not exist or wrong file path.")
        sys.exit()
    with file:        
        counter = 0
        for line in file:
            line = line.strip('\n').replace('|', sep)
            tpl: tuple = tuple( item for item in line.split(sep) )            
            counter += 1
            
            try:
                header = tpl
                if header[0].isalpha():
                    print(f"This No.{counter} line with its content of ' {tpl} ' is the header of the file: {path[path.find('/')+1 : ]}.")
                    continue
                elif (tpl[0].isdigit()) and (len(tpl) != fields):
                    raise ValueError
                  
            except:
                print(f"In No.{counter} line of the file: {path[path.find('/')+1 : ]}, there's an value error:")
                print(f"    ^ The line's fields is '{len(tpl)}', yet the expected fields is '{fields}'.")
                continue

            else:
                print(f"This legal No.{counter} line's content is {tpl}.")
                yield tpl
            
    file.close()

# (/)

""" # 03 function """
# <class>
class FileAnalyzer:
    """ Analyze and summarize each file's detailed quantity info about its function, class, method. """

    # ((method))
    def __init__(self, directory: str) -> None:
        """ Get analyzed summary info from the Python files and then package as a dictionary. """

        self.directory: str = directory # NOT mandatory!
        #self.files_summary: Dict[str, Dict[str, int]] = self.analyze_files()

        #print(self.files_summary)

        self.analyze_files() # summerize the python files data
    # ((/))

    # ((method))
    def analyze_files(self) -> Optional[ Dict ]:
        """ Pinpoint the current working dir, scan it, get Python files, then analyze. """

        try:
            setCurDir = os.chdir(self.directory)
            if setCurDir == False:
                raise FileNotFoundError
        except:
            print(f"Error! The directory: '{self.directory}' do not exist or pointed directory: '{self.directory}' is incorrect.")
        else:
            cwDir = os.listdir(os.getcwd())
            pyFiles: List = [ file for file in cwDir if '.py' in file ]
            #print(pyFiles)
            try:
                if len(pyFiles) == 0:
                    raise FileNotFoundError
            except:
                print("There're no Python files in current directory.")
        
        for pyF in pyFiles:

            pyF_ClassNum: int = 0
            pyF_FuncNum: int = 0
            pyF_LineNum: int = 0
            pyF_CharNum: int = 0
            
            eachPyFile: IO = open(pyF, 'r')
            with eachPyFile:                

                for line in eachPyFile:
                    pyF_LineNum += 1
                    
                    pureline = line.rstrip()
                    if 'class' == pureline[0 : 5]:
                        pyF_ClassNum += 1
                        #print(pureline)
                    if 'def' == pureline[0 : 3]:
                        pyF_FuncNum += 1
                        #print(pureline)
                    charNum: int = 0
                    for char in line:
                        charNum += 1

                    pyF_CharNum += charNum
                        
                #print(pyF)
                #BL()
                #print(f"Classes: {pyF_ClassNum}")
                #print(f"Functions: {pyF_FuncNum}")
                #print(f"Lines: {pyF_LineNum}")
                #print(f"Characters: {pyF_CharNum}")
                #BL()

                pyF_AnalyzedSumInfo: Dict = { pyF: {'Class': pyF_ClassNum, 'Function': pyF_FuncNum, 'Line': pyF_LineNum, 'Character': pyF_CharNum} }
                #print(pyF_AnalyzedSumInfo)
                BL()
                return pyF_AnalyzedSumInfo

    # ((/))

    # ((method))
    def pretty_print(self) -> None:
        """ Your docstring should go here for the description of the method."""

        pass # implement your code here
    # ((/))

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
    #fder = file_reader('HW08_Attached-Files/Reader_Test.txt', 3)
    #lines_counter = 9
    #for i in fder:
        #if i == lines_counter:
            #break
    #SL()
    #BL()

    # // "run # 03 class"
    FileAnalyzer("HW08_Attached-Files/")
    #osm.analyze_files()
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

1, 

Yujun Kong
'/"""
# ///
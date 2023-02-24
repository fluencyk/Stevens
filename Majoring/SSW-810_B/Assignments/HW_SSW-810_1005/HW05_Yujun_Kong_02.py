"""/*
School: Stevens Institute of Technology
-------------------
Course: SSW 810 - B
Instructor: Prof. Zhongyuan Yu
Teaching Assistant: Kavish Shanghvi
-----------------------------------
Homework: # 05 / Topic: Strings, Files and Coding Style
-------------------------------------------------------
Coder Name with The CWID: Name: Yujun Kong / CWID: 1046 6820
*/"""
# //

# # # Coding Begins # # #


# * import the potentially usable utilities *
import sys

# * import the supporting types *
from typing import Any, List, Sequence, Optional, Iterator, IO

# * import testing tool, target files and classes *
import unittest


""" # Global Objects Begin # """
# {format} for to print blank line:
def BL():
        print()

# {/format/}
""" # /Global Objects End # """


""" # Supporting Classes Begin # """
# <class> define supporting class"ezIO" for to reuse codes:
class ezIO:

    # ([constructor]) define a constructor for class itself:
    def __init__(self):
        pass
    
    # ((method)) define a method for to print out the welcoming words:
    def welcome(self):

        welcoming = "--- Welcome to String manipulation ---"
        print(welcoming)
        BL()

    # ((method)) define a method for to quit the main program:
    def quit_Main(self):

        BL()
        print("--- Thanks for your playing, Bye! ---")
        sys.exit()

    # ((method)) define a method for to get user's singular words sequence:
    def get_AnyType_Input(self, prompt) -> Optional[str]:
        
        illegal_Input_Set: str = '@#^-=_+'

        while True:
            raw_Input: Optional[str]

            try:
                raw_Input = input(prompt)
                
                for i in illegal_Input_Set:
                    if i in raw_Input:
                        print("Kidding?! Please don't input digit, try again.")
                        BL()
                        continue
                
                    elif raw_Input.isnumeric():
                        print("Kidding?! Please don't input digit, try again.")
                        BL()
                        continue
                    elif raw_Input.isspace():
                        print("Kidding?! Please don't only input space, try again.")
                        BL()
                        continue
                    elif raw_Input == "":
                        print("Kidding?! Please don't input nothing, try again.")
                        BL()
                        continue

            except ValueError:
                print(f"{raw_Input} is invalid! Please input again, thanks")
                continue

            return raw_Input
    # ((/method))

    # ((method)) define a method for to handle user's string input <- this example specifically adopts it as the program control:
    def get_String_Input(self, prompt) -> str:
        
        while True:
            raw_Input: str = ""
            try:
                raw_Input = input(prompt)
                return raw_Input
            except ValueError:
                print(f"{raw_Input} is a invalid input! Please try again, thanks")
                continue

# </class>
""" # /Supporting Classes End # """


""" # CORE DEFINING BEGINS HERE # """
# --------------------------------- #

""" # 01 function """
# (function) define a function for to reverse the order of a gotten string:
def my_Reverse(seq: str) -> str:

    max_Index: int = len(seq) - 1

    i = max_Index

    reversed_Seq: list = []

    while True:

        reversed_Seq.append(seq[i])
        i = i - 1

        if i < 0:
            break

    combined_Reversed_Seq = ' '.join(reversed_Seq)
    print (combined_Reversed_Seq)
        
# (/function)

""" # 02 function """
# (function) define a function for to find a target in a sequence to return its offset of the first index of the target:
def my_Substring(target: str, seq: str) -> str:

    tb: int = target[0]
    counter: int = 0

    for x_Letter in seq:

        if x_Letter != tb:
            counter = counter + 1

        elif x_Letter == tb:
            print (counter)

# (/function)

""" # 03 function """
# (function) define a function for to find the second occurrence content in a string matches the user input to return the offset:
def find_Second(key: str, seq: str) -> str:

    counter: int = -1
    finding_Iterator: int = 0

    temp_Stored_Slices: str = ''
    tss = temp_Stored_Slices

    out_Stack_Finding_Point: int = len(seq) - 1

    headOf_Slice_Index = 0
    tailOf_Slice_Index = len(key)

    hix = headOf_Slice_Index
    tix = tailOf_Slice_Index
    
    i = 0

    while (len(key) > 0) and (len(seq) > 0):

        tss = seq[hix : tix]
        counter = counter + 1

        if counter > out_Stack_Finding_Point:

            print ('Oops!')
            break

        elif tss != key:

            hix = hix + 1
            tix = tix + 1
            continue

        elif tss == key:

            hix = hix + 1
            tix = tix + 1

            finding_Iterator = finding_Iterator + 1

            if finding_Iterator == 1:
                continue

            elif finding_Iterator == 2:
                print (counter)
                break

# (/function)

""" # 04 function """
# (function) define a function for to find, and open a file and then read, write it:
def get_lines(target_FileName_withPath: str) -> Iterator[str]:

    try:
        target_file: IO = open(target_FileName_withPath, 'r')
    except FileNotFoundError:
        print (f'Not Found! {target_FileName_withPath} is not existed')
    else:
        with target_file:

            all_Lines: str = target_file.readlines()

            new_All_Lines: list = []

            for single_Line in all_Lines:

                backslash_Char_Index :int = single_Line.find('\\')

                if backslash_Char_Index:

                    single_Line.rsplit()
                    
                    new_Single_Line = single_Line[0:backslash_Char_Index]

                    new_All_Lines.append(new_Single_Line)

                    #combined_StringLine: list = []

                    #while True:

                        #combined_StringLine.append(new_Single_Line)

                        #print (combined_StringLine)
                        #break

                elif '\\' not in single_Line:

                    single_Line.rsplit()

                    new_All_Lines.append(single_Line)

                    #print (new_All_Lines)

                    #print (new_Single_Line)

                    #w = ''.join(new_Single_Line)

                    #print (w)

                    

                    #combined_StringLine.append(new_Single_Line)

                    #y = '\n'.join(combined_StringLine)

                    #print (y)

                    #new_Combined_StringLine.join(new_Single_Line)

                    #print (combined_StringLine)

                    #new_All_Lines.append(combined_StringLine)

            for line_By_Line in new_All_Lines:
                x = ''.join(line_By_Line)
                print (x)

            #print (new_All_Lines)

                    
            
            #for new_Single_Line in als:

                #comment_Char_Index: int = single_Line.find('#')

                #if comment_Char_Index:

                    #single_Line = single_Line[0 : comment_Char_Index]

                    #print (single_Line)
                
                    #if backslash_Char_Index:

                        #print (single_Line[:backslash_Char_Index])

                        #single_Line.rstrip('\\').replace(' ', '')

                        #print (single_Line)

                    #new_Single_Line: str = ''

                    #new_Single_Line.join(single_Line[:backslash_Char_Index])

                    #print (new_Single_Line)

                    

                    

                


                



                #print (letterOnly_Combined_LineStrings)
                #break

                #for letter in line:



            



                #print (line.strip('#'))

# (/function)            
 
# ------------------------------- #
""" # CORE DEFINING ENDS HERE # """


"""///*** define main program and execute it below ***///"""

def main(): #!! <- Main Program Procedure Flow !!#

    e = ezIO() #! <- Supporting Input/Output Class !#

    #my_Reverse('abcde')

    #my_Substring('cc', 'abc')

    #find_Second('rosa', 'rosa knows another rosa')
    #find_Second('jason', 'jason beat kevin,yet kevin beat wrong jack')

    get_lines('hw05_given_file.txt')


"""///*** main program ends ***///"""


"""///*** main program execute below ***///"""

if __name__ == '__main__':
    main()

"""///*** main program ends ***///"""

# # # Coding Ends # # #
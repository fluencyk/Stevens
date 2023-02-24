"""/*
School: Stevens Institute of Technology
---------------------------------------
Course: SSW 810 - B
Instructor: Prof. Zhongyuan Yu
Teaching Assistant: Kavish Shanghvi
-----------------------------------
Homework: # 05 / Topic: Strings, Files and Coding Style
-------------------------------------------------------
Coder Name with The CWID: Yujun Kong / 1046 6820
*/"""
# //
# ===== CODING BEGINS ===== #


# * import the potentially usable utilities *
import sys

# * import the supporting types *
from typing import Any, Counter, List, Sequence, Optional, Iterator, IO


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

        welcoming = "--- Welcome to ' Topic: Strings, Files and Coding Style ' ---"
        BL()
        print(welcoming)
        BL()

    # ((method)) define a method for to quit the main program:
    def quit_Main(self):

        BL()
        print("--- Thanks for your checking, Bye! ---")
        BL()
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
    # ((/method))

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

    combined_Reversed_Seq = ''.join(reversed_Seq)
    return combined_Reversed_Seq
    
    # // finnal self verification
    if combined_Reversed_Seq == 'e d c b a': # <- for to verify if the function runs okay #
        print ('Okay :)')
    else:
        print ('! Oops...')
        
# (/function)

""" # 02 function """
# (function) define a function for to find a target in a sequence to return its offset of the first index of the target:
def my_Substring(target: str, seq: str) -> str:

    firstlyIndexed_Offset_InSeq:int = 0
    fix = firstlyIndexed_Offset_InSeq
    lastlyIndexed_Offset_InSeq:int = len(target)
    lax = lastlyIndexed_Offset_InSeq

    consecutively_Captured_Slice = seq[fix : lax]
    #print (consecutively_Captured_Slice)

    pinpointed_Offset:int = 0
    
    while (len(target) > 0) and (len(seq) > 0):
        
        consecutively_Captured_Slice = seq[fix : lax]

        if len(target) > len(seq):
            
            print (f"'{target}' is longer than '{seq}', can not apply the finding comparison! The program terminated.")
            break
        
        elif target not in seq:

            #print ('Finding is now out of the stack!')
            #break
            return -1

        elif consecutively_Captured_Slice != target:

            fix += 1
            lax += 1
            pinpointed_Offset += 1
        
        elif consecutively_Captured_Slice == target:

            #print (pinpointed_Offset)
            #break
            return pinpointed_Offset

        else:
            return -1
                         
# (/function)

""" # 03 function """
# (function) define a function for to find the second occurrence content in a string matches the user input to return the offset:
def find_Second(key: str, seq: str) -> int:

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

            #print ('Oops!')
            break

        elif tss != key:

            hix = hix + 1
            tix = tix + 1
            continue

        elif tss == key:

            hix = hix + 1
            tix = tix + 1

            finding_Iterator = finding_Iterator + 1
            restSlice:str = seq[counter+len(key) : len(seq)]
            #print (restSlice)

            if (finding_Iterator == 1) and (key not in restSlice):
                return -1

            elif finding_Iterator == 2:
                return (counter)
                break

# (/function)

""" # 04 function """
# (function) define a function for to find, and open a file and then read, write it:
def get_Lines(target_FileName_withPath: str) -> Iterator[str]:

    try:
        target_file: IO = open(target_FileName_withPath, 'r')
    except FileNotFoundError:
        print (f'Not Found! {target_FileName_withPath} is not existed')
    else:
        with target_file:

            all_Lines: str = target_file.readlines()

            backslashFree_Lines: list = []
            for single_Line in all_Lines:

                first_IndexOf_SingleLine: int = single_Line[0]
                fix = first_IndexOf_SingleLine
                last_IndexOf_SingleLine: int = len(single_Line) - 1
                lax = last_IndexOf_SingleLine

                backslashChar_Index: int = single_Line.find('\\')

                if fix == '#':
                    continue

                elif (lax == '>') or (lax != '\\'):
                    single_Line = single_Line[: backslashChar_Index]
                    backslashFree_Lines.append(single_Line)

            #print (backslashFree_Lines)
            #return

            commentsFree_Lines: list = []
            array_Line: str = ''
            for array_Line in backslashFree_Lines:

                commentsChar_Index: int = array_Line.find('#')

                if '#' in array_Line:
                    array_Line = array_Line[: commentsChar_Index]
                    commentsFree_Lines.append(array_Line)

                elif array_Line[0] == 'm':
                    continue

                else:
                    commentsFree_Lines.append(array_Line)

            purified_Lines = ''.join(commentsFree_Lines)
            #print (purified_Lines)


            i: int = 0
            x: int = 0
            y: int = 0       

            final_Result_Lines: list = []
            for letter in purified_Lines:
                
                i = i + 1                

                if letter == '<':
                    
                    x = i              

                elif letter == '>':

                    y = i

                    #return purified_Lines[x-1 : y ]

                    final_Result_Lines.append( purified_Lines[x-1 : y ] )

            showOff = '\n'.join(final_Result_Lines)
            return showOff

# (/function)            
 
# ------------------------------- #
""" # CORE DEFINING ENDS HERE # """


"""///*** define main program and execute it below ***///"""
# (((main function)))
def main(): #!! <- Main Program Procedure Flow !!#

    e = ezIO() #! <- Supporting Input/Output Class !#

    e.welcome()

    # // "run # 01 function"
    print (f"The function # 01's return is ' { my_Reverse('abcde') } '")
    BL()

    # // "run # 02 function"
    print (f"The function # 02's return is ' { my_Substring('789', '456789') } '")
    BL()

    # // "run # 03 function"
    print (f"The function # 03's return is ' { find_Second('joe', 'joe-is-joe') } '")
    BL()

    # // "run # 04 function"
    print (f"The function # 04's return is:\n{ get_Lines('hw05_given_file.txt') }")

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

The 4th function can not be dare adopted by 'yield' method due to without full grasp because still can not be very clear about the mechanism.
And feel like some parts of the code are still inefficient and verbose. Will mend or refine this script later.

Yujun Kong
'/"""
# ///
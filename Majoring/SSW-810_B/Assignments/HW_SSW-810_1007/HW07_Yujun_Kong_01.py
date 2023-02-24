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

# * import the supporting build-in functions *
from collections import defaultdict, Counter
import typing


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

        welcoming = "-== Welcome to ' Topic: Containers ' ==-"
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

# </class>
""" # /Supporting Classes End # """


""" # CORE DEFINING BEGINS HERE # """
# --------------------------------- #

""" # 01.01 function """
# (function)
def anagrams_lst(str1: str, str2: str) -> Optional[bool]:
    """define a function for to return if str1 and str2 is a pair of anagrams:"""

    return True if sorted( [character for character in str1] ) == sorted( [ letter for letter in str2 ] ) else False
       
# (/function)

""" # 01.02 function """
# (function)
def anagrams_dd(str1: str, str2: str) -> Optional[bool]:
    """define a function for to return if str1 and str2 is a pair of anagrams:"""

    dd: DefaultDict[str, int] = defaultdict(int)

    for character in str1:
        dd[character] += 1

    for letter in str2:
        dd[letter] -= 1

    zeq = [ value for key, value in dd.items() ]
    
    for i in zeq:
        z: int = i + i

    return True if z == 0 else False
        

# (/function)

""" # 01.03 function """
# (function)
def anagrams_cntr(str1: str, str2: str) -> Optional[bool]:
    """define a function for to return if str1 and str2 is a pair of anagrams:"""

    a: typing.Counter[str] = Counter(str1)
    b: typing.Counter[str] = Counter(str2)

    return True if a == b else False

# (/function)

""" # 02 function """
# (function)
def covers_alphabet(sentence: str) -> Optional[bool]:
    """define a function for to return if its parameter(argument) covers the alphabet:"""
    
    alphabet_Set: Set = set('abcdefghijklmnopqrstuvwxyz')
    alphabet_List: List = sorted( [ element for element in alphabet_Set ] )

    sentence_Seq: List = sorted( [ letter for letter in sentence.lower() if letter in alphabet_List ] )
    
    purified_Seq: List = []
    [ purified_Seq.append(character) for character in sentence_Seq if character not in purified_Seq ]

    return True if purified_Seq == alphabet_List else False

# (/function)

""" # 03 function """
# (function)
def web_analyzer( weblogs: List[ Tuple [str, str] ] ) -> List[ Tuple [str, List[str] ] ]:
    """define a function for to return a refined log-list in the order of the visited websites: """

    sum_Result: List = []
    
    a = [ each_Blog[1] for each_Blog in weblogs ]
    b = [ each_Blog[0] for each_Blog in weblogs ]

    websites: List = []
    [ websites.append(site) for site in a if site not in websites ]

    names: List = []
    [ names.append(person) for person in b if person not in names ]

    for each_Website_Visited in websites:
        each_Who_Visited:tuple = ( each_Website_Visited, sorted( [ item[0] for item in weblogs if each_Website_Visited in item ] ) )
        sum_Result.append(each_Who_Visited)

    return sorted(sum_Result)

# (/function)

# ------------------------------- #
""" # CORE DEFINING ENDS HERE # """


"""///*** define main program and execute it below ***///"""
# (((main function)))
def main(): #!! <- Main Program Procedure Flow !!#

    e = ezIO() #! <- Supporting Input/Output Class !#

    e.welcome() #! <- Print Out The Header !#
    
    # // "run # 01.01 function"
    print (f"The function # 01.01's return is ' { anagrams_lst('own book', 'book now') } '")
    BL()

    # // "run # 01.02 function"
    print (f"The function # 01.02's return is ' { anagrams_dd('bark', 'brak') } '")
    BL()

    # // "run # 01.03 function"
    print (f"The function # 01.03's return is ' { anagrams_cntr('own book', 'cook now') } '")
    BL()

    # // "run # 02 function"
    print (f"The function # 02's return is ' { covers_alphabet('We promptly judged antique ivory buckles for the next prize') } '")
    BL()

    # // "run # 03 function"
    print (f"The function # 03's return is ' { web_analyzer( [ ('Vivian', 'bitcoin.org'), ('Bianca', 'apple.com'), ('Coco', 'bitcoin.org'),('Gul Dan', 'chase.com'), ('Vivian', 'apple.com'), ('Boss', 'chase.com'), ('Coco', 'apple.com') ] ) } '")
    BL()
    SL()
    
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
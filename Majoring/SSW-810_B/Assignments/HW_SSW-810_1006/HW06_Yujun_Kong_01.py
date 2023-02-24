"""/*
School: Stevens Institute of Technology
---------------------------------------
Course: SSW 810 - B
Instructor: Prof. Zhongyuan Yu
Teaching Assistant: Kavish Shanghvi
-----------------------------------
Homework: # 06 / Topic: List
------------------------------------------------
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
    print ()

# {format} for to print a separating line:
def SL():
    print ('-'*100)

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

        welcoming = "-== Welcome to ' Topic: List ' ==-"
        BL()
        print(welcoming)
        print ('-'*34)
        BL()

    # ((method)) define a method for to quit the main program:
    def quit_Main(self):

        BL()
        print("--- Thanks for your checking, Bye! ---")
        BL()
        sys.exit()

    # ((method)) define a method for to get user's string like words sequence:
    def get_String_Like_Input(self, prompt: Any) -> Optional[str]:

        while True:       
            raw_Input: str = input(prompt)
            pure_Input: str = ''.join( raw_Input.split() )

            if pure_Input == '':
                print("Oops... Please don't input nothing, try again.")
                BL()
                continue         
                        
            elif pure_Input.isalpha() == False:
                print("Oops... Please input ONLY letter in ALPHABET, try again.")
                BL()
                continue            
            
            else:
                try:            
                    return pure_Input
                except ValueError:            
                    print(f"{pure_Input} is not a number. please enter the number again.")

    # ((/method))

# </class>
""" # /Supporting Classes End # """


""" # CORE DEFINING BEGINS HERE # """
# --------------------------------- #

""" # 01 function """
# (function) define a function for to return a copied list:
def list_Copy(l: List[Any]) -> List[Any]:
    
    result = [ item for item in l ]

    return result
        
# (/function)

""" # 02 function """
# (function) define a function for to return all mutual items in two lists:
def list_Intersect(list_01: List[Any], list_02: List[Any]) -> List[Any]:
    
    result = [ i for i in list_01 for j in list_02 if i == j ]

    return result
       
# (/function)

""" # 03.01 function """
# (function) define a function for to return all different items in two lists:
def list_Difference(list_A: List[Any], list_B: List[Any]) -> List[Any]:
    
    result = [ i for i in list_A if i not in list_B ]

    return result

# (/function)

""" # 03.02 function """
# (function) define a function for to return all different items in two lists: # <- it's a self try for improving the understand.
def list_Difference_forFun(list_X: List[Any], list_Y: List[Any]) -> List[Any]:
    
    result = [ f'{j} is even number' if j % i == 0 else f'{j}/{i}, the remainder is {j % i}' for j in list_Y for i in list_X ]

    return result

# (/function)

""" # 04 function """
# (function) define a function for to return a filtered string without vowels started letter:
def remove_Vowels(string: str) -> str:

    vowels_Set = 'aeiouAEIOU'
    word_Sequence = ' '.join ( [vowelFree_Word for vowelFree_Word in [raw_Word for raw_Word in string.split()] 
    if vowelFree_Word[0] not in vowels_Set ] )
    
    return word_Sequence

# (/function)

""" # 05 function """
# (function) define a function for to return if True or False of the password's verification:
def check_Password(password: str) -> bool:

    upper_Counter:int = sum( [1 for upper_Check in password if upper_Check.isupper()] )
    lower_Counter:int = sum( [1 for lower_Check in password if lower_Check.islower()] )
    digit_Counter:int = sum( [1 if password[0].isdigit() else 0 ] )

    result = ( True if (upper_Counter > 1) and (lower_Counter > 0) and (digit_Counter > 0) else False ) 

    return result

# (/function)

""" # 06 class' functions """
# <class> define a class for to learn how to manipulate the list as queues:
class Donut_Queue():

    e = ezIO()
   
    def __init__(self) -> List: # <- constructor.
        
        self._vip_Customers: List = []
        self._mun_Customers: List = []
        self._all_Customers: List = []
        

    def __append_mun__(self, value: str) -> List: # <- private method to form the mundane customers list.
        
        self._mun_Customers.append(value)

        return self._mun_Customers


    def __append_vip__(self, value: str) -> List: # <- private method to form the vip customers list.

        #vip_Order_Counter: int = 0

        self._vip_Customers.append(value)

        return self._vip_Customers
    
    
    def __pop_out__(self) -> str: # <- private method for to pop out and return a list item as stack like data structure.
        
        return self._all_Customers.pop(0)

        
    def arrive(self, name: str, vip: bool) -> str: # <- form a all customers list.

        vip_Order_Counter: int = 0
        
        if vip == True:
            name = self.__append_vip__(name)

        elif vip == False:
            name = self.__append_mun__(name)
      
        self._all_Customers = self._vip_Customers + self._mun_Customers

        #self._all_Customers = self._vip_Customers

    
    def waiting(self) -> Optional[str]: # <- form a waiting list for all customers.

        if len( self._all_Customers ) == 0:

            #print ("Here's no more customers are waiting now...")

            return None

        elif len( self._all_Customers ) > 0:

            string_Merged_CustomersList: str = ','.join( ' ' + customer for customer in self._all_Customers )
            #string_Merged_CustomersList

            return string_Merged_CustomersList.lstrip()
    
    
    def next_customer(self) -> Optional[str]: # <- call a customer to serve that means pop out a item from the queue like list.

        if len( self._all_Customers ) == 0:

            #print ("Here's no more customers are waiting now...")

            return None

        elif len( self._all_Customers ) > 0:

            #print (f"* {self._all_Customers[0]} is now got served *")

            return self.__pop_out__()

# </class>

# ------------------------------- #
""" # CORE DEFINING ENDS HERE # """


"""///*** define main program and execute it below ***///"""
# (((main function)))
def main(): #!! <- Main Program Procedure Flow !!#

    e = ezIO() #! <- Supporting Input/Output Class !#
    dq = Donut_Queue()

    e.welcome()

    # // "run # 01 function"
    print (f"The function # 01's return is ' { list_Copy(['a', 'b', 'c']) } '")
    BL()

    # // "run # 02 function"
    print (f"The function # 02's return is ' { list_Intersect([1, 2, 4], [1, 2, 3]) } '")
    BL()

    # // "run # 03.01 function"
    print (f"The function # 03.01's return is ' { list_Difference([4, 5, 6], [1, 2, 3]) } '")
    BL()
    
    # // "run # 03.02 function"
    print (f"The function # 03.02's return is ' { list_Difference_forFun([2], [4, 5, 6]) } '")
    BL()

    # // "run # 04 function"
    print (f"The function # 04's return is ' { remove_Vowels('Amy is my favorite daughter') } '")
    BL()

    # // "run # 05 function"
    print (f"The function # 05's return is ' { check_Password('1046-6820_Yujun-Kong') } '")
    BL()
    SL()
    SL()
    SL()
    BL()

    # // "run # 06 class' functions"
    """ The belowing is the initial set for to test the class ' Donut_Queue 's functionality if okay or not """
    dq.arrive('Clark', False)
    dq.arrive('David', False)
    dq.arrive('Edwin', False)
    dq.arrive('Abby', True)
    dq.arrive('Bianca', True)
    # ///
    
    print ( "The Present Customers in 'Eugene's' Donut Store Are:\n" )
    print ( '\n'.join( each_Customer for each_Customer in dq._all_Customers ) )
    SL()
    BL()
    # ///

    print ( "### Method 'next_customer()' ###\n" )
    print (f"The method of next_customer()'s return is ' { dq.next_customer() } '")
    BL()
    print ( "The Customers List Remains:\n" )
    print ( '\n'.join( each_Customer for each_Customer in dq._all_Customers ) )
    SL()
    BL()
    # ///

    print ( "### Method 'waiting()' ###\n" )
    print (f"The method of waiting()'s return is ' { dq.waiting() } '")
    SL()
    BL()
    # ///

    print ( "### Method 'next_customer()' ###\n" )
    print (f"The method of next_customer()'s return is ' { dq.next_customer() } '")
    BL()
    print ( "The Customers List Remains:\n" )
    print ( '\n'.join( each_Customer for each_Customer in dq._all_Customers ) )
    SL()
    BL()
    # ///
    
    # // for to test if the method 'next_customer()' will return None when there're no any customer:
    print ("* Now begin to serve all remaind customers *")
    BL()
    print (f"This served customer's name is {dq.next_customer()}")
    BL()
    print (f"This served customer's name is {dq.next_customer()}")
    BL()
    print (f"This served customer's name is {dq.next_customer()}")
    BL()
    # ///

    # // now the last customer have been served:
    print ("=== == = - HINT! Now all remained customers are totally served! - = == ===")
    SL()
    BL()
    # ///

    # // here's actually no more customers:
    dq.next_customer() # <- Call 'waiting()' will retune the None result: 
    print ( "### Method 'waiting()' ###\n" )
    print (f"The method of waiting()'s return is ' { dq.waiting() } '")
    SL()
    BL()
    # ///

    dq.next_customer() # <- Call 'next_customer()' will retune the None result: 
    print ( "### Method 'next_customer()' ###\n" )
    print (f"The method of next_customer()'s return is ' { dq.next_customer() } '")
    SL()
    BL()
    # ///
    
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

1, When I try to implement the 'List Comprehensions', I found there's very hard to mix the 'elif' statement into the Comprehensions.
   I really want to later figure out how to implement it. So I am wondering if 'elif' can not be adopted in comprehensions?

2, When I try to implement the 'list[].extend( list[] )' method into my codes, I found it will cause double lists appeared! And this
   method even is not better than to simply use '+' to emerge two list[]. Why is that???

Yujun Kong
'/"""
# ///
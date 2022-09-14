# ===== Python - UTF-8 ===== #
"""/**
School: Stevens Institute of Technology
Course: SSW 567 - A
Instructor: Prof. Andre Bondi
---------------------------------------
Topic: Homework # 01
---------------------------------------
Coder with CWID: Yujun Kong / 1046 6820
*/"""
# ===== CODING BEGINS ===== #

import sys, gc
from typing import Any, Optional

# {<supporting class with utilities>}
class Valio:

    # <(default constructor)>
    def __init__(self) -> None:
        
        pass

    # (())
    def restart_program(self) -> bool:

        command: str = ""

        while(True):
            command = input("Replay the program or quit?\nType in 'r' to replay, or 'q' to quit: ")
            if command == "r":
                return True
            elif command == "q":
                return False
            else:
                print("Invalid command! Type in again, please.") 
                continue

    # (())
    def if_positive_number(self, string: str) -> Optional[bool]:

        count: int = 0
        if string[0] != "-":
            if string.strip(".").isnumeric():
                for i in string[0:len(string) - 1]:
                    if i == ".":
                        count += 1
                        if count > 1:
                            return False
                        else:
                            return string
        else:
            return False
    
    # (())
    def get_positive_number_input(self, side_name: str) -> None:

        prompt: str = "Please input the length of side '" + side_name + "': "
        userInput: str
        intInput: int
        floatInput: float
        msg: str = "The input must be a positive number, please try again!"

        while(True):
            userInput = input(prompt)
            if userInput.isalpha() == True:
                print(msg)
                continue
            elif self.if_positive_number(userInput) == False:
                print(msg)
                continue
            elif "." in userInput:
                try:
                    floatInput = float(userInput)
                    return floatInput
                except:
                    print(msg)
                    continue
            else:
                try:
                    intInput = int(userInput)
                    return intInput
                except:
                    print(msg)
                    continue
# {</>}

# (function)
def classify_triangle(a, b, c) -> Optional[str]:
  
    triangle_class_name: str

    if a == b == c:
        triangle_class_name = "Equilateral"

    if (a == b and a != c) or (b == c and a != b) or (c == a and b != c) and (pow(a, 2) + pow(b, 2) != pow(c, 0), 1):
        triangle_class_name = "Isosceles"
    elif (a == b and a != c) or (b == c and a != b) or (c == a and b != c) and (pow(a, 2) + pow(b, 2) == pow(c, 0), 1):
        triangle_class_name = "Isosceles and Right"
    elif (a != b != c) and (a != c) and (pow(a, 2) + pow(b, 2) == pow(c, 2)):
        triangle_class_name = "Right"
    elif (a != b != c) and (a != c) and (pow(a, 2) + pow(b, 2) != pow(c, 2)):
        triangle_class_name = "Scalene"

    return triangle_class_name  

# (((main)))
def main():

    print("-= Welcome to the program of 'Triangle Classifying' =-\n")
    
    v = Valio()

    a = v.get_positive_number_input("a")
    b = v.get_positive_number_input("b")
    c = v.get_positive_number_input("c")
    
    #print(f"Side 'a' = {a}\nSide 'b' = {b}\nSide 'c' = {c}\n")
    print(f"\nThis triangle is ' {classify_triangle(a, b, c)} '.\n" + "-" * 50) 
    
    if v.restart_program() == False:
        print("Thanks for your operation, Bye!")
        sys.exit()
    else:
        del a, b, c
        gc.collect()
        main()

"""/** main program executes below */"""

if __name__ == '__main__':
    main()

# ===== CODING ENDS ===== #

# / The Coding Experience and Conclusion /
"""/'
Nope...
'/"""
# ///
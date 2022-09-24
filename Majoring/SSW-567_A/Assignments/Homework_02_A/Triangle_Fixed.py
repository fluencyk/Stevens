# -*- coding: utf-8 -*-
"""
School: Stevens Institute of Technology
Course: SSW 567 - A
Instructor: Prof. Andre Bondi
Topic: Homework # 02.a

Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
----- ----- -----

Fixed Sep 21, 2022
The purpose of the fixed part is to pinpoint the bugs and logical faults existed in the original coding and then fix them

@author: Yujun Kong
"""
import sys, gc
from typing import Optional # the better, for the flexibility of the functions' returning

def classify_triangle(a: float ,b: float ,c: float) -> Optional[str]: # for verifying if the triangle is a right triangle type, the integer input is not adequate, the float input shall be considered
    """ /**
    Your correct code goes here...  Fix the faulty logic below until the code passes all of 
    you test cases. 
    
    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.
    
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'
      
      BEWARE: there may be a bug or two in this code
    */ """
    # Others of coding correctness are from here...

    """ 
    # require that the input values be >= 0 and <= 200
    if a > 200 or b > 200 or c > 200:
        return 'InvalidInput'
    """ # the above condition is no needed to be restricted, The sides of a, b, and c shall be input by any value in integer or float for testing except the negative numbers
        
    """ if a <= 0 or b <= b or c <= 0: """ # <--- bug 01!
    if a <= 0 or b <= 0 or c <= 0: # Fixed the statement of 'b <= b'
        return "InvalidInput"
    
    # verify that all 3 inputs are integers  
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    """if not(isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        return 'InvalidInput';"""
      
    # This information was not in the requirements spec but 
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    """ if (a >= (b - c)) or (b >= (a - c)) or (c >= (a + b)): """ # <--- bug 02!
    if (a >= b + c) or (b >= a + c) or (c >= a + b):
        return "Not a Triangle"
        
    """
    # now we know that we have a valid triangle 
    if a == b and b == a:
        return 'Equilateral'
    elif ((a * 2) + (b * 2)) == (c * 2):
        return 'Right'
    elif (a != b) and  (b != c) and (a != b):
        return 'Scalene'
    else:
        return 'Isoceles'
    """

    # the above is the original codes, and the below is the refactor

    slope_side: float

    if (a > b and a > c) and (a < (b + c)):
        slope_side = a
        if b == c:
            if pow(slope_side, 2) == pow(b, 2) + pow(c, 2):
                return "Isosceles and Right"
            elif pow(slope_side, 2) != pow(b, 2) + pow(c, 2):
                return "Isosceles but Not Right"
        elif b != c:
            if pow(slope_side, 2) == pow(b, 2) + pow(c, 2):
                return "Right"
            else:
                return "Scalene"

    elif (b > a and b > c) and (b < (a + c)):
        slope_side = b
        if a == c:
            if pow(slope_side, 2) == pow(a, 2) + pow(c, 2):
                return "Isosceles and Right"
            elif pow(slope_side, 2) != pow(a, 2) + pow(c, 2):
                return "Isosceles but Not Right"
        elif a != c:
            if pow(slope_side, 2) == pow(a, 2) + pow(c, 2):
                return "Right"
            else:
                return "Scalene"

    elif (c > a and c > b) and (c < (a + b)):
        slope_side = c
        if a == b:
            if pow(slope_side, 2) == pow(a, 2) + pow(b, 2):
                return "Isosceles and Right"
            elif pow(slope_side, 2) != pow(a, 2) + pow(b, 2):
                return "Isosceles but Not Right"
        elif a != b:
            if pow(slope_side, 2) == pow(a, 2) + pow(b, 2):
                return "Right"
            else:
                return "Scalene"

    elif a == b == c:
        return "Equilateral"

def is_valid(user_input: str) -> bool:
    """ adding new supporting feature, validate if the user input is a numeric like string """

    count: int = 0
    if user_input.strip(".").isnumeric():
        for i in user_input:
            if i == ".":
                count += 1
                if count > 1:
                    return False
                else:
                    return True

def get_input(side_label: str) -> float:
    """ adding new supporting feature, validate if the user input is a valid string and then convert it to a float value """
    
    while(True):
        raw_input: str = input("Input the value of side " + side_label + ": ")
        if is_valid(raw_input) == False:
            print("Invalid input! Try again, please.")
            continue
        else:
            try:
                return float(raw_input)
            except ValueError:
                print("Unknown error or invalid input! Try again, please.")
                continue

def restart_program() -> bool:

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

def main():

    print("-= Set a triangle by side a, b, and c to verify if it's a valid one and classify its type =-")

    a = get_input("a")
    b = get_input("b")
    c = get_input("c")

    print(f"The triangle is ' {classify_triangle(a, b, c)} '\n")

    if restart_program() == False:
        print("Thanks for your operation, Bye!")
        sys.exit()
    else:
        del a, b, c
        gc.collect()
        main()

if __name__ == "__main__":
    main()
# -*- coding: utf-8 -*-
"""
School: Stevens Institute of Technology
Course: SSW 567 - A
Instructor: Prof. Andre Bondi
----- ----- ----- ----- -----
Topic: Homework # 05
Requirement: Using static code analysis techniques and tools
----- ----- ----- ----- -----
@author: Yujun Kong
"""
import sys

class Fraction:

    def __init__(self, nutor: int, detor: int) -> None:

        self.numerator: int = 0
        self.denominator: int = 0
        self.value: str = ""
        self.ogl_value: str = str(nutor) + "/" + str(detor)
        self.validate(nutor, detor)
        self.simplify()

    def validate(self, nu: int, de: int) -> None:

        if nu == 0:
            self.value = "0"
        if de == 0:
            print("The denominator CANNOT be Zero! Program ends.")
            sys.exit()
        if nu < 0 and de < 0:
            self.numerator = abs(nu)
            self.denominator = abs(de)
        if nu < 0:
            self.numerator = nu
            self.denominator = de
        if de < 0:
            self.numerator = 0 - nu
            self.denominator = abs(de)
        if nu > 0 and de > 0:
            self.numerator = nu
            self.denominator = de
        if nu == de:
            self.value = "1"

    def simplify(self) -> None:

        i: int = None
        a = abs(self.numerator)
        b = b = self.denominator

        if a < b:
            i = a
        elif a > b:
            i = b

        while i != None:
            if a % i == 0 and b % i == 0:
                if self.numerator < 0:
                    self.numerator = 0 - a // i
                elif self.numerator > 0:
                    self.numerator = a // i
                self.denominator = b // i
                break
            else:
                i -= 1
                
        if self.numerator == self.denominator:
            self.numerator = 1
            self.denominator = 1
        elif self.numerator < 0 and abs(self.numerator) == self.denominator:
            self.numerator = -1
            self.denominator = 1
            self.value = "-1"
        elif self.numerator != self.denominator and self.denominator == 1:
            self.value = str(self.numerator)        
        else:
            self.value = str(self.numerator) + "/" + str(self.denominator)

class Fractions_Calculator(Fraction):
    """"""
    def __init__(self) -> "None":
        
        self.nutor: int = 0
        self.detor: int = 0
        self.result: "Fraction"

    def plus(self, f1: "Fraction", f2: "Fraction") -> None:

        if f1.value == "0":
            self.nutor = f2.numerator
            self.detor = f2.denominator
        elif f2.value == "0":
            self.nutor = f1.numerator
            self.detor = f1.denominator
        elif f1.value or f2.value != "0":
            if f1.denominator == f2.denominator:
                self.nutor = f1.numerator + f2.numerator
                self.detor = f1.denominator
            elif f1.denominator != f2.denominator:
                self.nutor = f1.numerator * f2.denominator + f2.numerator * f1.denominator
                self.detor = f1.denominator * f2.denominator

        self.result = Fraction(self.nutor, self.detor)

    def minus(self, f1: "Fraction", f2: "Fraction") -> None:

        if f1.value == "0":
            self.nutor = 0 - f2.numerator
            self.detor = f2.denominator
        elif f2.value == "0":
            self.nutor = 0 - f1.numerator
            self.detor = f1.denominator
        elif f1.value or f2.value != "0":
            if f1.denominator == f2.denominator:
                self.nutor = f1.numerator - f2.numerator
                self.detor = f1.denominator
            elif f1.denominator != f2.denominator:
                self.nutor = f1.numerator * f2.denominator - f2.numerator * f1.denominator
                self.detor = f1.denominator * f2.denominator

        self.result = Fraction(self.nutor, self.detor)

    def multiply(self, f1: "Fraction", f2: "Fraction") -> None:

        if f1.value == "0" or f2.value == "0":
            self.result.value = "0"

        elif f1.value == "0" or f2.value != "0":
            self.nutor = f1.numerator * f2.numerator
            self.detor = f1.denominator * f2.denominator
            self.result = Fraction(self.nutor, self.detor)

    def devide(self, f1: "Fraction", f2: "Fraction") -> None:

        if f1.value == "0" or f2.value == "0":
            self.result.value = "0"

        elif f1.value == "0" or f2.value != "0":
            self.nutor = f1.numerator * f2.denominator
            self.detor = f1.denominator * f2.numerator
            self.result = Fraction(self.nutor, self.detor)

def main():
    
    print("Welcome to use 'Fractions-Calculator'\n")

    fa = Fraction(10, -100)
    print(f"Fraction A = '{fa.ogl_value}' = '{fa.value}', as simplified")
    fb = Fraction(-21, -70)
    print(f"Fraction B = '{fb.ogl_value}' = '{fb.value}', as simplified")
    print("\n")

    rlt = Fractions_Calculator()

    rlt.plus(fa, fb)
    print(f"So, A + B = {rlt.result.value}")

    rlt.minus(fa, fb)
    print(f"So, A - B = {rlt.result.value}")

    rlt.multiply(fa, fb)
    print(f"So, A * B = {rlt.result.value}")

    rlt.devide(fa, fb)
    print(f"So, A / B = {rlt.result.value}")

    print("\n")

    sys.exit()    

if __name__ == "__main__":
    main()
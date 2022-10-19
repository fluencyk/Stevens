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
    """ base class, fraction data type construction"""
    def __init__(self, nutor: int, detor: int) -> None:
        """ constructor """
        self.numerator: int = 0
        self.denominator: int = 0
        self.value: str = ""
        self.ogl_value: str = str(nutor) + "/" + str(detor)
        self.validate(nutor, detor)
        self.simplify()

    def validate(self, nur: int, der: int) -> None:
        """ validate if deniminator zero, process negative notation and zero value """
        if nur == 0:
            self.value = "0"
        if der == 0:
            print("The denominator CANNOT be Zero! Program ends.")
            sys.exit()
        if nur < 0 and der < 0:
            self.numerator = abs(nur)
            self.denominator = abs(der)
        if nur < 0:
            self.numerator = nur
            self.denominator = der
        if der < 0:
            self.numerator = 0 - nur
            self.denominator = abs(der)
        if nur > 0 and der > 0:
            self.numerator = nur
            self.denominator = der
        if nur == der:
            self.value = "1"

    def simplify(self) -> None:
        """ simplify fraction value """
        i: int = None
        num = abs(self.numerator)
        den = self.denominator

        if num < den:
            i = num
        elif num > den:
            i = den

        while i is not None:
            if num % i == 0 and den % i == 0:
                if self.numerator < 0:
                    self.numerator = 0 - num // i
                elif self.numerator > 0:
                    self.numerator = num // i
                self.denominator = den // i
                break
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

class FractionsCalculator(Fraction):
    """ extended class, calculation of + - * / """
    def __init__(self) -> None:
        """ constructor """
        self.nutor: int = 0
        self.detor: int = 0
        self.result: "Fraction"
        super(Fraction, self).__init__()

    def plus(self, f_1: "Fraction", f_2: "Fraction") -> None:
        """ plus method """
        if f_1.value == "0":
            self.nutor = f_2.numerator
            self.detor = f_2.denominator
        elif f_2.value == "0":
            self.nutor = f_1.numerator
            self.detor = f_1.denominator
        elif f_1.value or f_2.value != "0":
            if f_1.denominator == f_2.denominator:
                self.nutor = f_1.numerator + f_2.numerator
                self.detor = f_1.denominator
            elif f_1.denominator != f_2.denominator:
                self.nutor = f_1.numerator * f_2.denominator + f_2.numerator * f_1.denominator
                self.detor = f_1.denominator * f_2.denominator

        self.result = Fraction(self.nutor, self.detor)

    def minus(self, f_1: "Fraction", f_2: "Fraction") -> None:
        """ minus method """
        if f_1.value == "0":
            self.nutor = 0 - f_2.numerator
            self.detor = f_2.denominator
        elif f_2.value == "0":
            self.nutor = 0 - f_1.numerator
            self.detor = f_1.denominator
        elif f_1.value or f_2.value != "0":
            if f_1.denominator == f_2.denominator:
                self.nutor = f_1.numerator - f_2.numerator
                self.detor = f_1.denominator
            elif f_1.denominator != f_2.denominator:
                self.nutor = f_1.numerator * f_2.denominator - f_2.numerator * f_1.denominator
                self.detor = f_1.denominator * f_2.denominator

        self.result = Fraction(self.nutor, self.detor)

    def multiply(self, f_1: "Fraction", f_2: "Fraction") -> None:
        """ multiply method """
        if f_1.value == "0" or f_2.value == "0":
            self.result = Fraction(0, 666)

        elif f_1.value != "0" or f_2.value != "0":
            self.nutor = f_1.numerator * f_2.numerator
            self.detor = f_1.denominator * f_2.denominator
            self.result = Fraction(self.nutor, self.detor)

    def devide(self, f_1: "Fraction", f_2: "Fraction") -> None:
        """ devide method """
        if f_1.value == "0" or f_2.value == "0":
            self.result = Fraction(0, 666)

        elif f_1.value == "0" or f_2.value != "0":
            self.nutor = f_1.numerator * f_2.denominator
            self.detor = f_1.denominator * f_2.numerator
            self.result = Fraction(self.nutor, self.detor)

def main():
    """ program entrance """
    print("Welcome to use 'Fractions-Calculator'\n")

    f_a = Fraction(55, -110)
    print(f"Fraction A = '{f_a.ogl_value}' = '{f_a.value}', as simplified")
    f_b = Fraction(-39, -78)
    print(f"Fraction B = '{f_b.ogl_value}' = '{f_b.value}', as simplified")

    rlt = FractionsCalculator()

    rlt.plus(f_a, f_b)
    print(f"So, A + B = {rlt.result.value}")

    rlt.minus(f_a, f_b)
    print(f"So, A - B = {rlt.result.value}")

    rlt.multiply(f_a, f_b)
    print(f"So, A * B = {rlt.result.value}")

    rlt.devide(f_a, f_b)
    print(f"So, A / B = {rlt.result.value}")

    print("\n")
    sys.exit()

if __name__ == "__main__":
    main()

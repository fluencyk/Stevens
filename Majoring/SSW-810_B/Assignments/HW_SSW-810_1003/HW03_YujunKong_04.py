"""
/*
School: Stevens Institute of Technology
Course: SSW 810 - B
Instructor: Zhongyuan Yu
Teaching Assistant: Kavish Shanghvi
Topic: Fractions Calculation
Coder Name with The CWID: Name: Yujun Kong / CWID: 1046 6820
*/
"""

# import the potential usable utilities
import sys

""" define glob objs """

def BL():
        print()

"""/* dgo end */"""

# < define supporting class"ezIO" for reusing codes >
class ezIO:

    def __init__(self):
        pass

    def welcome(self):

        welcoming = "# Welcome to Fractions Calculation #"
        print(welcoming)
        BL()

    def quit_Main(self):

        BL()
        print("*** Thanks for your operation, Bye! ***")
        sys.exit()

    def get_Int_Input(self,pmpt):
        
        while True:
            rawInt : int
            try:
                rawInt = input(pmpt)
                return int(rawInt)
            except ValueError:
                print(f"{rawInt} is invalid! Please input again, thanks")
                continue
# <>

# ( a method for to get the fraction's numerator and denominator from the user's input )
def get_User_Fraction():
        
    e = ezIO()

    print("Please set a fraction...")
    BL

    while True:
        n = e.get_Int_Input("Input a numerator: ")
        if n == 0:
            print("The numerator can not be set as 0, please input again.")
            continue
        d = e.get_Int_Input("Input a denominator: ")

        frac = []
        frac.append(n)
        frac.append(d)

        print(f"This fraction is: {frac[0]}/{frac[1]}")
        BL

        return frac
# ()

# < define class"Fraction" >
class Fraction():

    def __init__(self, numerator:int, denominator:int):
        
        f = get_User_Fraction()
        self.numerator = numerator
        self.denominator = denominator

        numerator = f[0]
        denominator = f[1]

        nF = [int]
        nF.append(numerator)
        nF.append(numerator)

        return nF

    # ( an internal methed for to calculate by plus for the fractions )
    def __add__(self,x,y):

        nu = (x[0] * y[1]) + (y[0] * x[1])
        de = (x[1] * y[1])
        #print(f"The result is: {x[0]}/{x[1]} + {y[0]}/{y[1]} = {nu}/{de}")

        rlt = []
        rlt.append(nu)
        rlt.append(de)

        return rlt

    # ( an internal methed for to calculate by minus for the fractions )
    def __sub__(self,x,y):

        nu = (x[0] * y[1]) - (y[0] * x[1])
        de = (x[1] * y[1])
        #print(f"The result is: {x[0]}/{x[1]} - {y[0]}/{y[1]} = {nu}/{de}")

        rlt = []
        rlt.append(nu)
        rlt.append(de)

        return rlt

    # ( an internal methed for to calculate by times for the fractions )
    def __mul__(self,x,y):

        nu = (x[0] * y[0])
        de = (x[1] * y[1])
        #print(f"The result is: {x[0]}/{x[1]} * {y[0]}/{y[1]} = {nu}/{de}")

        rlt = []
        rlt.append(nu)
        rlt.append(de)

        return rlt

    # ( an internal methed for to calculate by devide for the fractions )
    def __truediv__(self,x,y):

        nu = (x[0] * y[1])
        de = (x[1] * y[0])
        #print(f"The result is: {x[0]}/{x[1]} / {y[0]}/{y[1]} = {nu}/{de}")

        rlt = []
        rlt.append(nu)
        rlt.append(de)

        return rlt

    # ( an internal methed for to calculate by compare for the fractions )
    def __eq__(self,x,y):

        if (x[0]*y[1]) == (y[0]*x[1]):
            #print(f"The result is: {x[0]}/{x[1]} equals to {y[0]}/{y[1]}")
            BL()
        elif (x[0]*y[1]) > (y[0]*x[1]):
            #print(f"The result is: {x[0]}/{x[1]} bigger than {y[0]}/{y[1]}")
            BL()
        elif (x[0]*y[1]) < (y[0]*x[1]):
            #print(f"The result is: {x[0]}/{x[1]} smaller than {y[0]}/{y[1]}")
            BL()

        return y

    # ( new internal methods in the class for to support the testing )
    def __ne__(self,other:"Fraction"):
        pass

    def __lt__(self,other:"Fraction"):
        pass

    def __le__(self,other:"Fraction"):
        pass

    def __gt__(self,other:"Fraction"):
        pass

    def __ge__(self,other:"Fraction"):
        pass
    # ()
# <>

# ( a method for to get the fraction's numerator and denominator from the user's input )
def fraction_Operation():

    # ( a method for to assert if the fractions calculation operating commond from the user is lawful )
    def optCMD():

        lawfulCMD = ['+','-','*','/','=']
        while True:
            userCMD = input("Now choose one of the operations( '+' '-' '*' '/' '=' ) to calculate: ")
                
            if userCMD not in lawfulCMD:
                print("Invalid calculation commond! please input again, thanks.")
                continue
            return userCMD

    fr = Fraction()

    e = ezIO()

    a = []

    while True:
        if len(a) == 0:
            a = get_User_Fraction()
            v = optCMD()
                
            if v == '+':
                b = get_User_Fraction()
                i = fr.__add__(a,b)
                a = i

            elif v == '-':
                b = get_User_Fraction()
                i = fr.__sub__(a,b)
                a = i

            elif v == '*':
                b = get_User_Fraction()
                i = fr.__mul__(a,b)
                a = i

            elif v == '/':
                b = get_User_Fraction()
                i = fr.__truediv__(a,b)
                a = i

            elif v == '=':
                b = get_User_Fraction()
                i = fr.__eq__(a,b)
                a = i

        else:
            len(a) == 2
            altCMD = input("Okay! Continue to type one of ( '+' '-' '*' '/' '=' ) to calculate again, or 'q' to exit: ")
            lawfulCMD = ['+','-','*','/','=','q']

            if altCMD not in lawfulCMD:
                print("Invalid calculation commond! please input again, thanks.")
                continue
                
            elif altCMD == '+':
                b = get_User_Fraction()
                i = fr.__add__(a,b)
                a = i

            elif altCMD == '-':
                b = get_User_Fraction()
                i = fr.__sub__(a,b)
                a = i

            elif altCMD == '*':
                b = get_User_Fraction()
                i = fr.__mul__(a,b)
                a = i

            elif altCMD == '/':
                b = get_User_Fraction()
                i = fr.__truediv__(a,b)
                a = i

            elif altCMD == '=':
                b = get_User_Fraction()
                i = fr.__eq__(a,b)
                a = i

            elif altCMD == 'q':
                e.quit_Main()




"""/* define class and method ends */"""



"""///*** define main program and execute it below ***///"""

def main():

    t = ezIO()
    o = Fraction

    t.welcome()
    fraction_Operation()

    main()

"""///*** main program ends ***///"""

"""///*** main program execute below ***///"""

if __name__ == '__main__':
    main()

"""///*** main program ends ***///"""
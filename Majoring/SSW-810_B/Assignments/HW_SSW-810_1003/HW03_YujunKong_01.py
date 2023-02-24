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
import sys,types


""" define glob vars, cons, lists, dicts, and others """



"""/* define vcldo ends */"""


""" define print format method """

# <define blank line>
def BL():
    print()
# <>

"""/* define pfm ends */"""


"""/* define preset class and method */"""

# <define support-class="ezIO" for esay to re-use some repeatable codes>
class ezIO:

    def __init__(self):
        pass

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

# < define main-class="Fraction" >
class Fraction_RW():

    def welcome(self):

        welcoming = "# Welcome to Fractions Calculation #"
        print(welcoming)
        BL()

    # < rewrite fraction class' core methods >
    def __init__(self) -> None:
        pass

    def get_User_Fraction(self):

        e = ezIO()

        print("Please set a fraction...")
        BL()

        while True:
            n = e.get_Int_Input("Please Input a numerator: ")
            if n == 0:
                print("The numerator can not be set as 0, please input again.")
                continue
            d = e.get_Int_Input("Please Input a denominator: ")
            if d == 0:
                print("The numerator can not be set as 0, please input again.")
                continue

            frac = []
            frac.append(n)
            frac.append(d)

            print(f"This fraction is: {frac[0]}/{frac[1]}")
            BL()

            return frac

    def fraction_Operation(self):

        fr = Fraction_RW()

        a = []

        while True:
            if len(a) == 0:
                a = fr.get_User_Fraction()
                altCMD = input("Now choose one of the operations( '+' '-' '*' '/' '=' ) to calculate: ")
                lawfulCMD = ['+','-','*','/','=']

                if altCMD == '+':
                    b = fr.get_User_Fraction()
                    i = fr.__add__(a,b)
                    a = i

                elif altCMD == '-':
                    b = fr.get_User_Fraction()
                    i = fr.__sub__(a,b)
                    a = i

                elif altCMD == '*':
                    b = fr.get_User_Fraction()
                    i = fr.__mul__(a,b)

                elif altCMD == '/':
                    b = fr.get_User_Fraction()
                    i = fr.__truediv__(a,b)
                    a = i

                elif altCMD == '=':
                    b = fr.get_User_Fraction()
                    i = fr.__eq__(a,b)
                    a = i

                else: 
                    altCMD not in lawfulCMD
                    print("Invalid calculation commond! please input again, thanks.")
                    continue

            elif len(a) == 2:
                altCMD = input("Type one operation of ( '+' '-' '*' '/' '=' ) to calculate: ")
                lawfulCMD = ['+','-','*','/','=']

                if altCMD == '+':
                    b = fr.get_User_Fraction()
                    i = fr.__add__(a,b)
                    a = i

                elif altCMD == '-':
                    b = fr.get_User_Fraction()
                    i = fr.__sub__(a,b)
                    a = i

                elif altCMD == '*':
                    b = fr.get_User_Fraction()
                    i = fr.__mul__(a,b)

                elif altCMD == '/':
                    b = fr.get_User_Fraction()
                    i = fr.__truediv__(a,b)
                    a = i

                elif altCMD == '=':
                    b = fr.get_User_Fraction()
                    i = fr.__eq__(a,b)
                    a = i

                else: 
                    altCMD not in lawfulCMD
                    print("Invalid calculation commond! please input again, thanks.")
                    continue



    def __add__(self,x,y):

        nu = (x[0] * y[1]) + (y[0] * x[1])
        de = (x[1] * y[1])
        print(f"The result is: {x[0]}/{x[1]} + {y[0]}/{y[1]} = {nu}/{de}")
        
        rlt = []
        rlt.append(nu)
        rlt.append(de)

        return rlt

    def __sub__(self,x,y):

        nu = (x[0] * y[1]) - (y[0] * x[1])
        de = (x[1] * y[1])
        print(f"The result is: {x[0]}/{x[1]} - {y[0]}/{y[1]} = {nu}/{de}")

        rlt = []
        rlt.append(nu)
        rlt.append(de)

        return rlt

    def __mul__(self,x,y):

        nu = (x[0] * y[0])
        de = (x[1] * y[1])
        print(f"The result is: {x[0]}/{x[1]} * {y[0]}/{y[1]} = {nu}/{de}")

        rlt = []
        rlt.append(nu)
        rlt.append(de)

        return rlt

    def __truediv__(self,x,y):

        nu = (x[0] * y[1])
        de = (x[1] * y[0])
        print(f"The result is: {x[0]}/{x[1]} / {y[0]}/{y[1]} = {nu}/{de}")

        rlt = []
        rlt.append(nu)
        rlt.append(de)

        return rlt

    def __eq__(self,x,y):

        if (x[0]*y[1]) == (y[0]*x[1]):
            print(f"The result is: {x[0]}/{x[1]} equals to {y[0]}/{y[1]}")
        elif (x[0]*y[1]) > (y[0]*x[1]):
            print(f"The result is: {x[0]}/{x[1]} bigger than {y[0]}/{y[1]}")
        elif (x[0]*y[1]) < (y[0]*x[1]):
            print(f"The result is: {x[0]}/{x[1]} smaller than {y[0]}/{y[1]}")

        return y

    # <>

    # < new methods for to support >
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
    # <>


class Fraction():

    def __init__(self) -> None:
        pass

    
    def welcome(self):

        welcoming = "# Welcome to Fractions Calculation #"
        print(welcoming)
        BL()


    def get_Frac_Calcu(self):

        t = ezIO()

        #...
        def get_Frac():
        
            f = []

            print("Please set a fraction...")
            BL()

            n = t.get_Valid_InputVal("Please Input the numerator: ")
            d = t.get_Valid_InputVal("Then, please input the denominator: ")
                    
            f.append(n)
            f.append(d)

            print("This Fraction is: " + str(n) + '/' + str(d))
            BL()

            return f

        def init_Frac():

            a = get_Frac()
              
            while True:
                altCMD = input("Type one of '+','-','*','/','=' to start: ")
                lawfulCMD = ['+','-','*','/','=']
                if altCMD == '+':
                    
                    b = get_Frac()

                    nu = (a[0]*b[1])+(b[0]*a[1])
                    de = (a[1]*b[1])

                    print("The result is: "+ str(a[0]) + '/' + str(a[1]) + ' + ' + str(b[0]) + '/' + str(b[1]) + ' = ' + str(nu) + '/' + str(de) +",")

                    for i in range(2,nu):
                        while (nu % i == 0 and de % i == 0):
                            nu = nu//i
                            de = de//i

                    print("and simplified as: " + ' = ' + str(nu) + "/" + str(de))

                    iF = []

                    iF.append(nu)
                    iF.append(de)

                    return iF
                    

                elif altCMD == '-':

                    b = get_Frac()

                    nu = (a[0]*b[1])-(b[0]*a[1])
                    de = (a[1]*b[1])

                    print("The result is: "+ str(a[0]) + '/' + str(a[1]) + ' - ' + str(b[0]) + '/' + str(b[1]) + ' = ' + str(nu) + '/' + str(de) +",")

                    for i in range(2,nu):
                        while (nu % i == 0 and de % i == 0):
                            nu = nu//i
                            de = de//i

                    print("and simplified as: " + ' = ' + str(nu) + "/" + str(de))

                    iF = []

                    iF.append(nu)
                    iF.append(de)

                    return iF
                    

                elif altCMD == '*':

                    b = get_Frac()

                    nu = (a[0]*b[0])
                    de = (a[1]*b[1])

                    print("The result is: "+ str(a[0]) + '/' + str(a[1]) + ' * ' + str(b[0]) + '/' + str(b[1]) + ' = ' + str(nu) + '/' + str(de) +",")

                    for i in range(2,nu):
                        while (nu % i == 0 and de % i == 0):
                            nu = nu//i
                            de = de//i

                    print("and simplified as: " + ' = ' + str(nu) + "/" + str(de))

                    iF = []

                    iF.append(nu)
                    iF.append(de)

                    return iF
                    

                elif altCMD == '/':

                    b = get_Frac()

                    nu = (a[0]*b[1])
                    de = (a[1]*b[0])

                    print("The result is: "+ str(a[0]) + '/' + str(a[1]) + ' / ' + str(b[0]) + '/' + str(b[1]) + ' = ' + str(nu) + '/' + str(de) +",")

                    for i in range(2,nu):
                        while (nu % i == 0 and de % i == 0):
                            nu = nu//i
                            de = de//i

                    print("and simplified as: " + ' = ' + str(nu) + "/" + str(de))

                    iF = []

                    iF.append(nu)
                    iF.append(de)

                    return iF
                    

                elif altCMD == '=':

                    b = get_Frac()

                    if (a[0]*b[1]) == (b[0]*a[1]):
                        print("The result is: "+ str(a[0]) + '/' + str(a[1]) + ' equles ' + str(b[0]) + '/' + str(b[1]))

                    elif (a[0]*b[1]) > (b[0]*a[1]):
                        print("The result is: "+ str(a[0]) + '/' + str(a[1]) + ' bigger than ' + str(b[0]) + '/' + str(b[1]))

                    elif (a[0]*b[1]) < (b[0]*a[1]):
                        print("The result is: "+ str(a[0]) + '/' + str(a[1]) + ' smaller than ' + str(b[0]) + '/' + str(b[1]))

                    return b
                    

                else: 
                    altCMD not in lawfulCMD
                    print("Invalid calculation commond! please input again, thanks.")
                    continue

        

        def ifin_Frac():

            a = init_Frac()

            while True:
                altCMD = input("Type one of '+','-','*','/','=' to start: ")
                lawfulCMD = ['+','-','*','/','=']
                if altCMD == '+':
                    
                    b = get_Frac()

                    nu = (a[0]*b[1])+(b[0]*a[1])
                    de = (a[1]*b[1])

                    print("The result is: "+ str(a[0]) + '/' + str(a[1]) + ' + ' + str(b[0]) + '/' + str(b[1]) + ' = ' + str(nu) + '/' + str(de) +",")

                    for i in range(2,nu):
                        while (nu % i == 0 and de % i == 0):
                            nu = nu//i
                            de = de//i

                    print("and simplified as: " + ' = ' + str(nu) + "/" + str(de))

                    iF = []

                    iF.append(nu)
                    iF.append(de)

                    return iF
                    

                elif altCMD == '-':

                    b = get_Frac()

                    nu = (a[0]*b[1])-(b[0]*a[1])
                    de = (a[1]*b[1])

                    print("The result is: "+ str(a[0]) + '/' + str(a[1]) + ' - ' + str(b[0]) + '/' + str(b[1]) + ' = ' + str(nu) + '/' + str(de) +",")

                    for i in range(2,nu):
                        while (nu % i == 0 and de % i == 0):
                            nu = nu//i
                            de = de//i

                    print("and simplified as: " + ' = ' + str(nu) + "/" + str(de))

                    iF = []

                    iF.append(nu)
                    iF.append(de)

                    return iF
                    

                elif altCMD == '*':

                    b = get_Frac()

                    nu = (a[0]*b[0])
                    de = (a[1]*b[1])

                    print("The result is: "+ str(a[0]) + '/' + str(a[1]) + ' * ' + str(b[0]) + '/' + str(b[1]) + ' = ' + str(nu) + '/' + str(de) +",")

                    for i in range(2,nu):
                        while (nu % i == 0 and de % i == 0):
                            nu = nu//i
                            de = de//i

                    print("and simplified as: " + ' = ' + str(nu) + "/" + str(de))

                    iF = []

                    iF.append(nu)
                    iF.append(de)

                    return iF
                    

                elif altCMD == '/':

                    b = get_Frac()

                    nu = (a[0]*b[1])
                    de = (a[1]*b[0])

                    print("The result is: "+ str(a[0]) + '/' + str(a[1]) + ' / ' + str(b[0]) + '/' + str(b[1]) + ' = ' + str(nu) + '/' + str(de) +",")

                    for i in range(2,nu):
                        while (nu % i == 0 and de % i == 0):
                            nu = nu//i
                            de = de//i

                    print("and simplified as: " + ' = ' + str(nu) + "/" + str(de))

                    iF = []

                    iF.append(nu)
                    iF.append(de)

                    return iF
                    

                elif altCMD == '=':

                    b = get_Frac()

                    if (a[0]*b[1]) == (b[0]*a[1]):
                        print("The result is: "+ str(a[0]) + '/' + str(a[1]) + ' equles ' + str(b[0]) + '/' + str(b[1]))

                    elif (a[0]*b[1]) > (b[0]*a[1]):
                        print("The result is: "+ str(a[0]) + '/' + str(a[1]) + ' bigger than ' + str(b[0]) + '/' + str(b[1]))

                    elif (a[0]*b[1]) < (b[0]*a[1]):
                        print("The result is: "+ str(a[0]) + '/' + str(a[1]) + ' smaller than ' + str(b[0]) + '/' + str(b[1]))

                    return b
                    

                else: 
                    altCMD not in lawfulCMD
                    print("Invalid calculation commond! please input again, thanks.")
                    continue


        ifin_Frac()
       
# <>

"""/* define class and method ends */"""



"""///*** define main program and execute it below ***///"""

def main():

    x = Fraction_RW()

    x.welcome()
    x.fraction_Operation()

    main()

"""///*** main program ends ***///"""

"""///*** main program execute below ***///"""

if __name__ == '__main__':
    main()

"""///*** main program ends ***///"""
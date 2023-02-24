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

import sys,types,fractions

""" define glob vars, cons, lists, dicts, and others """

test = 0

"""/* define vcldo ends */"""


""" define print format method """

# <define blank line>
def BL():

    print()
# <>

"""/* define pf-m ends */"""


"""/* define preset class and method */"""

# <define support-class="ezIO" for esay to re-use some repeatable codes>
class ezIO:

    def __init__(self):
        pass

    def get_Valid_InputVal(self,pmpt):

        while True:
            rawVal = input(pmpt)
            if str(rawVal).isalpha():
                print("Invalid input! The input must be a number without 0 value.")
                print("Try again...")
                continue
            elif int(rawVal) == 0:
                print("Invalid input! The input number can not be 0, which makes the fraction untanable.")
                print("Try again...")
                continue
            #Below can not be worked
            elif len(rawVal) == 0:
                print("Invalid input! The input can not contain space inputting.")
                print("Try again...")
                continue
            #Below can not be worked
            elif rawVal.isspace():
                print("Invalid input! The input can not contain space inputting.")
                print("Try again...")
                continue
            else:
                return int(rawVal)
            # I can not handle all of the odd or weird input by user's possibility. Will overcome in near future!
# <>

# <define main-class="Fraction"> 
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

    x = Fraction()

    x.welcome()
    x.get_Frac_Calcu()

    main()

"""///*** main program ends ***///"""

"""///*** main program execute below ***///"""

if __name__ == '__main__':
    main()

"""///*** main program ends ***///"""
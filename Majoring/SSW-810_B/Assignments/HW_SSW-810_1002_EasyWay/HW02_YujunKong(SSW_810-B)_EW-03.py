"""
/*
School: Stevens Institute of Technology
Course: SSW 540 - A
Topic: Fractions Calculation
Coder with CWID: Name: Yujun Kong / CWID: 1046 6820
Stevens Tech CWID: 1046 6820
*/
"""


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

# <define support-class="KG_IO">
class ezIO:

    def __init__(self):
        pass

    #def pl(*args):print(*args,end='')

    def get_Valid_InputVal(self,pmpt,cvtType):

        while True:
            rawVal = input(pmpt)    
            if rawVal.isalpha():
                print("Invalid input, please try again.")
                break
            elif cvtType == 'Int':
                cvtedVal = int(float(rawVal))
                return cvtedVal
                continue

# <>

# <define main-class="Fraction"> 
class Fraction():

    def __init__(self) -> None:
        pass

    
    def welcome(self):

        welcoming = "# Welcome to Fractions Calculation #"
        print(welcoming)
        BL()


    def get_Frac_ArraySum(self):

        t = ezIO()

        #...
        def set_InitFrac():
        
            fracArr = []

            f = fracArr

            #...
            print("Please set a fraction...")
            BL()
            nu = t.get_Valid_InputVal("Input the numerator: ",'Int')
            de = t.get_Valid_InputVal("Input the denominator: ",'Int')

            f.append(nu)
            f.append(de)

            print("This Fraction is: " + str(nu) + '/' + str(de))
            BL()

            altCMD = t.get_Valid_InputVal("Which kind of calculation? Type one of '+','-','*','/','=' to start ",'Int')

            if altCMD == '+':
                
                return

            elif altCMD == '-':
                
                return

            elif altCMD == '*':

                return

            elif altCMD == '/':

                return

            elif altCMD == '=':
                
                return

            else:
                print("Invalid input! You shall type '+','-','*','/', or'=' commond to calculate.")

            




        #...
        def set_nextfrac():

            

    
        return fracArr


class Operation:

    def __init__(self):
        pass


    def opTest(self):

        o = Fraction()
        a = o.get_Frac_ArraySum()

        calcuAskPrompt = "Type '+', '-', '*', '/', '=' for to Plus, Minus, Times, Divide, or Compare Value: "
        altCMD = input(calcuAskPrompt)
        BL()
        print("Calculating ... ")
        

        if altCMD == "p":

            pls = " + "

            pls_Detor = a[1] * a[3] * a[5]
            pls_Nutor = (a[0] * a[3] * a[5]) + (a[2] * a[1] * a[5]) + (a[4] * a[1] * a[3])

            print(pls_Nutor)
            print(pls_Detor)

            print("The linear plus calculation result is:")
            BL()
            print( str(a[0])+'/'+str(a[1]) + pls + str(a[2])+'/'+str(a[3]) + pls + str(a[4])+'/'+str(a[5]) + eql + str(pls_Nutor)+'/'+str(pls_Detor) )
            BL()
            
        elif altCMD == "m":

            mis = " - "

            mis_Detor = a[1] * a[3] * a[5]
            mis_Nutor = (a[0] * mis_Detor) - (a[2] * mis_Detor) - (a[4] * mis_Detor)
            
            print(mis_Nutor)
            print(mis_Detor)

            print("The linear plus calculation result is:")
            BL()
            print( str(a[0])+'/'+str(a[1]) + mis + str(a[2])+'/'+str(a[3]) + mis + str(a[4])+'/'+str(a[5]) + eql + str(mis_Nutor)+'/'+str(mis_Detor) )
            BL()

        elif altCMD == "t":

            tms = " * "

            tms_Detor = a[1] * a[3] * a[5]
            tms_Nutor = (a[0] * mis_Detor) - (a[2] * mis_Detor) - (a[4] * mis_Detor)
            
            print(mis_Nutor)
            print(mis_Detor)

            print("The linear plus calculation result is:")
            BL()
            print( str(a[0])+'/'+str(a[1]) + mis + str(a[2])+'/'+str(a[3]) + mis + str(a[4])+'/'+str(a[5]) + eql + str(mis_Nutor)+'/'+str(mis_Detor) )
            BL()

        
          
    def plus(self):
        
# <>

"""/* define class and method ends */"""



"""///*** define main program and execute it below ***///"""

def mainTest():

    x = Fraction()
    y = Operation()

    x.welcome()
    y.opTest()


mainTest()

"""///*** main program ends ***///"""
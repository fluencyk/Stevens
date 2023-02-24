"""
/*
School: Stevens Institute of Technology
Course: SSW 810 - B
Topic: Fraction Class Application
Original Coder: Yujun Kong
Coder with CWID: Name: Yujun Kong / CWID: 1046 6820
Stevens Tech CWID: 1046 6820
Newly Updated Started Time Point: 13:00 09/16/2021
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
class UniIO:

    def __init__(self):
        pass

    def cvt(self,cvtType,Obj):

        if cvtType == 'Int':
            cvtObj = int(float(Obj))

        elif cvtType == 'Flo':
            cvtObj = float(Obj)

        elif cvtType == 'Cpx':
            cvtObj = complex(Obj)

        elif cvtType == 'Str':
            cvtObj = str(Obj)

        return cvtObj

    def get_Cvted_InputVal(self,pmpt,cvtType):

        rawVal = input(pmpt)

        if cvtType == 'Int':
            cvtedVal = int(float(rawVal))            

        elif cvtType == 'Flo':
            cvtedVal = float(rawVal)

        elif cvtType == 'Cpx':
            cvtedVal = complex(rawVal)

        elif cvtType == 'Str':
            cvtedVal = str(rawVal)

        return cvtedVal

# <>

# <define main-class="Fraction"> 
class Fraction():

    def __init__(self) -> None:
        pass

    
    def welcome(self):

        welcoming = "# Welcome to Linear Fractions Calculation #"
        print(welcoming)
        BL()


    def get_Frac_ArraySum(self):

        t = UniIO()

        sumFracArr = []


        def set_FirstFrac():

            soloFracArr = []

            print("Please set a first fraction...")
            BL()
            x = t.get_Cvted_InputVal("Input the numerator: ",'Int')
            y = t.get_Cvted_InputVal("Input the denominator: ",'Int')

            soloFracArr.append(x)
            soloFracArr.append(y)

            print("This Fraction is: " + str(soloFracArr[0] ) + '/' + str(soloFracArr[1]))
            BL()
            return soloFracArr


        def set_NextFrac():

            soloFracArr = []

            print("Please set a next fraction...")
            BL()
            x = t.get_Cvted_InputVal("Input the numerator: ",'Int')
            y = t.get_Cvted_InputVal("Input the denominator: ",'Int')
        
            soloFracArr.append(x)
            soloFracArr.append(y)

            print("This Fraction is: " + str(soloFracArr[0] ) + '/' + str(soloFracArr[1]))
            BL()
            return soloFracArr

        set_FirstFrac()
        set_NextFrac()

        print("Add a extra fraction? Type 'y' to add.")
        addexa_or_calcu = "Or type 'n' to calculate above fractions: "
        altCMD = input(addexa_or_calcu)
        BL()

        lawfulCMD = ["y","n"]
        if altCMD == "y":
            print("coding 'add a extra fraction'")
            set_NextFrac()
        elif altCMD == "n":
            print("coding 'execute fractions calculation'")
            print(sumFracArr)

        # check return value
        
        

    def get_NextFrac():

        r = Fraction()

        r.get_ArrSto_Frac()

    

        


    def plus(self):
        pass

    def minus(self):
        pass

    def times(self):
        pass

    def devide(self):
        pass

    def equal(self):
        pass

    def __str__(self) -> str:
        pass
# <>

"""/* define class and method ends */"""



"""///*** define main program and execute it below ***///"""

def mainTest():

    x = Fraction()

    x.welcome()
    x.get_Frac_ArraySum()


mainTest()

"""///*** main program ends ***///"""
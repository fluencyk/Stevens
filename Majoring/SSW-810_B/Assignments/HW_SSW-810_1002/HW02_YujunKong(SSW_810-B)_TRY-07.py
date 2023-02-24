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

        #...
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

        #...
        def set_NextFrac():

            soloFracArr = []
            #combFracArr = []

            print("Please set a next fraction...")
            BL()
            x = t.get_Cvted_InputVal("Input the numerator: ",'Int')
            y = t.get_Cvted_InputVal("Input the denominator: ",'Int')
        
            soloFracArr.append(x)
            soloFracArr.append(y)
            #combFracArr.append(soloFracArr)

            print("This Fraction is: " + str(soloFracArr[0]) + '/' + str(soloFracArr[1]))
            BL()

            #i = soloFracArr

            print("Add an extra fraction? Type 'a' to add, or type 'c' to calculate.")
            addexa_or_calcu = "Please type your commond: "
            altCMD = input(addexa_or_calcu)
            BL()

            #lawfulCMD = ["c","a"]
            if altCMD == "c":

                soloFracArr.append(x)
                soloFracArr.append(y)

                print("Calculating the fractions...")
                print(soloFracArr)

            elif altCMD == "a":
                
                print("Adding an extra fraction...")
                set_NextFrac()


            return soloFracArr

        #...
        a = set_FirstFrac()
        b = set_NextFrac()

        #...
        sumFracArr = []
        sumFracArr.append(a)
        sumFracArr.append(b)

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
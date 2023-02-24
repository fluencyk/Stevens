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

    def pl(*args):print(*args,end='')

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
        sumFracArr = []

        #...
        print("Please set first fraction...")
        BL()
        a = t.get_Cvted_InputVal("Input the numerator: ",'Int')
        sumFracArr.append(a)
        b = t.get_Cvted_InputVal("Input the denominator: ",'Int')
        sumFracArr.append(b)

        print("This Fraction is: " + str(a) + '/' + str(b))
        BL()

        #...
        print("Please set second fraction...")
        BL()
        c = t.get_Cvted_InputVal("Input the numerator: ",'Int')
        sumFracArr.append(c)
        d = t.get_Cvted_InputVal("Input the denominator: ",'Int')
        sumFracArr.append(d)

        print("This Fraction is: " + str(c) + '/' + str(d))
        BL()

        #...
        print("Please set third fraction...")
        BL()
        e = t.get_Cvted_InputVal("Input the numerator: ",'Int')
        sumFracArr.append(e)
        f = t.get_Cvted_InputVal("Input the denominator: ",'Int')
        sumFracArr.append(f)

        print("This Fraction is: " + str(e) + '/' + str(f))
        BL()
    
        return sumFracArr


class Operation:

    def __init__(self):
        pass


    def opTest(self):

        o = Fraction()
        a = o.get_Frac_ArraySum()

        calcuAskPrompt = "Type 'p', 'm', 't', 'd', 'c' for to Plus, Minus, Times, Divide, or Compare Value: "
        altCMD = input(calcuAskPrompt)
        BL()
        print("Calculating ... ")

        sla = "/"
        blk = " "
        eql = " = "
        pls = " + "

        if altCMD == "p":
                
            print("The linear plus calculation result is:")
            BL()
            print( str(a[0]) + sla + str(a[1]) + pls + str(a[2]) + sla + str(a[3]) + pls + str(a[4]) + sla + str(a[5]) + eql )
            BL()
            
        elif altCMD == "a":
            print("Adding next fraction...")

        """while i < al:

            i = i+1
            print(i)
            print( str(a[i]) + '/' + str(a[i+1]) )

            i = al"""

        
          
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
    y = Operation()

    x.welcome()
    y.opTest()


mainTest()

"""///*** main program ends ***///"""
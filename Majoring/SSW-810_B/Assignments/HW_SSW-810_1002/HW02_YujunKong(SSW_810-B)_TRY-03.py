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


    def get_ArrSto_FracElem(self):

        FC_nSum = []

        arrStoFC = []

        t = UniIO()

        x = t.get_Cvted_InputVal("Input the numerator: ",'Int')
        y = t.get_Cvted_InputVal("Input the denominator: ",'Int')

        arrStoFC.append(x)
        arrStoFC.append(y)

        '''print(arrStoFC)'''

        FC_nSum.append(arrStoFC)
        FC_nSum.append(arrStoFC)

        print(FC_nSum)




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

    x.get_ArrSto_FracElem()


mainTest()

"""///*** main program ends ***///"""
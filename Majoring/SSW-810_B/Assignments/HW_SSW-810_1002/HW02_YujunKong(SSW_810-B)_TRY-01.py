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
class Fraction(UniIO):

    def __init__(self) -> None:
        pass

    asf = ['n','d']
    

    optor[0] = UniIO.get_Cvted_InputVal("Input your first fraction's numerator: ",'Int')
    optor[1] = UniIO.get_Cvted_InputVal("Input your first fraction's denominator: ",'Int')

    optor[2] = UniIO.get_Cvted_InputVal("Input your second fraction's numerator: ",'Int')
    optor[3] = UniIO.get_Cvted_InputVal("Input your second fraction's denominator: ",'Int')

    optor[4] = UniIO.get_Cvted_InputVal("Input your third fraction's numerator: ",'Int')
    optor[5] = UniIO.get_Cvted_InputVal("Input your third fraction's denominator: ",'Int')

    
    def get_ArrSto_FracElem(self):

        arrStoFE = []

        nutor = UniIO.get_Cvted_InputVal("Input the numerator: ",'Int')
        detor = UniIO.get_Cvted_InputVal("Input the denominator: ",'Int')

        arrStoFE.append(nutor)
        arrStoFE.append(detor)

        arrStoFE[0] + arrStoFE[1]


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

    pass


mainTest()

"""///*** main program ends ***///"""
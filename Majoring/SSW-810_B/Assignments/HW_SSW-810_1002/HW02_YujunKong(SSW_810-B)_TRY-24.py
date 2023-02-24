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

            initFracArr = []

            print("Please set a first fraction...")
            BL()
            x = t.get_Cvted_InputVal("Input the numerator: ",'Int')
            y = t.get_Cvted_InputVal("Input the denominator: ",'Int')

            initFracArr.append(x)
            initFracArr.append(y)

            print("This Fraction is: " + str(initFracArr[0] ) + '/' + str(initFracArr[1]))
            BL()
            
            return initFracArr


        #...
        def set_SecondFrac():
                       
            soloFracArr = []
            nSumFracArr = []

            #...
            print("Please set a next fraction...")
            BL()
            x = t.get_Cvted_InputVal("Input the numerator: ",'Int')
            soloFracArr.append(x)
            y = t.get_Cvted_InputVal("Input the denominator: ",'Int')
            soloFracArr.append(y)


            print("This Fraction is: " + str(soloFracArr[0]) + '/' + str(soloFracArr[1]))
            BL()

            #...
            print("Add an extra fraction? Type 'a' to add, or type 'c' to calculate.")
            addexa_or_calcu = "Please type your commond: "
            altCMD = input(addexa_or_calcu)
            BL()


            if altCMD == "c":
                
                #print("Calculating the fractions...")
                return soloFracArr
            
            elif altCMD == "a":
                print("Adding next fraction...")

                #print(soloFracArr)
                a.extend(soloFracArr)
                n = set_SecondFrac()
                nSumFracArr.extend(n)

                return nSumFracArr

            else:                
                #print(soloFracArr)
                return soloFracArr

        #...
        a = set_FirstFrac() # 1/2
        b = set_SecondFrac() # 3/4

        #...
        sumFracArr = []
        #sumFracArr.append(a)
        #sumFracArr.append(b)
        
        a.extend(b)

        #print(a)
        #print(len(a))
        return a


class Operation:

    def __init__(self):
        pass

    

    def opTest():

        o = Fraction()

        a = o.get_Frac_ArraySum()

        al = len(a)



        n = 0       
        d = 1

        if n in range(al):
            n = n+1

        elif n in range(al):
            n = n+0

        print("Show the calculation expression")

        print( str(a[n]) + '/' + str(a[d])  )
        
        
        
        #print( str(a[n-2]) + '/' + str(a[d-2]) )
        
        
        
        #print( str(a[n-4]) + '/' + str(a[d-4]) )

        #x = (j[1]*j[3])

        #print(x-1)

        #deIdx = int(len(o.get_Frac_ArraySum()))-1

        #return deIdx

        #print(deIdx)

        #fcsArr = o.get_Frac_ArraySum()

        #print(o.get_Frac_ArraySum())
        

     
          
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
    y = Operation

    x.welcome()
    #x.get_Frac_ArraySum()
    y.opTest()


mainTest()

"""///*** main program ends ***///"""
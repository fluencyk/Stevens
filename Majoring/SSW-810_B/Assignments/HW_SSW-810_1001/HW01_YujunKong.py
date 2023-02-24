"""
/*
School: Stevens Institute of Technology
Course: SSW 810-B
Assignment: Homework # 1001, 
Topic: Rock-Paper-Scissors Game
Coder: Yujun Kong
*/
"""


"""/* def glob vars, cons, lists for pre-set */"""

moveValue = [9,4,1]

welcome = "*** Welcome to Rock-Paper-Scissors Game ***"

"""/* vars ends */"""


"""/* def supporting methods */"""

""" def blank line """
def BL():

    print()


def wrongHint_withRetype():

    print("You Need to Type S to Start the Game!")
    verifier_Input_of_Start()


def verifier_Input_of_Start():

    BL()
    gameStart = input("Type S to start the Game: ")

    if gameStart == "S":
        gameCore()
    if gameStart != "S":
        wrongHint_withRetype()
    

def gameInitiator():

    BL()
    print(welcome)
    verifier_Input_of_Start()


def getHuman_MoveValue():

    lawfulCommond = ["R","S","P","E"]

    humanMove = input("Type Your Move Commond(R, S, P) or Type E to Exit: ")

    humanCMD = ["Your Move is: Rock","Your Move is: Scissors","Your Move is: Paper"]

    humanValue = 0
    
    if humanMove not in lawfulCommond:
        print("!!!!! - You Must Type R, S, P or E for your Move or Exit - !!!!!")
    if humanMove not in lawfulCommond:
        gameCore()

    if humanMove == "R":
        humanValue = moveValue[0]

    if humanMove == "R":
        print(humanCMD[0])
        
    if humanMove == "S":
        humanValue = moveValue[1]
    if humanMove == "S":
        print(humanCMD[1])

    if humanMove == "P":
        humanValue = moveValue[2]
    if humanMove == "P":
        print(humanCMD[2])


    if humanMove == "E":
        gameTerminator()

    """ returning-type: int """
    return humanValue


def getComputer_MoveValue():

    print("------ ----- ---- ----- ------")
    print("----- Now Computer Moves -----")
    print("------ ----- ---- ----- ------")

    import random

    cpuValue = 0

    cpuCMD = ["Computer Move is: Rock","Computer Move is: Scissors","Computer Move is: Paper"]

    cpuValue = random.choice(moveValue)

    if cpuValue == 9:
        print(cpuCMD[0])

    if cpuValue == 4:
        print(cpuCMD[1])

    if cpuValue == 1:
        print(cpuCMD[2])

    BL()
    print("The Battle Result Is")

    """ returning-type: int """
    return cpuValue


def calcu_BattleReslut():

    gottenNumber = 0
    
    gH = getHuman_MoveValue()
    gC = getComputer_MoveValue()

    gottenNumber = gH - gC

    """ returning-type: int """
    return gottenNumber


class gameBattle_ResultPrinter():

    battleResult = ["You Win :)","You Lost :(","It's a Draw -_-!"]

    youWin = battleResult[0]
    youLost = battleResult[1]
    itsDraw = battleResult[2]


def resultPrinter():

    battleResult_Value = calcu_BattleReslut()

    draw = gameBattle_ResultPrinter.itsDraw
    win = gameBattle_ResultPrinter.youWin
    lost = gameBattle_ResultPrinter.youLost

    """Same-Move vs Same-Move"""
    if battleResult_Value == 0:
        print(draw)
        BL()


    """Rock vs Scissors"""    
    if battleResult_Value == 5:
        print(win)
        BL()

    """Rock vs Paper"""
    if battleResult_Value == 1:
        print(lost)
        BL()


    """Scissors vs Paper"""
    if battleResult_Value == 3:
        print(win)
        BL()

    """Scissors vs Rock"""
    if battleResult_Value == -5:
        print(lost)
        BL()


    """Paper vs Rock"""
    if battleResult_Value == -8:
        print(win)
        BL()

    """Paper vs Scissors"""
    if battleResult_Value == -3:
        print(lost)
        BL()


def gameBattle():

    resultPrinter()

    """ returning-type: resursive object """
    return gameBattle()

"""/* supporting methods end */"""


"""/* def core method */"""

def gameCore():

    BL()
    print("***********   RULE   *************")
    print("**                              **")
    print("* Rock can vanquish Scissors     *")
    print("* Scissors can vanquish Paper    *")
    print("* Paper can vanquish Rock        *")
    print("*                                *")
    print("* Type R for Rock's Move         *")
    print("* Type S for Scissors' Move      *")
    print("* Type P for Paper's Move        *")
    print("*                                *")
    print("* Type E for to Exit the Game    *")
    print("*                                *")
    print("**********************************")
    BL()

    gameBattle()

"""/* core method ends */"""


"""/* def Terminating method */"""

def gameTerminator():

    BL()
    print("Successfully Exit and Restart!")
    BL()
    gameInitiator()

"""/* method ends */"""


"""/* def controllor method */"""

def gameController():

        gameInitiator()

"""/* method ends */"""


"""///*** main program execute below ***///"""

gameController()

"""///*** main program ends ***///"""
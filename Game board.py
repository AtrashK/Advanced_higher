from dataclasses import dataclass
import random
@dataclass
class square():
    position : int = 0
    player : str = ''
    pointer : int = 0

gameboard=[square() for i in range(50)]

def displayBoard(gameboard):
    for row in range(len(gameboard)):
        print(str(gameboard[row].position) + ', ')

def initPosition(gameboard):
    for i in range(len(gameboard)):
        gameboard[i].position=i
        if (i==4):
            gameboard[i].pointer=7
        elif (i==11):
            gameboard[i].pointer=9
        elif (i==15):
            gameboard[i].pointer=19
        elif (i==22):
            gameboard[i].pointer=19
        elif (i==26):
            gameboard[i].pointer=28
        elif (i==31):
            gameboard[i].pointer=36
        elif (i==35):
            gameboard[i].pointer=31
        elif (i==44):
            gameboard[i].pointer=47
        elif (i==47):
            gameboard[i].pointer=45
        else:
            gameboard[i].pointer=-1

def playerData(gameboard):
    colour=input("What colour do you want, blue, green, red or yellow? ")
    while (colour!="red" and colour!="blue" and colour!="green" and colour!="yellow"):
        print("That wasn't an option.")
        colour=input("What colour do you want, blue, green, red or yellow? ")
    gameboard[0].player=colour
    return colour

def rollDiceandMove(gameboard):
    enter=input("Press enter to roll the dice ")
    roll=random.randint(1,6)
    print("You rolled a "+str(roll))
    found=False
    i=0
    while(found==False and i<50):
        if (gameboard[i].player!=""):
            found=True
            if (i+roll>50):
                print("That is beyond 50. Roll again")
            gameboard[i+roll].player=gameboard[i].player
            gameboard[i].player=""
            print("You are now on square " + str(i+roll))
        i+=1

initPosition(gameboard)
#displayBoard(gameboard)
colour=playerData(gameboard)
won=False
while (won==False):
    rollDiceandMove(gameboard)
import numpy as np
import os
import random
gridsize = 10
gamegrid = np.full((gridsize,gridsize), " ")
playerturn = True
game = True
debug = True
def endgame(value):
    global game
    game = False
    if value == "X":
        print("Player 1 win")
    else:
        print("Player 2 win")
    exit()
def clear():
    global debug
    if debug == False:
        os.system('cls')
def checkwin():
    for row in gamegrid:
        if "XXXXX" in ''.join(row):
            endgame("X")

def oldcheckwin():
    count = 0
    previous = None
    for row in gamegrid:
        for value in row:
            if (value == previous) & (value != " "):
                count += 1
            if count >= 4:
                endgame(value)
                return True
            previous = value
def ai():
    global playerturn
    aiinput = (random.randrange(1,gridsize),random.randrange(1,gridsize))
    while gamegrid[aiinput] != " ":
        aiinput = (random.randrange(1,gridsize),random.randrange(1,gridsize))
    gamegrid[aiinput] = "O"
    clear()
    checkwin()
    playerturn = True

def func(playerinput):
    if len(playerinput) != 2:
        raise IndexError      
    for i in playerinput:
        if i < 0:
            raise IndexError 
    if gamegrid[playerinput] != " ":
        return True
    gamegrid[playerinput] = "X"
    clear()
    checkwin()
    return False
def player():
    global playerturn
    while playerturn == True:
        print(str(gamegrid).replace(' [', '').replace('[', '').replace(']', ''))
        playerinput = input("Enter coord: ")
        try:
            playerinput = tuple(map(int,playerinput.split()))
            playerinput = tuple(x-1 for x in playerinput)
            playerinput = playerinput[::-1]
            playerturn = func(playerinput)
        except IndexError:
            clear()
            if len(playerinput) != 2:
                print("1st Invalid input. Input should be in format: x y")
                print(len(playerinput))  
            else:
                print("Input out of range")
    
while game == True:
    player()
    ai()
    checkwin()
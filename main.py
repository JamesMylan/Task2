import numpy as np
import os
import random
gridsize = 10
gamegrid = np.full((gridsize,gridsize), " ")
playerturn = True
game = True
debug = False
def endgame(value):
    global game
    game = False
    if value == "X":
        print("Player 1 win")
        print(gamegrid)
    else:
        print("AI win")
        print(gamegrid)
    exit()
def clear():
    global debug
    if debug == False:
        os.system('cls')
def checkwin():
    #check for win horizontally
    for row in gamegrid:
        if "XXXXX" in ''.join(row): #joins all values in row into a string
            endgame("X")
        if "OOOOO" in ''.join(row):
            endgame("O")
    #check for win vertically
    for i in range(len(gamegrid)):
        if "XXXXX" in ''.join(gamegrid[:,i]):
            endgame("X")
        if "OOOOO" in ''.join(gamegrid[:,i]):
            endgame("O")
    #check for win diagonally
    for i in range(-(gridsize-1),(gridsize)):
        if "XXXXX" in ''.join(np.diag(gamegrid, i)): #joins all values in diagonal line into a string
            endgame("X")
        if "OOOOO" in ''.join(np.diag(gamegrid, i)):
            endgame("O")

def ai():
    global playerturn
    aiinput = (random.randrange(1,gridsize),random.randrange(1,gridsize))
    while gamegrid[aiinput] != " ":
        aiinput = (random.randrange(1,gridsize),random.randrange(1,gridsize))
    gamegrid[aiinput] = "O"
    clear()
    checkwin()
    playerturn = True

def placeinput(playerinput):
    if len(playerinput) != 2:
        raise IndexError      
    for i in playerinput:
        if i < 0:
            raise IndexError 
    if gamegrid[playerinput] != " ":
        clear()
        print("Space already taken")
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
            playerturn = placeinput(playerinput)
        except IndexError:
            clear()
            if len(playerinput) != 2:
                print("Invalid input. Input should be in format: x y")
            else:
                print("Input out of range")
    
while game == True:
    player()
    ai()
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
        if os.name=='nt':
            os.system('cls')
        else:
            os.system('clear')
def checkingrid(grid,value: str):
    #check for value horizontally
    for row in grid:
        if value in ''.join(row): #joins all values in row into a string
            return True
    #check for value vertically
    for i in range(len(grid)):
        if value in ''.join(grid[:,i]):
            return True
    #check for value diagonally
    for i in range(-(len(grid)-1),(len(grid))):
        if value in ''.join(np.diag(grid, i)): #joins all values in diagonal line into a string
            return True
    return False
def checkwin():
    if checkingrid(gamegrid,"XXXXX"):
        endgame("X")
    elif checkingrid(gamegrid,"OOOOO"):
        endgame("O")

def ai():
    global playerturn
    aiinput = tuple()
    gamegridcopy = gamegrid.copy()
    for row in range(len(gamegridcopy)):
        for value in range(len(gamegridcopy)):
            if gamegrid[row,value] == " ":
                gamegridcopy[row,value] = "X"
            if (checkingrid(gamegridcopy,"XXXXX")) & (gamegrid[row,value] == " "):
                if aiinput == tuple():
                    aiinput = row,value
            if gamegrid[row,value] == " ":
                gamegridcopy[row,value] = " "
    print(aiinput)
    if aiinput == tuple():
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
        print(str(gamegrid).replace(' [', '').replace('[', '').replace(']', '')) #prints list without square bracket border
        playerinput = input("Enter coord: ")
        try:
            playerinput = tuple(map(int,playerinput.split()))
            playerinput = tuple(x-1 for x in playerinput) #subtract 1 from each coordinate
            playerinput = playerinput[::-1] #reverses tuple from (y, x) to (x, y)
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
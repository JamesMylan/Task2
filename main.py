import numpy as np
import os
import random
gridsize = 10
gamegrid = np.full((gridsize,gridsize), " ") #gamegrid must be a square
playerturn = True #Player starts first
game = True
debug = False #when set to True the terminal will not be cleared
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
def clear(): #clears terminal output
    global debug
    if debug == False:
        if os.name=='nt':
            os.system('cls')
        else:
            os.system('clear')
def checkingrid(grid, value: str):
    #check for value horizontally
    for row in grid:
        if value in ''.join(row): #joins all values in row into a string
            return True
    #check for value vertically
    for i in range(len(grid)):
        if value in ''.join(grid[:,i]): #joins all values in column into a string
            return True
    #check for value diagonally
    for i in range(-(len(grid)-1),(len(grid))):
        if value in ''.join(np.diag(grid, i)): #joins all values in diagonal line into a string
            return True
    return False
def checkwin(): #Win is reached when either player reaches 5 in a row
    if checkingrid(gamegrid,"XXXXX"):
        endgame("X")
    elif checkingrid(gamegrid,"OOOOO"):
        endgame("O")
def findmove(grid,value: str,letter: str,move):
    gamegridcopy = grid.copy() #make copy of grid
    for row in range(len(gamegridcopy)):
        for item in range(len(gamegridcopy)): #this can be done since the grid is a square
            if grid[row,item] == " ": #only considers empty places
                gamegridcopy[row,item] = letter
                if checkingrid(gamegridcopy,value):
                    if not checkingrid(grid,value): #checks if this move was already placed on the actual grid
                        move = row,item
                gamegridcopy[row,item] = " "
    return move
def ai(grid):
    global playerturn
    aiinput = tuple()
    #check if opponent can make a winning move and attempt to block it
    aiinput=findmove(grid,"XXXXX","X",aiinput)
    if aiinput == tuple():  #if a move hasn't already been decided
       aiinput = findmove(grid,"XXXX","X",aiinput)
    for i in range(5,1,-1): #attempt to continue an exisiting line
        if aiinput == tuple():
            aiinput=findmove(grid,i*"O","O",aiinput)
    if aiinput == tuple(): #if no line can be contiued or blocked a random move is chosen
        aiinput = (random.randrange(1,gridsize),random.randrange(1,gridsize))
        while grid[aiinput] != " ":
            aiinput = (random.randrange(1,gridsize),random.randrange(1,gridsize))
    grid[aiinput] = "O"
    checkwin()
    playerturn = True

def placeinput(playerinput):
    if len(playerinput) != 2:
        raise IndexError      
    for i in playerinput:
        if i < 0: #no negative values
            raise IndexError 
    if gamegrid[playerinput] != " ": #prevent moves in already taken places
        clear()
        print("Space already taken")
        return True
    gamegrid[playerinput] = "X"
    clear()
    checkwin()
    return False
def player():
    global playerturn
    while playerturn:
        gamegriddisplay = gamegrid.copy()
        #prints row/column numbers
        #gamegriddisplay = np.c_[np.arange(1,gridsize+1),gamegriddisplay] 
        #gamegriddisplay = np.r_[[np.arange(gridsize+1)],gamegriddisplay]
        print(str(gamegriddisplay).replace(' [', '').replace('[', '').replace(']', '')) #prints list without square bracket border
        playerinput = input("Enter coord: ")
        try:
            playerinput = tuple(map(int,playerinput.split()))
            playerinput = tuple(x-1 for x in playerinput) #subtract 1 from each coordinate
            playerinput = playerinput[::-1] #reverses move from (y, x) to (x, y)
            playerturn = placeinput(playerinput)
        except:
            clear()
            if len(playerinput) != 2:
                print("Invalid input. Input should be in format: x y")
            else:
                print("Input out of range")
    
def main():
    while game == True:
        player()
        clear()
        ai(gamegrid)
if __name__ == '__main__':
    main()

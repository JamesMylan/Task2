import numpy as np
import os
import random
gridsize = 5
gamegrid = np.full((gridsize,gridsize), " ")
while True:
    print(str(gamegrid).replace(' [', '').replace('[', '').replace(']', ''))
    playerinput = input("Enter coord: ")
    try:
        playerinput = tuple(map(int,playerinput.split()))
        playerinput = tuple(x-1 for x in playerinput)
        if len(playerinput) != 2:
            raise IndexError      
        for i in playerinput:
            if i < 0:
                raise IndexError 
        gamegrid[playerinput] = "X"
        os.system('cls')
    except IndexError:
        os.system('cls')
        if len(playerinput) != 2:
            print("Invalid input. Input should be in format: x y")         
        else:
            print("Input out of range")
    except:
        os.system('cls')
        print("Invalid input. Input should be in format: x y")
import pygame
import main #imports functions from the ASCII base
import math
import numpy as np
# pygame setup
pygame.init()
windowwidth = 600
windowheight = 600
offset=50 #how far the grid should be from the window border
screen = pygame.display.set_mode((windowwidth, windowheight))
pygame.display.set_caption("Connect Boxes")
clock = pygame.time.Clock()
running = True
dt = 0
background = pygame.image.load("images/background.jpg")
gridsize = 10
gamegrid = np.full((gridsize,gridsize), " ")
running = True
font =  pygame.font.SysFont("Arial",30)
playerwintext = font.render(("Player Wins"),True,(255,255,255))
aiwintext = font.render(("AI Wins"),True,(0,0,0))
clickpos = 0,0
def win(value):
    global running
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if value == "X":
            screen.blit(playerwintext,(10,10))
        elif value == "O":
            screen.blit(aiwintext,(10,10))
        pygame.display.flip()
        dt = clock.tick(60) / 1000
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            clickpos = pygame.mouse.get_pos()
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")
    screen.blit(background,(0,0))
    blocksize = int((windowwidth-(2*offset))/10) #Set the size of the grid block
    for x in range(offset, windowwidth-offset, blocksize):
        for y in range(offset, windowheight-offset, blocksize):
            rect = pygame.Rect(x, y, blocksize, blocksize)
            playerinput = tuple(math.floor((i-offset)/blocksize) for i in clickpos) #get grid coordinate of mouse click
            rectcoord = tuple(math.floor((i-offset)/blocksize) for i in (x,y)) #get grid coordinate of current square
            try:
                gamegrid[playerinput] #check if click is outside of the grid
            except IndexError:
                playerinput = -1,-1
            if rect.collidepoint(clickpos) & (gamegrid[playerinput[::-1]] == " "): #player clicks an empty square
                gamegrid[playerinput[::-1]] = "X"
                main.ai(gamegrid)
            if (gamegrid[rectcoord[::-1]] == "X"): #checks if move exists in grid, and changes the colour of the square
                pygame.Surface.fill(screen,"blue",rect)
                pygame.draw.rect(screen, "black", rect, 1)
            elif gamegrid[rectcoord[::-1]] == "O":
                pygame.Surface.fill(screen,"red",rect)
                pygame.draw.rect(screen, "black", rect, 1)
            else:
                pygame.Surface.fill(screen,"white",rect)
                pygame.draw.rect(screen, "black", rect, 1)
    if main.checkingrid(gamegrid,"XXXXX"):
        win("X")
    if main.checkingrid(gamegrid,"OOOOO"):
        win("O")
    pygame.display.flip()
    dt = clock.tick(60) / 1000
pygame.quit()
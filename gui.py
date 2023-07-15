# Example file showing a circle moving on screen
import pygame
import main
import math
import numpy as np
# pygame setup
pygame.init()
windowwidth = 600
windowheight = 600
offset=50
screen = pygame.display.set_mode((windowwidth, windowheight))
clock = pygame.time.Clock()
running = True
dt = 0
gridsize = 10
gamegrid = np.full((gridsize,gridsize), " ")
running = True
font =  pygame.font.SysFont("Arial",30)
playerwintext = font.render(("Player Wins"),True,(0,0,0))
aiwintext = font.render(("AI Wins"),True,(0,0,0))
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
    clickpos = 0,0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            clickpos = pygame.mouse.get_pos()
            print(clickpos)


    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")
    blocksize = int((windowwidth-(2*offset))/10) #Set the size of the grid block
    for x in range(offset, windowwidth-offset, blocksize):
        for y in range(offset, windowheight-offset, blocksize):
            rect = pygame.Rect(x, y, blocksize, blocksize)
            playerinput = tuple(math.floor((i-offset)/blocksize) for i in clickpos)
            rectcoord = tuple(math.floor((i-offset)/blocksize) for i in (x,y))
            if rect.collidepoint(clickpos) & (gamegrid[playerinput[::-1]] == " "):
                gamegrid[playerinput[::-1]] = "X"
                main.ai(gamegrid)
            if (gamegrid[rectcoord[::-1]] == "X"):
                pygame.Surface.fill(screen,"blue",rect)
                pygame.draw.rect(screen, "black", rect, 1)
            elif gamegrid[rectcoord[::-1]] == "O":
                pygame.Surface.fill(screen,"red",rect)
                pygame.draw.rect(screen, "black", rect, 1)
            else:
                pygame.draw.rect(screen, "black", rect, 1)
    if main.checkingrid(gamegrid,"XXXXX"):
        win("X")
    if main.checkingrid(gamegrid,"OOOOO"):
        win("O")
    pygame.display.flip()
    dt = clock.tick(60) / 1000
pygame.quit()
import pygame
import time
import random
import numpy as np
import os
import grid

os.environ["SDL_VIDEO_CENTERED"]='1'

#resolution
width, height = 780,780
size = (width, height)

pygame.init()

pygame.display.set_caption("CONWAY'S GAME OF LIFE")

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 24

black = (0, 0, 0)
blue = (0, 121, 150)
blue1 = (0,14,71)
white = (255, 255, 255)

scaler = 30
offset = 1

Grid = grid.Grid(width,height, scaler, offset)
Grid.random2d_array()

pause = False
run = True
while run:
    clock.tick(fps)
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_SPACE:
                pause = not pause
        if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                x,y=mouse_pos
                if Grid.grid_array[x//30][y//30] == 0:
                    Grid.grid_array[x//30][y//30] = 1
                    Grid.grid_alive[x//30][y//30] +=1
                print("This cell lived", int(Grid.grid_alive[x//30][y//30]), "times")
                print("And died", int(Grid.grid_dead[x//30][y//30]), "times")

    Grid.Conway(off_color=white, on_color=blue1, surface=screen, pause=pause)

   


    pygame.display.update()

pygame.quit()

import pygame
import numpy as np
import random

class Grid:
    def __init__(self, width, height, scale, offset):
        # side of the square  
        self.scale = scale

        self.columns = int(height/scale)
        self.rows = int(width/scale)

        # tuple for Example : (5, 10)
        self.size = (self.rows, self.columns)

        # cellular automata grid 
        self.grid_array = np.ndarray(shape=(self.size))
        self.grid_alive = np.ndarray(shape=(self.size))
        self.grid_dead = np.ndarray(shape=(self.size))
        
        self.offset = offset

    # intialize the grid with a random values
    def random2d_array(self):
        for x in range(self.rows):
            for y in range(self.columns):
                self.grid_array[x][y] = random.randint(0,1)
                self.grid_alive[x][y] = 0
                self.grid_dead[x][y] = 0
                if self.grid_array[x][y] == 1:
                    self.grid_alive[x][y] +=1


    def Conway(self, off_color, on_color, surface, pause):
        for x in range(self.rows):
            for y in range(self.columns):
                y_pos = y * self.scale + 15
                x_pos = x * self.scale + 15

                if self.grid_array[x][y] == 1:
                    if not pause:
                        on_color = (tuple(np.random.randint(256, size=3)))
                    pygame.draw.circle(surface, on_color, [x_pos, y_pos], 15)
                else:
                    pygame.draw.circle(surface, off_color, [x_pos, y_pos], 15)

        next = np.ndarray(shape=(self.size))
        if pause == False:
            for x in range(self.rows):
                for y in range(self.columns):
                    state = self.grid_array[x][y]
                    neighbours = self.get_neighbours( x, y)
                    if state == 0 and neighbours == 3:
                        next[x][y] = 1
                        self.grid_alive[x][y] +=1
                    elif state == 1 and (neighbours < 2 or neighbours > 3):
                        next[x][y] = 0
                        self.grid_dead[x][y] += 1
                    elif state ==1 and neighbours<=1:
                        if (np.random.randint(100)<=79):
                            next[x][y] = 0
                            self.grid_dead[x][y] += 1
                    else:
                        next[x][y] = state
            self.grid_array = next


    def get_neighbours(self, x, y):
        total = 0
        for n in range(-1, 2):
            for m in range(-1, 2):
                x_edge = (x+n) % self.rows
                y_edge = (y+m) % self.columns
                total += self.grid_array[x_edge][y_edge]

        total -= self.grid_array[x][y]
        return total

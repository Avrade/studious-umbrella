import pygame as pg
from random import randint

#Se lance au debut du programme
grid = [[0 for i in range(10)] for j in range(20)]

print(grid)
#Tourne dans le vide
def loop():
    pass

def draw():
    for i in grid:
        print(i)


class Tetromino:
    def __init__(self, n):
        self.pos = 4, 0
        if n == 0: #Carré
            self.shape = [[[1,1,0,0],
                          [1,1,0,0],
                          [0,0,0,0],
                          [0,0,0,0]],
                          [[1,1,0,0],
                          [1,1,0,0],
                          [0,0,0,0],
                          [0,0,0,0]],
                          [[1,1,0,0],
                          [1,1,0,0],
                          [0,0,0,0],
                          [0,0,0,0]],
                          [[1,1,0,0],
                          [1,1,0,0],
                          [0,0,0,0],
                          [0,0,0,0]]]

            self.col = pg.Color(255,255,0)

        elif n == 1: #Ligne
            self.shape = [[[1,1,1,1],
                          [0,0,0,0],
                          [0,0,0,0],
                          [0,0,0,0]],
                          [[1,0,0,0],
                          [1,0,0,0],
                          [1,0,0,0],
                          [1,0,0,0]],
                          [[1,1,1,1],
                          [0,0,0,0],
                          [0,0,0,0],
                          [0,0,0,0]],
                          [[1,0,0,0],
                          [1,0,0,0],
                          [1,0,0,0],
                          [1,0,0,0]]]
            self.col = pg.Color(0,255,255)

        elif n == 2: #L
            self.shape = [[[0,0,1,0],
                          [1,1,1,0],
                          [0,0,0,0],
                          [0,0,0,0]],
                          [[0,0,1,0],
                          [1,1,1,0],
                          [0,0,0,0],
                          [0,0,0,0]],
            self.col = pg.Color(255,145,0)
        elif n == 3: #J
            self.shape = [[1,0,0,0],
                          [1,1,1,0],
                          [0,0,0,0],
                          [0,0,0,0]]
            self.col = pg.Color(0,0,255)

        elif n == 4: #Z
            self.shape = [[1,1,0,0],
                          [0,1,1,0],
                          [0,0,0,0],
                          [0,0,0,0]]
            self.col = pg.Color(255,0,0)

        elif n == 5: #S
            self.shape = [[0,1,1,0],
                          [1,1,0,0],
                          [0,0,0,0],
                          [0,0,0,0]]
            self.col = pg.Color(0,255,0)

        elif n == 6: #T
            self.shape = [[0,1,0,0],
                          [1,1,1,0],
                          [0,0,0,0],
                          [0,0,0,0]]
            self.col = pg.Color(255,0,255)

import pygame as pg
from random import randint

#Se lance au debut du programme
grid = [[0 for _ in range(10)] for _ in range(20)]

#Score de départ
score = 0

#2 Next initiaux
tet_next_1 = Tetromino(randint(0,6))
tet_next_2 = Tetromino(randint(0,6))
tet_actuel = Tetromino(randint(0,6))
tet_stock = None

def stock():
    tet_stock = tet_actuel
    if tet_stock == None:
        tet_actuel = Tetromino(randint(0,6))
    else:
        tet_actuel = tet_stock

#Nexts
def nexts():
    tet_actuel = tet_next_1
    tet_next_1 = tet_next_2
    tet_next_2 = Tetromino(randint(0,6))

#Elimination ligne comlète
def elim():
    elims = 0 #Nombre d'éliminations d'un coup
    for i in grid:
        if i == [2 for _ in range(10)]:
            grid.remove(i)
            grid.insert(0,[0 for _ in range(10)])
            elims += 1
    #Répartition du score
    if elims == 1:
        score += 100
    elif elims == 2:
        score += 200
    elif elims == 3:
        score += 400
    elif elims == 4:
        score += 1200

#Tourne dans le vide
def loop():
    draw()

def draw():
    for i in grid:
        print(i)

#Main
while True:
    loop()

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

import pygame as pg
from random import randint

class Tetromino:
    def __init__(self, n):
        self.pos = [4, 0, 0]
        if n == 1: #Carré
            self.shape = [[[n,n,0,0],
                          [n,n,0,0],
                          [0,0,0,0],
                          [0,0,0,0]],
                          [[n,n,0,0],
                          [n,n,0,0],
                          [0,0,0,0],
                          [0,0,0,0]],
                          [[n,n,0,0],
                          [n,n,0,0],
                          [0,0,0,0],
                          [0,0,0,0]],
                          [[n,n,0,0],
                          [n,n,0,0],
                          [0,0,0,0],
                          [0,0,0,0]]]


        elif n == 2: #Ligne
            self.shape = [[[n,n,n,n],
                          [0,0,0,0],
                          [0,0,0,0],
                          [0,0,0,0]],
                          [[n,0,0,0],
                          [n,0,0,0],
                          [n,0,0,0],
                          [n,0,0,0]],
                          [[n,n,n,n],
                          [0,0,0,0],
                          [0,0,0,0],
                          [0,0,0,0]],
                          [[n,0,0,0],
                          [n,0,0,0],
                          [n,0,0,0],
                          [n,0,0,0]]]

        elif n == 3: #L
            self.shape = [[[0,0,n,0],
                          [n,n,n,0],
                          [0,0,0,0],
                          [0,0,0,0]],
                          [[n,0,0,0],
                          [n,0,0,0],
                          [n,n,0,0],
                          [0,0,0,0]],
                          [[n,n,n,0],
                          [n,0,0,0],
                          [0,0,0,0],
                          [0,0,0,0]],
                          [[n,n,0,0],
                          [0,n,0,0],
                          [0,n,0,0],
                          [0,0,0,0]]]

        elif n == 4: #J
            self.shape = [[[n,0,0,0],
                          [n,n,n,0],
                          [0,0,0,0],
                          [0,0,0,0]],
                          [[n,n,0,0],
                          [n,0,0,0],
                          [n,0,0,0],
                          [0,0,0,0]],
                          [[n,n,n,0],
                          [0,0,n,0],
                          [0,0,0,0],
                          [0,0,0,0]],
                          [[0,n,0,0],
                          [0,n,0,0],
                          [n,n,0,0],
                          [0,0,0,0]]]

        elif n == 5: #S
            self.shape = [[[n,n,0,0],
                          [0,n,n,0],
                          [0,0,0,0],
                          [0,0,0,0]],
                          [[0,n,0,0],
                          [n,n,0,0],
                          [n,0,0,0],
                          [0,0,0,0]],
                          [[n,n,0,0],
                          [0,n,n,0],
                          [0,0,0,0],
                          [0,0,0,0]],
                          [[n,n,0,0],
                          [0,n,0,0],
                          [0,n,0,0],
                          [0,0,0,0]]]

        elif n == 6: #Z
            self.shape = [[[0,n,n,0],
                          [n,n,0,0],
                          [0,0,0,0],
                          [0,0,0,0]],
                          [[n,0,0,0],
                          [n,n,0,0],
                          [0,n,0,0],
                          [0,0,0,0]],
                          [[0,n,n,0],
                          [n,n,0,0],
                          [0,0,0,0],
                          [0,0,0,0]],
                          [[n,0,0,0],
                          [n,n,0,0],
                          [0,n,0,0],
                          [0,0,0,0]]]

        elif n == 7: #T
            self.shape = [[[0,n,0,0],
                          [n,n,n,0],
                          [0,0,0,0],
                          [0,0,0,0]],
                          [[n,0,0,0],
                          [n,n,0,0],
                          [n,0,0,0],
                          [0,0,0,0]],
                          [[n,n,n,0],
                          [0,n,0,0],
                          [0,0,0,0],
                          [0,0,0,0]],
                          [[0,n,0,0],
                          [n,n,0,0],
                          [0,n,0,0],
                          [0,0,0,0]]]

    def rotate():
        self.pos[2] = (self.pos[2] + 1) % 4

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

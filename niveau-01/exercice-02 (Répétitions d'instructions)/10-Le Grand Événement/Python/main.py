from robot import *

for _ in range(9):
    haut()

for _ in range(4):
    droite()

    for _ in range(8):
        bas()

    droite()

    for _ in range(8):
        haut()

droite()

for _ in range(9):
    bas()

for _ in range(9):
    gauche()

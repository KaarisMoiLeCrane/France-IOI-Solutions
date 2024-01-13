from robot import *

nbr_aller_retour = 1

for _ in range(10):
    for _ in range(nbr_aller_retour):
        droite()
    ramasser()

    for _ in range(nbr_aller_retour):
        gauche()
    deposer()

    nbr_aller_retour += 1

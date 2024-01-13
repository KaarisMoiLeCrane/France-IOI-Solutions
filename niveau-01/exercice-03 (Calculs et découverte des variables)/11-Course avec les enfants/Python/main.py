from robot import *

anneau = 1

for _ in range(10):
    for _ in range(anneau):
        droite()
    ramasser()

    for _ in range(anneau):
        gauche()
    deposer()

    anneau += 1

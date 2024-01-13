from robot import *

for _ in range(108):
    for sens_du_deplacement in [haut, droite, bas, gauche]:
        for _ in range(13):
            sens_du_deplacement()

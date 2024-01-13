date_debut = int(input())
date_fin = int(input())
nbr_entrees = int(input())
nbr_personnes_espion = 0

for _ in range(nbr_entrees):
    date_arrivee = int(input())
    if date_debut <= date_arrivee <= date_fin:
        nbr_personnes_espion += 1
print(nbr_personnes_espion)

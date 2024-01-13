date_debut = int(input())
date_fin = int(input())
nbr_entrees = int(input())
nbr_personnes_espion = sum(
    1 for _ in range(nbr_entrees) if date_debut <= int(input()) <= date_fin
)
print(nbr_personnes_espion)

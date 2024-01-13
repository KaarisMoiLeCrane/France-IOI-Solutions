nbr_cubes = 0
largeur_arete = 1

for _ in range(9):
    nbr_cubes += largeur_arete**3
    largeur_arete += 2
print(nbr_cubes)

nbr_lignes = 1
nbr_colonnes = 1

for _ in range(20):
    for _ in range(20):
        print(nbr_colonnes * nbr_lignes, end=" ")
        nbr_lignes += 1
    print()

    nbr_lignes = 1
    nbr_colonnes += 1

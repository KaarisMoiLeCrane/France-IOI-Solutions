nbr_lignes = 1

for _ in range(20):
    nbr_colonnes = 1

    for _ in range(20):
        print(nbr_colonnes * nbr_lignes, end=" ")
        nbr_colonnes = nbr_colonnes + 1
    print()

    nbr_lignes = nbr_lignes + 1

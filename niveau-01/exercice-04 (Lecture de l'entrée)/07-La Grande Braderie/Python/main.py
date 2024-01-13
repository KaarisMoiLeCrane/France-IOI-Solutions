position_depart = int(input())
largeur_emplacement = int(input())
nbr_vendeurs = int(input())

for _ in range(nbr_vendeurs + 1):
    print(position_depart)
    position_depart += largeur_emplacement

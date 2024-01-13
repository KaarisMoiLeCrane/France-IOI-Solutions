nbr_joueurs = int(input())
poids_equipe1 = 0
poids_equipe2 = 0

for _ in range(nbr_joueurs):
    poids_joueur_equipe1 = int(input())
    poids_equipe1 += poids_joueur_equipe1

    poids_joueur_equipe2 = int(input())
    poids_equipe2 += poids_joueur_equipe2

if poids_equipe1 > poids_equipe2:
    print("L'équipe 1 a un avantage")
else:
    print("L'équipe 2 a un avantage")

print("Poids total pour l'équipe 1 :", poids_equipe1)
print("Poids total pour l'équipe 2 :", poids_equipe2)

date_debut = int(input())
date_fin = int(input())
nbr_invites = int(input())
nbr_suspects = 0

for _ in range(nbr_invites):
    date_arrivee = int(input())
    date_depart = int(input())
    innocent = (date_depart < date_debut) or (date_arrivee > date_fin)
    if not innocent:
        nbr_suspects += 1

print(nbr_suspects)

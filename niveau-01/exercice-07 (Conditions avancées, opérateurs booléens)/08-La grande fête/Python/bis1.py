date_debut = int(input())
date_fin = int(input())
nbr_invites = int(input())
invites = iter((int(input()), int(input())) for _ in range(nbr_invites))

nbr_suspects = sum(
    1
    for (date_arrivee, date_depart) in invites
    if (date_depart >= date_debut) and (date_arrivee <= date_fin)
)

print(nbr_suspects)

date_debut = int(input())
date_fin = int(input())
nbr_entrees = int(input())

print(
    sum(
        1 for _ in range(nbr_entrees) if int(input()) in range(date_debut, date_fin + 1)
    )
)

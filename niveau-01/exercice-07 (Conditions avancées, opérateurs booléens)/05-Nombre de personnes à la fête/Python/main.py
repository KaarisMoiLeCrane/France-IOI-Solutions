nbr_personnes = int(input())
total_personnes = 0
record = 0

for _ in range(2 * nbr_personnes):
    nbr_personnes_entree_sortie = int(input())
    if nbr_personnes_entree_sortie < 0:
        total_personnes -= 1
    else:
        total_personnes += 1
    if total_personnes > record:
        record = total_personnes

print(record)

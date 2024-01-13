jours_marche = int(input())
record = 0

for _ in range(jours_marche):
    distance_parcourue = int(input())
    if distance_parcourue > record:
        record = distance_parcourue

print(record)

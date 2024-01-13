nbr_villes = int(input())
total_villes = 0

for _ in range(nbr_villes):
    population = int(input())

    if population > 10 * 1000:
        total_villes += 1

print(total_villes)

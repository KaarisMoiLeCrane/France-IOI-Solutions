nbr_montees = int(input())
total_montee = 0
total_descente = 0

for _ in range(nbr_montees):
    variation_altitude = int(input())
    if variation_altitude > 0:
        total_montee += variation_altitude
    else:
        total_descente += variation_altitude

print(total_montee)
print(-total_descente)

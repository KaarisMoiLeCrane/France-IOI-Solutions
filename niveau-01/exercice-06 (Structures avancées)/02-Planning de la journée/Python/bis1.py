position_actuelle = int(input())
nbr_villages = int(input())
total_villages = 0

for _ in range(nbr_villages):
    position_village = int(input())
    ecart = abs(position_village - position_actuelle)

    if ecart <= 50:
        total_villages += 1

print(total_villages)

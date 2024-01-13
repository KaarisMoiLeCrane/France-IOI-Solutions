position_actuelle = int(input())
nbr_villages = int(input())
total_villages = 0

for _ in range(nbr_villages):
    position_village = int(input())
    difference = position_village - position_actuelle

    if difference <= 50 and difference >= -50:
        total_villages += 1

print(total_villages)

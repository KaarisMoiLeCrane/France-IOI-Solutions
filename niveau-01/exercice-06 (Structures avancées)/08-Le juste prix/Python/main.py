nbr_marchands = int(input())

marchand_moins_cher, prix_min = 1, 1000000

for position_marchand in range(1, nbr_marchands + 1):
    prix = int(input())
    if prix < prix_min:
        marchand_moins_cher, prix_min = position_marchand, prix

print(marchand_moins_cher)

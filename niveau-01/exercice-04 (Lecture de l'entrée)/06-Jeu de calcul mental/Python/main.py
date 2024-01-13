nbr_nombres = int(input())
nbr_depart = 66
nbr_increment = 1

for _ in range(nbr_nombres):
    print(nbr_depart)
    nbr_increment += 1
    nbr_depart *= nbr_increment

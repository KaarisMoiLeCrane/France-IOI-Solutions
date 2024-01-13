nbr_jetons = int(input())

for _ in range(nbr_jetons):
    x = int(input())
    y = int(input())
    dans_feuille = x > 0 and x < 90 and y > 0 and y < 70
    zone_jaune_milieu = x > 25 and x < 50 and y > 20 and y < 45
    if not dans_feuille:
        print("En dehors de la feuille")
    elif ((x > 15 and x < 45) or (x > 60 and x < 85)) and y > 60:
        print("Dans une zone rouge")
    elif not zone_jaune_milieu and x > 10 and x < 85 and y > 10 and y < 55:
        print("Dans une zone bleue")
    else:
        print("Dans une zone jaune")

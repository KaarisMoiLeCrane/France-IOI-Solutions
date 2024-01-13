borne_depart = int(input())
borne_arrivee = int(input())

difference = borne_arrivee - borne_depart

if difference < 0:
    difference = -difference

print(difference)

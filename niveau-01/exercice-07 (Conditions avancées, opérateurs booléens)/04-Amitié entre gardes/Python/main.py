date_debut_premier = int(input())
date_fin_premier = int(input())
date_debut_second = int(input())
date_fin_second = int(input())

if (date_fin_second < date_debut_premier) or (date_fin_premier < date_debut_second):
    print("Pas amis")
else:
    print("Amis")

mois = int(input())
print(29 if mois == 11 else 31 if mois >= 4 and mois <= 6 or mois == 10 else 30)

nbr_bagages = int(input())
poids_bagages = int(input())
poids_total = nbr_bagages * poids_bagages

if poids_total > 105:
    print("Surcharge !")

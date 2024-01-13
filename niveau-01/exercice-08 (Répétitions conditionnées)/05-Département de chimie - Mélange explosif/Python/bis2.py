total_mesures = int(input())
temperature_min = int(input())
temperature_max = int(input())
alerte = False

for _ in range(total_mesures):
    temperature = int(input())
    if not(alerte) and temperature_min <= temperature <= temperature_max:
        print("Rien à signaler")
    else:
        if not alerte:
            print("Alerte !!")
            alerte = True

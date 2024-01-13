total_mesures = int(input())
temperature_min = int(input())
temperature_max = int(input())

for _ in range(total_mesures):
    temperature = int(input())
    if temperature_min <= temperature <= temperature_max:
        print("Rien à signaler")
    else:
        print("Alerte !!")
        break
